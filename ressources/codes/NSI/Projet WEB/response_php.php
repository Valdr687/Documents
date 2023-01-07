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
	<p>	<?php
		if (isset($_GET['melon']) AND $_GET['melon']==1 ) {
			echo "Vous avez choisi melon d'eau, c'est une mauvaise réponse.";		
		} 
		elseif (isset($_GET['melon']) AND $_GET['melon']==2 ) {
			echo "Vous avez choisi pastèque, c'est une bonne réponse!";	
		} 
		else {
			echo "Vous n'avez pas répondu." ;
		}
		?></p>
	<p></p>
	<p>	<?php
		if (isset($_POST['banane']) AND $_POST['banane']==1 ) {
			echo "Vous avez choisi manger, c'est une réponse logique mais fausse !.";		
		}
		elseif (isset($_POST['banane']) AND $_POST['banane']==2 ) {
			echo "Vous avez choisi Faire glisser les autres, ce n'est pas la bonne réponse!";	
		} 
		elseif (isset($_POST['banane']) AND $_POST['banane']==3 ) {
			echo "Vous avez choisi banana for scale, c'est la bonne réponse !";	
		} 
		else {
			echo "Vous n'avez pas répondu." ;
		}
		?></p>
	<p></p>
	<p>	<?php
		if (isset($_GET['Gif']) AND $_GET['Gif']==1 ) {
			echo "Vous avez choisi Gif, c'est la bonne réponse ! ";		
		} 
		elseif (isset($_GET['Gif']) AND $_GET['Gif']==2 ) {
			echo "Vous avez choisi Jif, c'est une mauvaisse réponse.";	
		} 
		else {
			echo "Vous n'avez pas répondu." ;
		}
		?></p>
	<p></p>
	<p><?php
		if (isset($_GET['choc']) AND $_GET['choc']==1 ) {
			echo "Vous avez choisi pain au chocolat, c'est la bonne réponse ! ";		
		} 
		elseif (isset($_GET['choc']) AND $_GET['choc']==2 ) {
			echo "<img src='./images/test/monopoly.png' />";	
		} 
		else {
			echo "Vous n'avez pas répondu, ce qui est théoriquement impossible." ;
		}
		?></p>
	</div>

		
</body>
</html>
