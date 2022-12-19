# Créer son pack de texture Minecraft Java :

Ce tutoriel s'adresse à ceux qui veulent créer leur pack de texture soit à partir des textures du jeu directement ou bien en mélangeant des packs pris sur Internet.

## Comment marche un pack de texture ?

Le jeu divise les blocks en 3 parties, les items en 2 et les entités n'ont que leur texture.  

* ### Les Blocks :
    - Blockstates : ce fichier .json permet d'associer à chaque sous-état[^1] d'un block le model 3D associé, il permet également de rajouter des variants à un même sous-état[^1].  
    - Model : ce fichier .json définit le model utilisé par le block, il peut faire appel à un model parent
    - Texture(s) : un ou plusieurs .png, généralement un / coté
* ### Les items :
    - Model : ce fichier .json définit le model utilisé par l'item, il peut faire appel à un model parent et définit comment doit être affiché l'item dans l'inventaire, dans un cadre...
    - Texture(s) : un ou plusieurs ( si model 3d custom) .png
* ### Les entitées :
    - Texture : accesibles dans *NomDuPack*/assets/minecraft/textures/entity il existe soit un fichier / entitées ou un dossier avec des variants
* ### Nomenclature :
    - Tout les noms des fichiers sont ceux des identifiants présent dans le jeu, si vous jouez en anglais retrouver la texture de l'herbe(*grass*) est simple, il suffit de rechercher son nom dans le dossier *textures*.  
    ![Barre recherche](./images/grass.png)
* ### Résumé : 
    ![arbre](./images/schema.png)   

## Prérequis

* Paint3D ou tout autre logiciel de dessin de votre choix
* Pour ouvrir les .json : bloc-note ( installé par défaut sur Windows)
* Pour faire de la 3D Blockbench (gratuit), à télécharger [ici](https://www.blockbench.net/downloads), ou à utiliser en [ligne](https://web.blockbench.net/)

## Avant de commencer

* Installer le Template dans le dossier texture pack du jeu :
    - Appuyer sur <kbd>Windows</kbd> + <kbd>R</kbd> 
    - Entrer dans la fenetre qui viens de s'ouvrir :  %appdata%\.minecraft\resourcepacks
    ![Image](./images/appdata.png)
    - Télécharger le [template ](./template.zip) et dézipper le. On doit obtenr ceci :
    ![Illustation](./images/dossier.png) 
    

## Modifier une texture

On va prendre un exemple tout simple, le tronc de chene (oak log), le principe est le même pour toutes les autres textures.














[^1]: Désigne un variant d'un block

