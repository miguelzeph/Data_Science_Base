from __future__ import division
import matplotlib.pyplot as plt
import numpy as np



x = np.arange(0,365,1)
infectados = x*np.exp(+x*0.04)
populacao = 200000000# Todo País
possibilidade = populacao/infectados
novos_casos = infectados*np.exp(-x/possibilidade)


plt.plot(x,novos_casos,'-b')
plt.show()
