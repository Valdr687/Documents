import matplotlib.pyplot as plt
import random as rd

y = [rd.randint(1,100) for i in range(1,201) ]
x = [rd.randint(1,100) for i in range(1,201) ]

plt.figure()
plt.scatter(x,y,s=100)
plt.show()