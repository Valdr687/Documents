# Fiche révision

## Contenu

- [Python](#python)
- [Méthode de résolutions analytique](#méthodes-de-résolutions-analytique)
  - [Recherche de 0](#recherche-de-0---dichotomie)
  - [Résolution d'équation différentielle](#résolution-déquation-différentielle)
  - [Intégration numérique](#intégration-numérique)
- [Traitement de données](#traitements-de-données)
  - [Dichotomie](#dichotomie)
- [SQL](#sql)

---

## Python

### Lecture dans un fichier

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
    return ci
```

### Recherche de 0 - Newton

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

### Manipulations sur les listes

## SQL

[^1]: Loves U$
