// Fonction pour extraire le premier lien correspondant à un fichier MP3 ou M4A
function extractAudioLink(html) {
    const regex = /https?:\/\/[^"']*?\.(?:mp3|m4a)/i;
    const match = regex.exec(html);
    if (match && match[0]) {
        return match[0];
    }
    return null;
}

// Fonction pour télécharger le fichier audio
function downloadAudio() {
    // Récupérer l'onglet actif
    browser.tabs.query({ active: true, currentWindow: true }).then((tabs) => {
        const activeTab = tabs[0];
        // Récupérer le contenu de la page
        browser.tabs.sendMessage(activeTab.id, { action: 'getHtml' }).then((response) => {
            const html = response.html;
            // Extraire le lien audio
            const audioLink = extractAudioLink(html);
            if (audioLink) {
                // Créer un élément <a> pour le téléchargement
                const downloadLink = document.createElement('a');
                downloadLink.href = audioLink;
                downloadLink.download = 'audio.mp3';
                // Simuler un clic sur le lien pour lancer le téléchargement
                downloadLink.click();
            } else {
                console.log('Aucun lien audio trouvé.');
            }
        });
    });
}

document.getElementById("text").textContent="newtext";
// Ajouter un gestionnaire d'événement pour le clic sur le bouton de téléchargement
document.getElementById('downloadBtn').addEventListener('click', downloadAudio);
