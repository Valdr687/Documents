<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Réponse PHP</title>
	<link rel='stylesheet' href='./css/style_formulaire.css'>
	<link rel="icon" href="./images/globales/icon_small.png" type="image/icon type">
</head>
<body>
	<div class="corps">
	<h1>Bienvenue chez 13Informatique !</h1>
	<p></p>
	<?php
		if (isset($_POST['nom'])) {
			$nom = $_POST['nom'];		
		}
		else {
			$nom = 'Inconnu';	
		} ?>
	<p></p>
	<p>Votre nom est <?php echo $nom ?></p>
	<?php
		if (isset($_POST['age'])) {
			$age = $_POST['age'];		
		}
		else {
			$age = 'Inconnu';	
		} ?>
	<p></p>
	<p>Vous avez <?php echo $age ?> ans.</p>
	<?php
		if (isset($_POST['mail'])) {
			$mail = $_POST['mail'];		
		}
		else {
			$mail = 'Inconnu';	
		} ?>
	<p></p>
	<p>Votre adresse mail est <?php echo $mail ?></p>
	<?php
		if (isset($_POST['phone'])) {
			$phone = $_POST['phone'];		
		}
		else {
			$phone = 'Inconnu';	
		} ?>
	<p></p>
	<p>Votre numéro de téléphone est <?php echo $phone ?></p>
	<p><?php
		if (isset($_POST['homme']) AND empty($_POST['femme'])) {
			echo "Votre sexe est : ".$_POST['homme'];		
		}
		elseif (isset($_POST['femme']) AND empty($_POST['homme'])) {
			echo "Votre sexe est : ".$_POST['femme'];	
		} 
		else {
			echo "Votre sexe est inconnu." ;
		}
		?></p>
	<p></p>
	<p><?php
		if (isset($_POST['niveau']) AND $_POST['niveau']==1 ) {
			echo "Vous avez choisi le niveau gratuit.";		
		}
		elseif (isset($_POST['niveau']) AND $_POST['niveau']==2 ) {
			echo "Vous avez choisi le niveau premium !";	
		} 
		elseif (isset($_POST['niveau']) AND $_POST['niveau']==3 ) {
			echo "Vous avez choisi le niveau gold !";	
		} 
		else {
			echo "Vous n'avez pas défini de niveau d'adhsésion, ce qui équivaut au niveau 1." ;
		}
		?></p>
	<p></p>
	<p><?php
		if (isset($_POST['suscribe'])) {
			echo "Vous avez choisi de vous abonner à la newsletter.";		
		} 
		else {
			echo "Vous avez choisi de ne pas vous abonner à la newsletter !" ;
		}
		?></p>
	</div>
		
</body>
</html>
