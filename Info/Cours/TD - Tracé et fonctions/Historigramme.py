import matplotlib.pyplot as plt
from random import randint

y = [randint(1, 100) for i in range(1, 201)]

plt.figure()
plt.title("Histogramme")
plt.subplot(211)
plt.hist(y,10,color='r')
plt.subplot(212)
plt.hist(y,50,color=[0.2,0.1,0.8])
plt.show()

