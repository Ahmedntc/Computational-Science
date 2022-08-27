import numpy as np 

altura = np.loadtxt('txt/altura.txt')
idade = np.loadtxt('txt/anos.txt')

idade = np.logical_and(idade >=1998, idade<=2005)
idade = np.nonzero(idade)

altura = np.take(altura, idade)

mediaH = np.average(altura)

print(mediaH)


