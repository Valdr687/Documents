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


plt.figure()
plt.plot(Abscises, profil, 'r', label="Profil de l'aile")
plt.plot(Abscises, dérivé, 'g', label="Fonction dérivé")
plt.xlabel('Abscises')
plt.legend()
plt.ylim(-0.3, 0.3)
plt.xlim(0, 1)
plt.show()

# 2) Dichotomie


epsilon = 10**(-4)
IterationMax = 100

def dicho(fonctionDérivé, a: float, b: float, e: float, IterationMax: int) -> float:
    ai, bi, ci = a, b, (a+b)/2
    fa, fb, fc = fonctionDérivé(ai), fonctionDérivé(bi), fonctionDérivé(ci)
    ite = 0
    while bi-ai > 2*e and abs(fc) > e and ite < IterationMax:
        ite += 1
        ci = (ai+bi)/2
        fc = fonctionDérivé(ci)
        if fa*fc <= 0:
            bi, fb = ci, fc
        else:
            ai, fa = ci, fc
    return ci


print('Racine obtenue par dichotomie', dicho(
    fonctionDérivé, 0.2, 0.4, epsilon, IterationMax))

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
        print(xi)
        fx = fonctionProfil(xi)

print('Racine obtenue par méthode de Newton',xi)
