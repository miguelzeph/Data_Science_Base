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


def gauss(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

arq = open('./dados/dados_%s.txt'%(name),'r')
lines = arq.readlines()
arq.close()

x = [float(line.split(',')[0]) for line in lines[1:]]
y1 = [float(line.split(',')[1]) for line in lines[1:]]
y2 = [float(line.split(',')[2]) for line in lines[1:]]

#plt.plot(x,y,'o')

a = 100
xo = 200
sigma = 10


days = 365

X = np.arange(0,days)
Y = gauss(X,a,xo,sigma)

#plt.plot(X,Y)

#plt.show()

#------------------------GRAFICO--------------------
ax1=plt.subplot(121)
plt.subplots_adjust(left=0.1, bottom=0.3)
k, =plt.plot(x,y1,'or',linewidth=2,label="New_cases")
g1, =plt.plot(X,Y,'--b',linewidth=2)
g2, =plt.plot(X,Y,'--b',linewidth=2)
g, =plt.plot(X,Y,'-g',linewidth=3,label="Accumulated")

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
d, =plt.plot(X,Y,'-g',linewidth=3,label="Accumulated")

plt.title("%s - Covid-19 Deaths - 31/12/19 to 12/05/20"%name)
plt.xlabel('day')
plt.ylabel("Deaths")

#plt.xlim(0,40)
plt.xticks(np.arange(0, days, step=30))
plt.legend()
plt.grid(True)






#---------------------------------------barra interativa----------------------------------------------
axcolor=(0.5,0.7,0.7)

ai = 0.01
af = 1e5

xoi = 0
xof = 500

sigmai = 0.01
sigmaf = 100


# Barras Casos
a1_ = plt.axes([0.15, 0.20, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a1bar= Slider(a1_, 'a1', ai, af, valinit=a, valfmt='%.2e')

xo1_ = plt.axes([0.15, 0.17, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
xo1bar= Slider(xo1_, "Xo1", xoi, xof, valinit=xo)

sigma1_ = plt.axes([0.15, 0.14, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
sigma1bar= Slider(sigma1_, "sigma1", sigmai, sigmaf, valinit=sigma)


a2_ = plt.axes([0.15, 0.11, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a2bar= Slider(a2_, 'a2', ai, af, valinit=a, valfmt='%.2e')

xo2_ = plt.axes([0.15, 0.08, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
xo2bar= Slider(xo2_, "Xo2", xoi, xof, valinit=xo)

sigma2_ = plt.axes([0.15, 0.05, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
sigma2bar= Slider(sigma2_, "sigma2", sigmai, sigmaf, valinit=sigma)

# Barras Mortes
a3_ = plt.axes([0.60, 0.20, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a3bar= Slider(a3_, 'a3', ai, af/10, valinit=a, valfmt='%.2e')

xo3_ = plt.axes([0.60, 0.17, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
xo3bar= Slider(xo3_, "Xo3", xoi, xof, valinit=xo)

sigma3_ = plt.axes([0.60, 0.14, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
sigma3bar= Slider(sigma3_, "sigma3", sigmai, sigmaf, valinit=sigma)


a4_ = plt.axes([0.60, 0.11, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a4bar= Slider(a4_, 'a4', ai, af/10, valinit=a, valfmt='%.2e')

xo4_ = plt.axes([0.60, 0.08, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
xo4bar= Slider(xo4_, "Xo4", xoi, xof, valinit=xo)

sigma4_ = plt.axes([0.60, 0.05, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
sigma4bar= Slider(sigma4_, "sigma4", sigmai, sigmaf, valinit=sigma)


#Textos
infectados = plt.text(0.05, 0.95, "total_infected (predict) = %.2f"%(sum(y1)), fontsize=12, transform=plt.gcf().transFigure)
mortes = plt.text(0.60, 0.95, "total_deaths (predict) = %.2f"%(sum(y2)), fontsize=12, transform=plt.gcf().transFigure) 
func_text = plt.text(0.35, 0.95, "function: Gauss", fontsize=10, transform=plt.gcf().transFigure)


def update(val):#este val nao tem nada a ver com ...

	#atualizar o valor
	
	a1 = a1bar.val
	xo1 = xo1bar.val
	sigma1 = sigma1bar.val

	a2 = a2bar.val
	xo2 = xo2bar.val
	sigma2 = sigma2bar.val

	a3 = a3bar.val
	xo3 = xo3bar.val
	sigma3 = sigma3bar.val

	a4 = a4bar.val
	xo4 = xo4bar.val
	sigma4 = sigma4bar.val
	
	
	G1 = []
	G2 = []
	G = []

	D1 = []
	D2 = []
	D = []


	for x in np.arange(0,days):

		gauss1 = gauss(x,a1,xo1,sigma1) 
		G1.append(float(gauss1))
		gauss2 = gauss(x,a2,xo2,sigma2) 
		G2.append(float(gauss2))
		G.append(gauss1+gauss2)

		gauss3 = gauss(x,a3,xo3,sigma3) 
		D1.append(float(gauss3))
		gauss4 = gauss(x,a4,xo4,sigma4) 
		D2.append(float(gauss4))
		D.append(gauss3+gauss4)
	
	g1.set_ydata(G1)
	g2.set_ydata(G2)
	g.set_ydata(G)

	d1.set_ydata(D1)
	d2.set_ydata(D2)
	d.set_ydata(D)


	#Texto
	infectados.set_text("total_infected (predict) = %.2f"%sum(G))
	mortes.set_text("total_deaths (predict) = %.2f"%sum(D))

	#Alterar Gráfico
	plt.draw()

a1bar.on_changed(update)
xo1bar.on_changed(update)
sigma1bar.on_changed(update)

a2bar.on_changed(update)
xo2bar.on_changed(update)
sigma2bar.on_changed(update)

a3bar.on_changed(update)
xo3bar.on_changed(update)
sigma3bar.on_changed(update)

a4bar.on_changed(update)
xo4bar.on_changed(update)
sigma4bar.on_changed(update)

plt.show()

