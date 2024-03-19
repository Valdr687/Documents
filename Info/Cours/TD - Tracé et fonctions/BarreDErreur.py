import matplotlib.pyplot as plt
import random as rd
import math as m 

x = []
y = []
e = []

for i in range(10):
    x.append(i)
    y.append(1-m.exp(-x[i]))
    e.append(0.1*rd.random())

plt.figure()
plt.axis([0,10,0,1.1])
plt.errorbar(x,y,yerr=e,fmt='go',ecolor='r')
plt.show()