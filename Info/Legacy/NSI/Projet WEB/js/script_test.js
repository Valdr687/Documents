function Banane() {
	const selecteur = document.getElementById('banane');
	const Banana = selecteur[selecteur.selectedIndex];
  if (Banana.value == 2) {
  	alert("Ce n'est pas très gentil...")
  }
}

function DernièreQuestion() {
	alert("Vous êtes arrivés à la dernière question, bonne chance.")
}

function Fin() {
	const selecteur = document.getElementById('choc');
	const PainChoc = selecteur[selecteur.selectedIndex];
  if (PainChoc.value == 1) {
  	alert("Vous avez terminé le questionnaire, merci de cliquer sur Valider")
  }
  if (PainChoc.value == 2) {
  	alert("Êtes-vous sûr?");
  }
}