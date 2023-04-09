#### [Retour](../README.md#documentation)

# Documentation

##  Portfolio :

- ### Stratégie générale
    - Une grille avec nav pour la barre latérale.
    - Body sous divisé en sections pour les images.
    - Chaque sous section se décompose en l'image et une div avec le titre.
- ### Nav 
    - titre : nom
    - items : div parent de la bio, du menu...
    - #menu : regroupe les "item", les liens de navigation
    - #social : liens vers les réseaux
- ### Main
    - section-type1 : un carré + un portrait
    - section-type2 : portrait + carré
    - section-type3 : 3 portraits
    - section-type4 : 4 paysages
    - section-type5 : 2 paysages + 1 portrait
- ### Image 
    - image-survol : filtre
    - image : div parent
    - image-actif : image active

## Couleurs

1. Thème clair / par défaut :
    - Couleurs d'arrière plan :
        - Couleur de fond : --fond-page ![#f5f5ee](https://via.placeholder.com/15/f5f5ee/000000.png?text=+) `#f5f5ee`
        - Fond secondaire : --fond-2 ![#204ecc](https://via.placeholder.com/15/204ecc/000000.png?text=+) `#204ecc`
        - Fond tertiaire : --fond-3
        - Fond quaternaire : --fond-4
        - Fond sombre : --fond-sombre ![#0f0f0f](https://via.placeholder.com/15/0f0f0f/000000.png?text=+) `#0f0f0f`
    - Couleurs textes :
        - Texte : --texte ![#131212](https://via.placeholder.com/15/131212/000000.png?text=+) `#131212` 
        - Citation : --citation ![#858585](https://via.placeholder.com/15/858585/000000.png?text=+) `#858585`
        - Texte clair : --texte-clair ![#eedbd3](https://via.placeholder.com/15/eedbd3/000000.png?text=+) `#eedbd3`
    - Couleurs d'accentuation :
        - Liens : --accentuation-1 ![#764d47](https://via.placeholder.com/15/764d47/000000.png?text=+) `#764d47`
    - Couleurs de survol :
        - Liens : --accentuation-2 ![#cc7320](https://via.placeholder.com/15/cc7320/000000.png?text=+) `#cc7320`

1. Thème sombre :
    - Couleurs d'arrière plan :
        - Couleur de fond : --fond-page ![#2b2a33](https://via.placeholder.com/15/2b2a33/000000.png?text=+) `#2b2a33`
        - Fond secondaire : --fond-2 ![#204ecc](https://via.placeholder.com/15/204ecc/000000.png?text=+) `#204ecc`
        - Fond tertiaire : --fond-3
        - Fond quaternaire : --fond-4
    - Couleurs textes :
        - Citation : --citation ![#858585](https://via.placeholder.com/15/858585/000000.png?text=+) `#858585`
    - Couleurs d'accentuation :
        - Liens : --accentuation-1 ![#96625a](https://via.placeholder.com/15/96625a/000000.png?text=+) `#96625a`

## CSS :

- Déclarations générales pour faciliter le positionnement, on définit une classe qui permet de cacher le défilement lors de l'ouverture d'une image (gràce à jquery) et des variables pour la réacivité.
```css
* {
	margin: 0;
	padding: 0;
}

.barre-cache {
	overflow-y: hidden !important; 
	overflow-x: hidden !important;
}

html,body {
	width: 100%;
	--Body-Nav:20%;
	--header-height:100px;
	min-height: 100vh;
	background-color: #ecd5ca;
}

```

- Structure générale pour pc (nav et main affichés ensembles):

```css
body {  display: grid;
	grid-template-columns: var(--Body-Nav) calc(100% - var(--Body-Nav)); 
    grid-template-rows: var(--header-height) max-content; 
    gap: 0 0; 
	grid-template-areas:
	  "header main"
	  "nav main";	
}

nav {
	grid-area: nav; 
	height: calc(100vh - var(--header-height)) ;
	width: 92%;
	padding: 0 4%;
	position: sticky;
	top: var(--header-height);
}

.hamburger {
	display: none;
}

main { grid-area: main; 
	height: fit-content;
	min-height: calc(100vh - 2%);
	width: 96%;
	padding: 2% 2% 0 2%;
	background-color: #eedbd3;
}

header {
	grid-area: header;
	height: var(--header-height) ;
	position: sticky;
	top: 0;
	display: flex;
	padding: 0 2%;
	justify-content: space-between;
	flex-direction: row;
	text-align: center;
	z-index: 2;
	background-color: inherit;
}

```
- Image : Description dans l'ordre parent>enfant
    - Image : ```<div>``` parent de ```<img>```, contient ```<div class=".image-survol">``` et le texte. 
        - image-survol : filtre sur l'image lors du survol qui permet de rendre le texte visible gràce à une animation détaillée plus bas
    - Image-actif : Image en plein écran, avec le texte visible. Il s'agit d'une grille.
        - image-survol : ```<div>``` permettant de positionner le texte lors d'une image en plein écran.  


  
- Effets lors du survol
    - Item de navigation : changement de la couleur
    ```css
    #menu .item:hover, .item-actif:hover {
	color: rgb(118,71,77);
    }
    ```
    - Icone : retour en couleur
    ```css
    #social img{
	filter: grayscale(100%);
	height: 100%;
    }

    #social img:hover {
	filter: grayscale(0);
    }
    ```
    - Image :
        - image survol : fond noir
        ```css
        .image-survol:hover {
	        background-color: #00000060;
        }
        ```
        - texte sur l'image : devient visible
        ```css
        .image-survol:hover .texte {
	        display: block;	
        }   
        ```

- Réactivité

    - Déclarations de base lors de l'utilation d'une tablette et plus petit
    ```css
    @media screen and (max-width: 768px) {
        body { 
            grid-template-areas:
                "header header"
                "main main";
            --header-height: 80px;	
        }
        .hamburger {
            display: inline-block;
        }
        nav {
            display: none;
        }
    }
    ```
    - .menu n'est nul autre ```<body>``` lors de l'activation du menu de navigation
    ```css
	.menu {
		grid-template-areas:
		"header header"
		"nav main";	 
		--Body-Nav: 40%;
	}
	.menu nav {
		display: block;
	}
	.image-actif {
		grid-template-columns: 64% 36%;
	}
    ```
	- Règles spécifiques au téléphones : la seule différence est que lorsqu'une image est en plein écran le texte est dessous.

    ```css
    @media screen and (max-width: 465px) {
        .image-actif {
            display: grid;
            grid-template-columns: 100%; 
            grid-template-rows: 70% 30%; 
            grid-template-areas:
            "img" 
            "texte";
        }
        .image-actif img {
            margin: auto;
            max-width: 96%;
            max-height: 98%;
        }
        .image-survol:hover .texte {
            display: none;	
        } 
        .image-actif .image-survol .texte {
            display: block;
        }   
    }
    ```

