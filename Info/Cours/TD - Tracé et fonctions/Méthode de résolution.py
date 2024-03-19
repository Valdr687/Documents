import matplotlib.pyplot as plt
from math import *
from numpy import linspace

# Fonctions -------------
def fonctionProfil(x):
    return 0.15*(3.7*sqrt(x)-3.4*x-0.3*(x**4))

def fonctionDérivé(x):
    return 0.15*((3.7/(2*sqrt(x)))-3.4-1.2*(x**3))

# Abscises & fonctions -----------
Abscises = linspace(0, 1, 10000)
Abscises = Abscises[1:len(Abscises)]

profil=[]
dérivé=[]

for x in Abscises:
    profil.append(fonctionProfil(x))
    dérivé.append(fonctionDérivé(x))


figure, axis = plt.subplots(1, 2) 
  
axis[0].plot(Abscises, profil) 
axis[0].set_title("Profil de l'aile") 
  
axis[1].plot(Abscises, dérivé) 
axis[1].set_title("fonction f(x)") 
  
plt.show()

# 2) Dichotomie

a = 0.2
b = 0.5
epsilon = 10**(-4)
IterationMax = 1000
ai,bi,racine= a,b,(a+b)/2
fa, fb, fc = fonctionProfil(ai), fonctionProfil(bi), fonctionProfil(racine)

Iteration = 0
while  bi-ai > 2*epsilon and abs(fc) > epsilon and Iteration < IterationMax : 
    Iteration += 1
    racine = (ai+bi)/2 
    fc = fonctionProfil(racine)
    if  fa*fc <= 0 :
        bi = racine
        fb = fc
    else :
        ai = racine 
        fa = fc

print('Racine obtenue par dichotomie',racine)

# 3) Méthode de Newton

x0= 0.1

Iteration = 0
xi = x0
fx = fonctionProfil(xi)
while abs(fx) > epsilon and Iteration < IterationMax :
    Iteration = Iteration + 1
    fpx = fonctionDérivé(xi) 
    if fpx == 0 :
        break
    else : 
        xi = xi - fx/fpx
        fx = fonctionProfil(xi)

print('Racine obtenue par méthode de Newton',xi)
