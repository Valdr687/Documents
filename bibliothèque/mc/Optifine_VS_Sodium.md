# Optifine VS Sodium+Iris
 
Lorsque l'on recherche plus de fps dans Minecraft, de meilleurs effets graphiques, on se tourne par défaut vers Optifine, mais est-ce pour autant une bonne idée ?  
La seule réponse que je puisse donner pour le moment est ça dépend, de quoi, pourquoi, c'est ce qu'on va voir.
 
## Optifine
 
Optifine est un "mod qui ajoute le support des textures HD et un grand nombre d'options pour de meilleurs aspects graphiques et de meilleures  performances. Un doublement des FPS est commun." pour reprendre les mots du créateur.  
Un premier point qui apparaît est l'absence du terme "optimisation" car Optifine n'est pas un mod dédié à l'optimisation pure. Mais bien un mod qui permet l'ajout de nombreuses fonctionnalités visuelles.
Et une précision s'impose, le gain de fps lié à Optifine est dû majoritairement à la réduction du nombre de chunk, voyez cette [page](https://web.archive.org/web/20210131212246/https://gist.github.com/jellysquid3/e46882e37907dfbb3d03d26f589b1c6a) pour en savoir plus.
 
## Sodium + Iris
 
### Sodium
 
Sodium est un mod Fabric qui réécrit des parties du système de rendu vanilla pour optimiser les performances du jeu. Sodium est mis à jour régulièrement, et vise à être compatible avec la plupart des autres mods Fabric pour un maximum de FPS. Combiné avec Lithium et Phosphor le ticking et l'éclairage sont aussi optimisés.
 
### Iris
 
Iris vise la prise en charge des shaders avec Sodium, il permet ainsi d'utiliser des shaders avec de meilleures performances qu'en Vanilla.
 
# Quelle option choisir ?
 
Pour faire votre choix il faut déterminer ce que vous voulez :
- jouer dans une version antérieur à la 1.16 : Optifine
- jouer en Vanilla ?
- jouer avec un shader
- jouer avec un pack de texture
 
Enfin, si vous êtes, comme moi, créateur de pack de texture, je vous (nous ?) réserve un paragraphe.
 
## Avant la 1.16 :
 
Sodium n'est disponible que pour les versions depuis la 1.16 et ne sera pas rétro porté. Donc la question ne se pose pas.
 
## Vanilla 1.16+
 
Vous ne voulez que des fps ? Alors utilisez Sodium+Iris, l'installateur Iris (avec Sodium inclus) est fait pour vous, vous le trouverez à cette [adresse](https://modrinth.com/mod/iris).
 
## Avec shader **sans** texture pack
 
Là encore on utilise Sodium et Iris. Sachez juste que certains shaders on des problèmes de compatibilités avec Iris, tout comme d'autres en ont avec Optifine, essayez en plusieurs et vérifiez la comptabilité présente ou future auprès du développeur.
 
## Avec un texture pack  
 
Optifine propose une longue liste de fonctionnalité pour les packs de textures, fonctionnalités que Sodium ne propose pas. Et ces fonctionnalités sont néanmoins utilisées par de nombreux packs, tels que le [Aspack](https://www.planetminecraft.com/texture-pack/the-asphyxious-custompack-16x16/) ou le [Vervada](https://www.planetminecraft.com/texture-pack/the-vervada/), tous deux développés par la commu MC-FR.  
Mais êtes-vous pour autant condamnés à utiliser Optifine pour profiter des packs de textures ? Non, déjà parce que tout les packs n'utilisent pas les fonctionnalités d'Optifine, ensuite ce [modpack](https://www.curseforge.com/minecraft/modpacks/bettervanillabuilding-fabric-compatibility) contient des mods qui permettent d'émuler ces fonctionnalités. 
Pour autant il n'existe pas de mods permettant de recopier toutes les fonctionnalités en raison de la licence restrictive d'Optifine, mais les fonctionnalités non-couvertes par ces mods sont négligeable.  
Et je préfère vous prévenir, les mods qui font comme Optifine sans être compatible avec les formats Optifine sont une fausse bonne idée, vous croyez vraiment que lorsqu'on fait notre pack, on a que ça à faire ?
 
## Pour la création
 
Lorsqu'on développe son pack, on fait tout pour gagner du temps et une des fonctionnalités de Minecraft est F3+t qui permet de recharger son pack et de voir les modifications qu'on y a apporté. Et le problème est que certains mods ont des problèmes avec cette fonctionnalité.  
Donc développez sous Optifine, jouez sous Sodium.
 
# Encore plus de performance
 
Si vous avez un grille pain en guise d'ordinateur ou que vous souhaitez tout simplement embellir votre jeux sans perte de performace, sachez qu'il est possible de rajouter encore plus de mods d'optimisation, la liste est [ici](https://github.com/NordicGamerFE/usefulmods/blob/main/Performance/Performance119.md).

