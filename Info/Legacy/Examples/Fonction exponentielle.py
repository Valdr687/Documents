import matplotlib.pyplot as plt
from math import exp

#Déclarartion des variables 
x=[] #Absices
y=[] #exp(x)

NombreDépart=""
NombreArrive=""
pas=""

#Entrée du nombre de départ et d'arrivée

run= True
while run:
    NombreDépart = input('Nombre initial : ')
    try:
        NombreDépart = int(NombreDépart)
        run = False
    except ValueError:
            try:
                NombreDépart = float(NombreDépart)
                run = False
            except ValueError:
                print("Merci d'entrer un nombre.")

run= True
while run:
    NombreArrive = input('Nombre final : ')
    try:
        NombreArrive = int(NombreArrive)
        if NombreArrive>NombreDépart :
            run=False
    except ValueError:
            try:
                NombreArrive = float(NombreArrive)
                if NombreArrive>NombreDépart :
                    run=False
            except ValueError:
                print("Merci d'entrer un nombre.")
    
run= True
while run:
    pas = input('Distance entre les points : ')
    try:
        pas = int(pas)
        run = False
    except ValueError:
            try:
                pas = float(pas)
                run = False
            except ValueError:
                print("Merci d'entrer un nombre.")


#Remplissage des tableaux

n=NombreDépart
while n<NombreArrive :
    n+=pas
    x.append(n)

for i in x :
    y.append(exp(i))

#Affichage
plt.title('Courbe représentative de la fonction exponentielle', color="blue")     # Titre
plt.xlabel('x')                 # Légende abscisse
plt.ylabel('exp(x)')                 # Légende ordonnée
plt.plot(x, y, color="red")
plt.grid()                      # Ajout d'une grille
plt.show()                      # Affichage

