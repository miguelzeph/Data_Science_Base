from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
from matplotlib.widgets import Slider, Button, RadioButtons
#from matplotlib.ticker import MultipleLocator
import os

def func(x,a,pop,A):
	"""
	x: dias
	a: constante de consentimento
	pop: população do país
	A: Normalizar
	"""
	infectados = np.exp(+x*a)
	possibilidade = pop/infectados**2
	novos_casos = A*infectados*np.exp(-1/possibilidade)
	return novos_casos


arq = open('./dados.txt','r')
lines = arq.readlines()
arq.close()

x = [float(line.split(',')[0]) for line in lines[1:]]
y1 = [float(line.split(',')[1]) for line in lines[1:]]
y2 = [float(line.split(',')[2]) for line in lines[1:]]

#plt.plot(x,y,'o')

a = 100




days = 365

X = np.arange(0,days)
Y = func(X,a,2000000,10)

#plt.plot(X,Y)

#plt.show()

#------------------------GRAFICO--------------------
ax1=plt.subplot(121)
plt.subplots_adjust(left=0.1, bottom=0.3)
k, =plt.plot(x,y1,'or',linewidth=2,label="New_cases")
g1, =plt.plot(X,Y,'--b',linewidth=2)
g2, =plt.plot(X,Y,'--b',linewidth=2)
g, =plt.plot(X,Y,'-g',linewidth=3,label="Accumulated")

plt.title("Cases of Covid-19 in 2020")
plt.xlabel('day')
plt.ylabel("Cases Confirmed")

#plt.xlim(0,40)
plt.xticks(np.arange(0, days, step=30))
plt.legend()
plt.grid(True)

ax2=plt.subplot(122)
plt.subplots_adjust(left=0.1, bottom=0.3)
l, =plt.plot(x,y2,'or',linewidth=2,label="New_deaths")
d1, =plt.plot(X,Y,'--b',linewidth=2)
d2, =plt.plot(X,Y,'--b',linewidth=2)
d, =plt.plot(X,Y,'-g',linewidth=3,label="Accumulated")

plt.title("Deaths of Covid-19 in 2020")
plt.xlabel('day')
plt.ylabel("Deaths")

#plt.xlim(0,40)
plt.xticks(np.arange(0, days, step=30))
plt.legend()
plt.grid(True)


#Menor RL
infectados = plt.text(0.05, 0.95, "total_infectadas = %.2f"%(sum(y1)), fontsize=10, transform=plt.gcf().transFigure)
mortes = plt.text(0.60, 0.95, "total_mortes = %.2f"%(sum(y2)), fontsize=10, transform=plt.gcf().transFigure) 


#---------------------------------------barra interativa----------------------------------------------
axcolor=(0.5,0.7,0.7)


#Func nova
ai = 1e-6
af = 1e-1
Ai = 1e-2
Af = 100

# Barras Casos
a1_ = plt.axes([0.15, 0.20, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a1bar= Slider(a1_, 'a1', ai, af, valinit=a, valfmt='%.2e')# gaussiana

A1_ = plt.axes([0.15, 0.17, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
A1bar= Slider(A1_, "A1", Ai, Af, valinit=Af/2)


a2_ = plt.axes([0.15, 0.11, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a2bar= Slider(a2_, 'a2', ai, af, valinit=a, valfmt='%.2e')

A2_ = plt.axes([0.15, 0.08, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
A2bar= Slider(A2_, "A2", Ai, Af, valinit=Af/2)


# Barras Mortes
a3_ = plt.axes([0.60, 0.20, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a3bar= Slider(a3_, 'a3', ai, af, valinit=a, valfmt='%.2e')

A3_ = plt.axes([0.60, 0.17, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
A3bar= Slider(A3_, "A3", Ai, Af, valinit=Af/2)

a4_ = plt.axes([0.60, 0.11, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a4bar= Slider(a4_, 'a4', ai, af, valinit=a, valfmt='%.2e')

A4_ = plt.axes([0.60, 0.08, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
A4bar= Slider(A4_, "A4", Ai, Af, valinit=Af/2)


def update(val):#este val nao tem nada a ver com ...

	#atualizar o valor
	
	a1 = a1bar.val
	A1 = A1bar.val
	

	a2 = a2bar.val
	A2 = A2bar.val
	
	a3 = a3bar.val
	A3 = A3bar.val
	

	a4 = a4bar.val
	A4 = A4bar.val
	
	
	
	G1 = []
	G2 = []
	G = []

	D1 = []
	D2 = []
	D = []


	A1 = A1bar.val

	for x in np.arange(0,days):

		f1 = func(x,a1,200000000,A1)#Função nova		
		G1.append(float(f1))
		f2 = func(x,a2,200000000,A2)#Função nova 
		G2.append(float(f2))
		G.append(f1+f2)

		f3 = func(x,a3,200000000,A3)#Função nova
		D1.append(float(f3))
		f4 = func(x,a4,200000000,A4)#Função nova
		D2.append(float(f4))
 		D.append(f3+f4)
	
	g1.set_ydata(G1)
	g2.set_ydata(G2)
	g.set_ydata(G)

	d1.set_ydata(D1)
	d2.set_ydata(D2)
	d.set_ydata(D)

	infectados.set_text("total_pessoas_infectadas = %.2f"%sum(G))
	mortes.set_text("total_pessoas_mortas = %.2f"%sum(D))

	#Alterar Gráfico
	plt.draw()



a1bar.on_changed(update)
A1bar.on_changed(update)

a2bar.on_changed(update)
A2bar.on_changed(update)

a3bar.on_changed(update)
A3bar.on_changed(update)

a4bar.on_changed(update)
A4bar.on_changed(update)


plt.show()
