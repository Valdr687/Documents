# Fiche révision

## Contenu

- [Python](#python)
- [Méthode de résolutions analytique](#méthodes-de-résolutions-analytique)
  - [Méthode de Newton](#méthode-de-newton)
  - [Intégration numérique](#intégration-numérique)
- [Traitement de données](#traitements-de-données)
  - [Dichotomie](#dichotomie)
- [SQL](#sql)

---

## Python

### Lecture dans un fichier

## Méthodes de résolutions analytique

### Méthode de Newton

On cherche à résoudre le problème (dit de Cauchy) suivant :  
$y\prime = f(t,y(t))$  
$y(t_0)=y_0$ pour $t \in [t_{0} ; t_{max} ]$

On procède ainsi :  

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

### Intégration numérique

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
