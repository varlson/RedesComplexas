from graphBuilder import *
from random import randint as rand

def gera():
	return [rand(0,10) for i in range(0,4)]


all = []
cor = ['Blue', "Black", "Red"]
for i in range(3):
	aux = plt.plot(gera(), marker="*", color=cor[i], label=cor[i, ["ttttt"]])
	all.append(aux)

plt.legend()
plt.show()