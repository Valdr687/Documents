test=[0,1,2,3,4,5,6,7,8,9,10,12,14,15,16,17,18,19]
def dichotomie(tab,n):
    a = 0
    b = len(tab) - 1
    while a <= b:
        m = (a + b) // 2
        if tab[m] == n:
            # on a trouvé n
            return True
        elif tab[m] < n:
            a = m + 1
        else:
            b = m - 1
    # on a a > b
    return False

def dicho(tab,n):
    a=0
    b=len(tab)-1