import matplotlib.pyplot as plt
from random import randint

x = [4,9,21,55,30,18]
plt.figure(figsize=(5,5))
L = ['Chiens','Chats','Souris','Pies','Lapins','Vers']
plt.pie(x,labels=L,autopct='%.2f %%')
plt.show()
