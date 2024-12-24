def lagrange(listex, listey, x):
    Valeur = 0

    for RangY in range(len(listey)):

        TermeItération = listey[RangY]

        for RangX in range(len(listex)):
            if RangX != RangY:
                TermeItération *= (x - listex[RangX]) / \
                    (listex[RangY] - listex[RangX])

        Valeur += TermeItération

    return Valeur
