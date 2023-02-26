/*fonction affichant le choix de la classe*/
function choixNiveau() {
	const selecteur = document.getElementById('choix');
	const niveauSel = selecteur[selecteur.selectedIndex];
	if ( niveauSel.value == 1 ) {
		alert("Vous avez choisi le niveau gratuit");
	}
	else if ( niveauSel.value == 2 ) {
		alert("Vous avez choisi l'adhésion premium !")
	}
	else { 
		alert("Vous avez choisi le niveau gold !")
	}	
}
/*Fonction test nombre*/
function isInt(value) {
	var x;
	if (isNaN(value)) {
	  return false;
	}
	x = parseFloat(value);
	return (x | 0) === x;
  }

/*Fonction vérification de l'âge*/
function verifAge() {
	var age = document.getElementById('age1');
	if ((isInt(age.value)==true)) {
		if (age.value < 15) {
			alert("Tu es trop jeune !");
			}
		else if ( age.value =="") {
			alert("Valeur obligatoire !");
		}
		else {
			alert("Valeur enregistrée !") ;
		};
	}
	else if ( age.value =="") {
		alert("Valeur obligatoire !") ;
	}
	else {
		alert("Merci d'entrer un nombre !");
	}
}

/*Fonction vérification du mail*/
function verifMail() {
	var mail = document.getElementById('mail');
	if ( mail.value =="") {
		alert("Valeur obligatoire !") ;
	}
	else {
		if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail.value))  {
		alert("Valeur enregistrée !") ;
		}
		else {
			alert("Vous avez entré une adresse mail invalide") ;
		} ;
	}

}
