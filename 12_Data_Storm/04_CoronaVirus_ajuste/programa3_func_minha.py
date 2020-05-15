from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
from matplotlib.widgets import Slider, Button, RadioButtons
#from matplotlib.ticker import MultipleLocator
import os
import sys


name = sys.argv #Nome do País colocado no Terminal

if len(name) == 2:
	name = name[1] # País com 1 nome. ex: Brazil
if len(name) == 3:
	name = "%s %s"%(name[1],name[2]) # País com dois nomes. ex: United Kingdom



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

def RMSE(y,y_pred):
	y = np.array(y)
	y_pred = np.array(y_pred[:len(y)])#Para pegar até os dados que temos de infectados
	return np.sqrt(sum(y-y_pred)**2/len(y))


arq = open('./dados/dados_%s.txt'%name,'r')
lines = arq.readlines()
arq.close()

x = [float(line.split(',')[0]) for line in lines[1:]]
y1 = [float(line.split(',')[1]) for line in lines[1:]]
y2 = [float(line.split(',')[2]) for line in lines[1:]]



a = 0.001

days = 365

X = np.arange(0,days)
Y = func(X,a,2000000,10)

#-------------GRAFICO--------------------
ax1=plt.subplot(121)
plt.subplots_adjust(left=0.1, bottom=0.3)
k, =plt.plot(x,y1,'or',linewidth=2,label="New_cases")
g1, =plt.plot(X,Y,'--b',linewidth=2)
g2, =plt.plot(X,Y,'--b',linewidth=2)
g, =plt.plot(X,Y,'-g',linewidth=3,label=r"Accumulated")

plt.title("%s - Covid-19 Cases - 31/12/19 to 12/05/20"%name)
plt.xlabel('day')
plt.ylabel("Confirmed Cases")

#plt.xlim(0,40)
plt.xticks(np.arange(0, days, step=30))
plt.legend()
plt.grid(True)

ax2=plt.subplot(122)
plt.subplots_adjust(left=0.1, bottom=0.3)
l, =plt.plot(x,y2,'or',linewidth=2,label="New_deaths")
d1, =plt.plot(X,Y,'--b',linewidth=2)
d2, =plt.plot(X,Y,'--b',linewidth=2)
d, =plt.plot(X,Y,'-g',linewidth=3,label=r"Accumulated")

plt.title("%s - Covid-19 Deaths - 31/12/19 to 12/05/20"%name)
plt.xlabel('day')
plt.ylabel("Deaths")

#plt.xlim(0,40)
plt.xticks(np.arange(0, days, step=30))
plt.legend()
plt.grid(True)


#Textos
infectados = plt.text(0.05, 0.95, "total_infected (predict) = %.2f"%(sum(y1)), fontsize=12, transform=plt.gcf().transFigure)
infectados_RMSE = plt.text(0.05, 0.93, "RMSE_inf = %.2f"%(0), fontsize=12, transform=plt.gcf().transFigure)

mortes = plt.text(0.60, 0.95, "total_deaths (predict) = %.2f"%(sum(y2)), fontsize=12, transform=plt.gcf().transFigure) 
mortes_RMSE = plt.text(0.60, 0.93, "RMSE_dea = %.2f"%(0), fontsize=12, transform=plt.gcf().transFigure)

func_text = plt.text(0.35, 0.95, r"$I = e^{a.x}$,$pos=\frac{pop}{infected}$, f(x)=$A*I*e^{-\frac{1}{pos}}$", fontsize=10, transform=plt.gcf().transFigure)


#---------------------------------------barra interativa----------------------------------------------
axcolor=(0.5,0.7,0.7)


#Func nova
ai = 1e-6
af = 1
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
A3bar= Slider(A3_, "A3", Ai/4, Af/4, valinit=Af/2)

a4_ = plt.axes([0.60, 0.11, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a4bar= Slider(a4_, 'a4', ai, af, valinit=a, valfmt='%.2e')

A4_ = plt.axes([0.60, 0.08, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
A4bar= Slider(A4_, "A4", Ai/4, Af/4, valinit=Af/2)


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

	#Error
	RMSE_inf = RMSE(y1,G)
	RMSE_dea = RMSE(y2,D)
	
	g1.set_ydata(G1)
	g2.set_ydata(G2)
	g.set_ydata(G)

	d1.set_ydata(D1)
	d2.set_ydata(D2)
	d.set_ydata(D)
	

	#Texto Predict
	infectados.set_text("total_infected (predict) = %.2f"%sum(G))
	mortes.set_text("total_deaths (predict) = %.2f"%sum(D))

	#Texto Error
	infectados_RMSE.set_text("RMSE_dea = %.2f"%(RMSE_inf))
	mortes_RMSE.set_text("RMSE_dea = %.2f"%(RMSE_dea))

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
