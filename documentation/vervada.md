# Comment fonctionne le css du site du Vervada ?
- Je vais essayer d'y répondre pour le futur moi.

# Linktree.css

```css
.profil {
    margin: 10px auto; /* marge en haut de 10px - contenu centré*/
    width: fit-content; /* la div s'adapte au contenu*/
}
.icone {
   width: 96px; height: 96px; /* icone en 96/96px*/
   margin: 0 calc(50% - 48px); /* marge basse et haute nulle - contenu centré grace à soustraction de 50% du parent - 50% de l'image*/
}
.bio {
    max-width: 60%; /* choix esthétique = widht de .vignette*/
    margin: 0 auto; /* auto permet de centrer*/
}
```

## Liens
- ```<div .liens>``` --> tous les liens 
- ```<a .lien>``` --> lien unique vers un réseau social, élément parent de la div d'affichage ```<div .vignette>```
- ```<div .vignette>``` --> élément enfant ( petit fils de <div .liens> ) contenant l'icone et le texte représentatif du compte
	
```css
.liens { display: flex; /* design responsif*/
    flex-wrap: wrap;
    flex-direction: column;
    justify-content: space-evenly;
    height: 100%; /* la div occupe tt l'espace */
}

.lien { 
    display: block; /*permet l'affichage de la div enfant*/
}
      
.vignette {
    width: 60%; 
    margin: 1em 20%;
    display: grid; /* grid permet de gérer l'icone et le texte
    grid-auto-rows: 100%; 
    grid-template-columns: 30% 70%; /* icone représente 30 % et le texte 70%*/
    gap: 0px 5px; /* ecart null car inutile - 5px entre la gauche et la droite*/
    height: 80px;
    z-index: 2;
    cursor: pointer; /*curseur indique le lien*/
    /*aspect similaire à du verre, semi-transparent */
    border-radius: 25% 10%;
    box-shadow: 20px 20px 50px #10101040;
    border-radius: 15px;
    border-top: 1px solid #e8f5f550;
    border-left: 1px solid #e8f5f550;
    background: #10101010;
    backdrop-filter: blur(5px);
    overflow: hidden;
}
.gauche { grid-area: 1 / 1 / 2 / 2;
    place-items: center; /*centre le contenu*/
    padding:24px 0;
}
.droite { grid-area: 1 / 2 / 2 / 3; 
    place-items: center; /*centre le contenu*/
    text-align: center; /*centre le contenu*/
}
.droite p {
    position: absolute;
    top: 10px;
    margin: 5px;
}
.image { /*image en 32px format 1/1*/
    width: 32px;
    height: 32px;
    margin: 24px auto; position: absolute; top: 50% ; left: 10px; /* permet de centrer */
}
```

## Police, gestion des titres

```css
a:any-link {
    text-decoration: inherit;
    color: inherit;
}

p {
	font-family:  sans-serif;
	font-size: 14px;
}
h1 {
	font-family:  serif;
	font-size: 2em;
  	margin: 0 0.5em;
}
```

## Eléments généraux

- le footer doit avoir une taille fixe : 100% de large et 38px de haut

```css
footer {
	text-align: center !important;
	padding: 0px 5%;
	width: 90%;
	height: auto;
	position: relative ;
  	margin: 5px 0px !important;
}
footer p {
    margin: 0; 
}


main {
    margin: 0px auto; /* div centrée
    min-height: calc(100vh - 38px); /* hauteur minale de la hauteur de l'écran moins celle du <footer>*/
    width: fit-content; max-width: 680px; 
    text-align: center !important; /* le texte doit etre centré*/
   
}

/* déclaration de base - filet de secours pour gérer les moindres détails*/
html {
    min-height: 100vh;
    width: 100%;
    margin: 0;
    
}
      
body {
  background: linear-gradient(180deg, rgba(46,226,255,1) 0%, rgba(18,53,98,1) 100%); /* dégradé*/
  background: rgb(46,226,255); /* si le dégradé plante coté client*/
  color: #e8f5f5; /*couleur du texte - proche du blanc*/
  margin: 0;
  padding: 0;
}
```

# Style acceuil

- L'unique différence entre "style_accueil.css" et "style_accueil_dark.css" est la couleur. Mais je pense que c'est évident.

## Couleurs :

* *Thème clair :*
```css
body {
	background: #ccd3db; /*fond clair*/
	color: #101010; /*texte sombre*/
}
header, .nav-sub {
	background:  #ac541c; /* fond de l'entete et du menu de navigation ( pour mobile) orange (inexact mais il y a l'hexadecimal donc...) */
}
footer {
	background-color: #11111180; /*Fond noir transparent à 80%, ça donne du gris*/
}
h1, .prev,.next {
	color: #f4f4f4; /*titre et flèches du diapo noir*/
}
.bar1,.bar2,.bar3, .dot{  
	background-color:#101010;  /*barres de l'hamburger et point du diapo noir*/
}
#switch_theme :hover {
	background-color: #11111180; /*icone sombre au survol*/
}
.prev:hover, .next:hover {
	background-color: rgba(0,0,0,0.8); /*boutons precedent et suivant sombres au survol*/
}
.active, .dot:hover {
	background-color: #717171; /*point actif ou survolé gris sombre*/
}
.mySlides img {
	border : 5px solid #101010; /*bordure des images du diapo noir et de 5px*/
}
.barre, .barre_petite {
	background-color: #101010; /*barres de séparation noires*/
}
```

* *Thème sombre : à ne pas confondre avec l'inverse du clair*

```css
body {
	background: #2e2d26; /*fond de la page noir*/
	color: #e8f5f1; /*texte blanc*/
}
header, .nav-sub {
	background:  #59402d ; /*en gros c'est orange*/
}
footer {
	background-color: #433c3c; /*fond gris sombre*/
}
h1, footer p , .prev,.next  {
	color: #f4f4f4; /*titre et flèches du diapo blancs*/
}
.bar1,.bar2,.bar3, .dot{  
	background-color:#101010; /*barres de l'hamburger et point du diapo noir*/
}
#switch_theme :hover {
	background-color: #11111180;  /*icone sombre au survol*/
}
.prev:hover, .next:hover {
	background-color: rgba(0,0,0,0.8);  /*boutons precedent et suivant sombres au survol*/
}
.active, .dot:hover {
	background-color: #717171; /*point actif ou survolé gris sombre*/
}
.mySlides img {
	border : 5px solid #101010; /*bordure des images du diapo noir et de 5px*/
}
.barre, .barre_petite {
	background-color: #f4f4f4  ; /*barres de séparation blanches*/
}
```
## Eléments généraux 

- Style sur classe :
```css
body { /*déclarations générales*/
	width:100%; 
	min-height: 100vh;
	margin: 0;
}


header { 
	z-index: 100; /*header doit etre devant*/
    height: 70px; /*hauteur de 70px*/
    width: 100%; /*largeur de la page*/
    position: fixed; /*fixé en haut*/
    top: 0; left : 0 ;
    

}

a:any-link { 
	color: inherit;
	text-decoration: none; /*pas de différence formelle avec du texte classique */
}

main { /*contient la page*/
	position: relative; /*placé après l'entete*/
	margin: 72px 80px 10px 80px; /*marge pour la lissiblité du contenu, modifiée par la suite avec des @media queries*/
	padding: 20px; 
	min-height: 100vh; /*occupé cette portion de l'écran fait que le footer sera en dessous quoi qu'il arrive*/
}
```
## Style sur classe
( classes bassiques uniquements )

``` css
.logo {
	max-width: fit-content; /*mesure 32*32px*/
	min-height: 32px; 
	position: fixed; /*reste en haut*/
	top: 5px; left : 50px ;
}

.texte_centre {
	text-align: center; /*texte centré, je pense que c'est clair*/
}

/*Barres de séparation, liées à des <span class="barre">*/
.barre {
	display: block;
	width:50%;  
	height:3px;  
	margin:5px auto;  
}
.barre_petite {
	display: block;
	width:20%;  
	height:3px;  
	margin:5px 0;  
}
```
## Polices, gestion des titres

```css
p {
	font-family: 'Quicksand', sans-serif; /*quicksand est utilisé pour le texte sinon c'est sans-serif*/
	line-height: 1em;
	font-size: 14px;
}
h1 {
	font-family: 'Almendra SC', serif; /*Almendra SC est utilisé pour le texte sinon c'est serif*/
	font-size: 50px;
}

h2 {
	font-family: 'Almendra SC', serif;
	font-size: 25px;

}

.faq h3 {
	font-family: 'Quicksand', sans-serif;
	font-size: 18px;
}

.faq p {
	font-size: 14px;
}

article p {
	font-size: 18px; /*police plus grande pour les articles*/
}

article a:any-link {
	text-decoration: underline; /*liens soulignés dans les articles*/
}
```

## Layout mobile 

- Hamburger

```css
.ham{  
	display:block;
	position:absolute; /*placé en haut à droite*/
	top:23px ; left: 5px;  
	cursor: pointer;
}

/*anime les barres 1 et 3 pour faire une croix après un clic*/
.change .bar1 {  
   transform: rotate(45deg) translate(8px,3px);  
}  
.change .bar3 {  
   transform: rotate(-45deg) translate(8px,-3px);  
}
/*bar2 est cachée après ce clic*/
.change .bar2 {  
   opacity: 0;  
}  

.bar1,.bar2,.bar3{  
	display:block;  
	width:35px;  
	height:3px;  
	margin:5px auto;   
}
```

- Barre de navigation

```css
nav{  
	display:flex;  
	top:0;  
	height:100%;  
	justify-content:flex-start;  
	align-items:center;   
	padding:0px 20px;   
}  
  
.nav-sub{  
	display:flex;  
	justify-content:flex-start;  /*début à gauche*/
	height: 100%;
	align-items:center;   
}  
.list-item {  
	padding:10px;  
	list-style:none;  /*pas de puce en debut de ligne*/
}
.list-item-active, .list-item:hover {  
	text-decoration: underline; /*souligné qd actif ou au survol*/
	padding:10px;
	list-style:none;  
}    
.nav-link{  
	color:inherit;   /*comme le texte*/
	text-decoration:none;  
}
```   

## Pied de page et icone de theme

```css
#switch_theme {
	position: absolute; /*en haut à droite*/
	right: 15px ; top :15px ;
	width: 28px;
	height: 28px;
	border-radius: 8px;
	padding: 8px 0 0 8px; /*permet de centrer l'image*/
}
```
```css
footer {
	display: grid;
	text-align: center !important;
	grid-template-columns: 49% 49%;
	grid-template-rows: min-content;
	gap: 0px 2%;
	grid-auto-flow: row;
	justify-content: center;
	grid-template-areas:
	  "bas_gauche bas_droite";
	padding: 0px 5%;
	width: 90%;
	height: auto;
	position: relative ;	
}


.bas_gauche { grid-area: bas_gauche;
	display: grid;
	width: fit-content;
	margin: 0 auto;
	grid-template-columns: 100%;
	grid-template-rows: min-content;
	gap: 0px 0px;
	gap : 5px ;
	grid-auto-flow: row;
	grid-template-areas:
	  "haut"
	  "bas";
	grid-area: bas_gauche;
}
  
.bas_droite {  display: grid;
	width: fit-content;
	margin: 0 auto;
	grid-template-columns: 100%;
	grid-template-rows: min-content;
	gap: 0px 0px;
	gap : 5px ;
	grid-auto-flow: row;
	grid-template-areas:
	  "haut"
	  "bas";
	grid-area: bas_droite;
}
  
  
.haut { grid-area: haut; 
}
  
  
.bas { grid-area: bas; 
}

.haut, .bas {
	width: 100%;
	height: min-content;
	text-align:center;
}
```
## @media queries

- Règles d'affichage basique ( margin / padding de ```<main>```)

```css
@media (min-width: 2560px) { /*4K*/
	main {
		margin: 72px 10vw 10px 10vw;
		padding: 2vh 20px;
	}
	p {
		font-size: 20px !important;
	}
	h2 {
		margin-top: 1em;
		padding-top: 1em ;
	}
}

@media (min-width: 1440px) and (max-width: 2560px) { /*ordinteur portable L*/
	main {
		margin: 72px 10vw 10px 10vw;
		padding: 0 20px;
	}
}

@media (min-width: 1024px) { /*ordinteur portable*/
	main {
		margin: 72px 60px 10px 60px;
		padding: 0 20px;
	}
}

@media (max-width: 600px) {
	main {
		margin: 72px 40px 10px 40px;
		padding: 0 10px;
	}

}
@media (max-width: 500px) {
	main {
		margin: 72px 30px 10px 30px;
		padding: 0 10px;
	}
}

@media (max-width: 400px) {
	main {
		margin: 72px 20px 10px 20px;
		padding: 0 5px;
	}
}

@media (orientation: landscape) and (max-width: 1000px) {
	main {
		margin: 72px 20px 10px 20px;
		padding: 0 5px;
	}
}
```
- Règles pour le passage mobile / ordinateur

```css

@media (min-width: 768px) { /*Ecran de plus de 768px : ordinateur*/
	.logo {
		min-height: 32px;
		position: fixed;
		top: 5px; left : 5px ;
	}
	
	.ham{  
		display:none; /*hamburger caché*/
	}  
	 
	.bar1,.bar2,.bar3{  
		display:block;  
		width:35px;  
		height:3px;  
		margin:5px auto;  
		transition: 0.4s;  
	}   
}

@media (max-width :767px ) { /*Ecran de moins de 768px : téléphone ou tablette verticale*/
	.list-item {  
		padding:10px;  
		list-style:none;  
	}  
	.nav-link{  
		color:inherit;  
		text-decoration:none;  
	}  
	.nav-sub{  
		visibility: hidden;
		position:absolute;
		padding: 0 10px;  
		top:54px;  left:-6px;  
		flex-direction:column;   
		transition: transform 0.3s ease-in;  
		transform:translate(100%);
		height: 100vh;  
	}  
	.nav-change{  
		transform:translate(0%);  
		visibility: visible;
	} 
}
```

## Diapositive : ```index.html```

```css
.slideshow-container {
  	max-width: 80%;
 	position: relative;
  	margin: auto;
  	border-radius: 5px;
	height: fit-content;
}

.mySlides {
  display: none;
}

.mySlides img {
	z-index: 1;
	border-radius: 5px;
}


.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}
.next {
  right: -5px;
  border-radius: 3px 0 0 3px;
}
.prev {
	left: 5px;
	border-radius: 3px 0 0 3px;
}

.text { /*texte affiché en haut à gauche de l'image*/
	font-size: 15px;
	padding: 8px 12px;
	position: absolute;
	top: 10px;
	left: 10px;
	text-align: center;
}


.dots { /*conteneur de .dot*/
	text-align: center;
	position: absolute;
	bottom: 15px ;
	width: 100%;
}
.dot {
	cursor: pointer;
	height: 15px;
	width: 15px;
	margin: 0 2px;
	border-radius: 50%;
	display: inline-block;
	transition: background-color 0.6s ease;
	z-index: 2; /*devant l'image*/
}
```

## Galerie : ```showcase.html```

```css
.container { 
	display: grid;
	grid-template-columns: 1fr;
	grid-template-rows: repeat(5, 1fr);
	gap: 1em 1em;
	grid-template-areas:
	  	"ville"
	  	"wood"
		"flowers"
	  	"house"
		"axolotl";
}
  
.wood { grid-area: wood; background-color: #216793;}
  
.flowers { grid-area: flowers; 	background-color: #93216d;}
  
.ville { grid-area: ville; background-color: #937421;}
  
.house { grid-area: house; background-color: #3b9321;}
  
.axolotl { grid-area: axolotl; background-color: #217893;}

@media (min-width: 600px) {
	.container { 
		grid-template-columns: repeat(2, 1fr);
		grid-template-rows: repeat(3, 1fr);
		gap: 1em 1em;
		grid-template-areas:
			"ville ville"
			"wood flowers"
			"house axolotl";
	}
}

@media (min-width: 900px) {
	.container {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		grid-template-rows: repeat(3, 1fr);
		gap: 1em 1em;
		grid-template-areas:
			"ville ville ville"
			"wood wood flowers"
			"house axolotl axolotl";
	}
}
```
