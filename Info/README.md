# Mémo info PTSI/PT

## Cours

1. [Binaire](./Cours/Binaire.md)
1. [Récursivité](./Cours/Complexité.md)
1. [Complexité](./Cours/Complexité.md)

## Table des matières

- [Python](#python)
  - [Lecture dans un fichier](./Cours/fichier.md)
  - [Tracé de courbes](#tracé-de-courbes)
- [Méthode de résolutions analytique](#méthodes-de-résolutions-analytique)
  - [Recherche de 0](#recherche-de-0---dichotomie) *Newton*
  - [Résolution d'équation différentielle](#résolution-déquation-différentielle)
  - [Intégration numérique](#intégration-numérique)
- [Traitement de données](#traitements-de-données)
  - [Dichotomie](#dichotomie)
  - [Tris](#tris)
  - [Manipulation sur les listes](#manipulations-sur-les-listes) *TBD*
- [SQL](#sql)

---

## Python

### Tracé de courbes

On utilise le module ``pyplot`` de ``matplotlib`` avec deux listes ayant la même dimension, l'une représente les ordonnées et l'autres et les abscises.

```python
import numpy as np
import matplotlib.pyplot as plt
plt.figure() # pour une nouvelle figure
x = np.array([1, 3, 4, 6]) # les abscisses des 4 points
y = np.array([2, 3, 5, 1]) # les ordonnées
plt.plot(x, y)
plt.show() # affiche la figure a l’écran, nécessaire pour avoir un affichage
plt.close() #trop de figures ouvertes peuvent créer une surcharge de la mémoire
```

Pour plus d'information, voyez [ce document](./Cours/Tracés.md).

## Méthodes de résolutions analytique

### Recherche de 0 - Dichotomie

Entrées : fonction f, a et b (l'intervalle de recherche est [a,b]), ε (marge de précision), IteMax (Nombre max d'itération)  
Sortie : racine approchée de 0 notée c

```python
from math import abs 

def f(x)
    return x #expression de f

def dichotomie(f,a,b,ε,IteMax):
    ai,bi,ci=a,b,(a+b)/2
    fa,fb,fc=f(ai),f(bi),f(ci)
    ite = 0
    while bi-ai > 2 and abs(fc)>ε and ite<IteMax :
        ci = (ai+bi)/2
        fc=f(ci)

        if fa*fc <= 0 : # la racine est dans [ai,ci]
            bi = ci # on actualise l'intervalle de recherche
            fb = fc
        else : # la racine est dans [ci,bi]
            ai = ci
            fa = fc
        ite=ite+1
    return ci
```

### Recherche de 0 - Newton

Cette méthode utilise le développement de Taylor à l’ordre 1. Si la fonction est de classe $\mathcal{C}^1$ sur l’intervalle $[a,b]$, alors le
développement de Taylor d’ordre 1 donne :  

$f(b)=f(a)+f\prime(a)\times(b-a) + o(b-a)$.  

A partir d’un point choisi x0, la méthode consiste à rechercher le point suivant x1 en le supposant racine de la fonction $f$ et en négligeant le terme $o(x1-x0)$ dans le développement de Taylor. Si bien que :  

$0 = f(x_1) = f(x_0) + f\prime(x_0)\times(x_1-x_0) \implies x_1 = x_0 - \frac{f(x_0)}{f\prime(x_0)}$.

Si $f(x_1)$ ne vérifie pas le critère de convergence $|f(x_1)| < \epsilon$, alors un nouveau candidat $x_2$ est calculé à partir de $x_1$ et ainsi de suite
jusqu’à convergence.

Entrées : fonction f, fonction $f\prime$, $x_0$ (début de la recherche), $\epsilon$ (marge de précision), IteMax (Nombre max d'itération)  
Sortie : racine approchée de 0

```python
from math import abs

def f(x)
    return x #expression de f

def df(x):
    return x #expression de f'

def newton(f,df,x0,ε,IteMax):
    ite=0
    xi=x0
    fx=f(xi)
    while abs(fx)>ε and ite < IteMax:
        ite +=1
        fpx=df(xi)
        if fpx=0: # on sort de la boucle si la dérivée est nulle
            break
        else:
            xi = xi - fx/fpx # on actualise le candidat
            fx=f(xi)
    return xi
```

---

### Résolution d'équation différentielle

On cherche à résoudre le problème (dit de Cauchy) suivant :  
$y\prime = f(t,y(t))$  
$y(t_0)=y_0$ pour $t \in [t_{0} ; t_{max} ]$

On procède ainsi (grace à la méthode d'Euler [^1]) :  

- Calcul du pas :  
$h=\frac{t_{m a x} \times t_0}{n}$ où n représente le nombre de points
- Passage de l'équation différentielle à une relation de récurrence :  
$a\frac{d y}{d t}+b y(t)=x(t) \leftrightarrow \frac{d y(t)}{d t}=\frac{x(t)-b_y(t)}{a}$  
d'où $f(y, t)=\frac{x(t)-by(t)}{a}$
et la relation de récurrence : $y_{k+1}=y_k+h f(t_k, y_k)$

Programme :  

```python
def euler(y0,T0,Tmax,h,f(t,y)):
    t=T0
    y=y0
    ListeY = [y]
    while t<Tmax:
        y = y + h*f(t,y)
        t = t + h
        ListeY.append(y)
    return ListeY
```

---

### Intégration numérique

#### Méthode des rectangles

Dans cette méthode, la fonction à intégrer est interpolée par un polynôme de degré 0, à savoir une fonction constante. Géométriquement, l'aire sous la courbe est alors approximée par un rectangle.  

Le théorème de Riemann dit que si f est continue (par morceaux) sur un segment [a; b], alors on peut approcher I'aire située sous le graphe de f par la somme des aires des rectangles approchant f en n points uniformément répartis. f est intégrable sur [a; b], si et seulement si pour toute subdivision $\sigma_k = (\sigma_0 < \sigma_1 <...< \sigma_n)$ les sommes ci-dessous convergent:

$\sum_{k=1}^{n-1}\left(\sigma_{k+1}-\sigma_k\right) f\left(t_k\right) \xrightarrow[n \rightarrow \infty]{\forall t_t \in\left[\sigma_k, \sigma_{t+1}\right]} I=\int_a^b f(t) d t$

Avec l'expression de $\sigma$ :  
$\sigma_k=a+k \times \frac{b-a}{n} , 0 \le k \le n -1 $

On peut donc insérer le point des rectangles à gauche, au milieu ou à droite :  
|Gauche|Milieu|Droite|
|-|-|-|
|$R_n=\frac{b-a}{n} \sum_{k=0}^{n-1} f\left(\sigma_{k}\right)$|$R_n=\frac{b-a}{n} \sum_{k=0}^{n-1} f\left({\sigma_{k+1} + \sigma_{k}} \over {2}\right)$|$R_n=\frac{b-a}{n} \sum_{k=0}^{n-1} f\left(\sigma_{k+1}\right)$|

```python
def f(x):
    return x # Expression de f - à modifier à chaque fois

# Méthode avec insertion à gauche, il suffit de changer l'expression dans comme dans le tableau ci dessus pour les autres

a = int(input("Entrer le nombre de départ de la courbe"))
b = int(input("Entrer le nombre d'arrivée de la courbe"))
n = int(input("Entrer le nombre de subdivisions"))

def AireSousLaCourbe(a,b,n,f) :
    S = 0
    for k in range(0,n):
        sigma = a + k * ((b-a)/float(n))
        S = S + ((b-a)/float(n)) * f(sigma)
    return S
```

#### Méthode des trapèzes

Le principe est similaire mais on utilise des trapèzes. On somme donc les $T_n$ tels que :

$T_n=\frac{b-a}{2n} \sum_{k=0}^{n-1}\left(f(\sigma_k) + f(\sigma_{k+1}) \right)$

```python
def f(x):
    return x # Expression de f - à modifier à chaque fois

# Méthode avec insertion à gauche, il suffit de changer l'expression dans comme dans le tableau ci dessus pour les autres

a = int(input("Entrer le nombre de départ de la courbe"))
b = int(input("Entrer le nombre d'arrivée de la courbe"))
n = int(input("Entrer le nombre de subdivisions"))

def AireSousLaCourbe(a,b,n,f) :
    S = 0
    for k in range(0,n):
        sigma = a + k * ((b-a)/float(n))
        sigma1 = a + (k+1) * ((b-a)/float(n))
        S = S + ((b-a)/float(2*n)) * (f(sigma) + f(sigma1))
    return S
```

## Traitements de données

### Dichotomie

Entrée : liste triée par ordre croissant ; élément à chercher  
Sortie : rang de l'élément cherché

```python
def dicho(liste, x):
    i_min = 0
    i_max = len(liste) - 1

    while i_max >= i_min:
        milieu = (i_max + i_min)//2  # calcul de l'indice "du milieu"

        if liste[milieu] == x:      # x est présent dans la liste
            return milieu
        else:
            if liste[milieu] > x:  # alors x est dans la première moitié de la liste
                i_max = milieu - 1
            else:                   # x est donc dans la deuxième moitié
                i_min = milieu + 1

    return False  # si on en est là, x n'est pas présent dans la liste
```

### Tris

On l'a vu, la dichotomie ne fonctionne qu'avec des listes triées, d'où l'intérêt des tris.

#### Tri à bulles

Le tableau `nombres` est modifié par la fonction ; on parle donc de **tri en place**.

```python
def tri_bulle(nombres : list) -> list:
    n = len(nombres)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if nombres[j] > nombres[j+1]:
                # nombres[j] et nombre[j + 1] à échanger
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
    return nombres
```

#### Tri rapide

```python
def tri_rapide(tab):
    if tab == []:
        return []
    else:
        pivot = tab[0]
    t1, t2 = [], []
    for x in tab[1:]:
        if x < pivot:
            t1.append(x)
        else:
            t2.append(x)
    return tri_rapide(t1) + [pivot] + tri_rapide(t2)
```

On rappelle les complexités temporelles des algorithmes suivants en fonction de n : la taille du tableau à trier

- tri par sélection : **$O(n^2)$**
- tri à bulles : **$O(n^2)$**
- tri fusion : **$O(n*log(n))$**
- tri rapide : **$O(n*log(n))$**

Vous pouvez visualiser leur fonctionnement grace à ce [site](https://interstices.info/les-algorithmes-de-tri/).

### Manipulations sur les listes

## SQL

|Commande||
|-|-|
|SELECT *colonne*,*colonne2*| Précise les colonnes qui vont apparaitre dans la requête (* permet de tout sélectionner)|
|FROM *table*|Précise la table dont on sélectionne les donnés|
|WHERE|Précise les [conditions](#conditions) à appliquer sur les lignes|
|JOIN *table2* ON *table1*.*colonne_de_table1* = *table2*.*colonne_de_table2* |JOIN est utilisée pour combiner les lignes de deux ou plusieurs tables, en fonction d'une colonne liée entre elles.|
|ORDER BY *tri*|Tri croissant *ASC* ou décroissant *DESC* |
| HAVING | Applique des conditions sur les groupes de résultats.|
| MIN(*colonne*) | Renvoie la plus petite valeur de la colonne spécifiée.|
| MAX(*colonne*) | Renvoie la plus grande valeur de la colonne spécifiée.|
| SUM(*colonne*)  | Renvoie la somme des valeurs de la colonne spécifiée.|
| COUNT(*colonne*) | Renvoie le nombre de valeurs dans la colonne. `COUNT(DISTINCT colonne)` élimine les doublons.         |
| COUNT(*)  | Compte toutes les lignes de la table.|
| AVG(*colonne*)       | Renvoie la moyenne des valeurs de la colonne spécifiée.|

### Modification

|Commande||
|-|-|
| CREATE    | Crée une nouvelle table.|
| ALTER     | Modifie une table existante.|
| DROP      | Supprime une table.|
| INSERT    | Insère des lignes dans une table.|
| UPDATE    | Met à jour des lignes dans une table.|
| DELETE    | Supprime des lignes dans une table.|

### Conditions

**Comparaisons:**
=,>,<,>=,<=,!= : comme en Python sauf que l'égalité est testée avec *un simple* égal

**Opérateurs logiques**  
AND, NOT, OR

**Les prédicats**  
IN, NOT IN, LIKE, NULL, ALL, SOME, ANY, EXIST
  
[^1]: Loves U
