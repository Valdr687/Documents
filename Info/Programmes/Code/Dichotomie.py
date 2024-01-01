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
