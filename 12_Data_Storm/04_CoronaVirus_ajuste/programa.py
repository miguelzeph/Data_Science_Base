from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
from matplotlib.widgets import Slider, Button, RadioButtons
#from matplotlib.ticker import MultipleLocator
import os



def gauss(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

arq = open('./dados.txt','r')
lines = arq.readlines()
arq.close()

x = [float(line.split(',')[0]) for line in lines[1:]]
y = [float(line.split(',')[1]) for line in lines[1:]]

#plt.plot(x,y,'o')

a = 10000
xo = 200
sigma = 10

X = np.arange(0,200)
Y = gauss(X,a,xo,sigma)

#plt.plot(X,Y)

#plt.show()

#------------------------GRAFICO 1 - Reflection Loss (RL)-----------------------
ax1=plt.subplot(111)
plt.subplots_adjust(left=0.1, bottom=0.3)
k, =plt.plot(x,y,'or',linewidth=2,label="New_cases")
g1, =plt.plot(X,Y,'--b',linewidth=2)
g2, =plt.plot(X,Y,'--b',linewidth=2)
g, =plt.plot(X,Y,'-g',linewidth=3,label="Accumulated")

plt.title("Cases of Covid-19 in 2020")
plt.xlabel('day')
plt.ylabel("Cases Confirmed")


#plt.xlim(0,40)
plt.xticks(np.arange(0, 200, step=20))


plt.legend()
plt.grid(True)





#---------------------------------------barra interativa----------------------------------------------
axcolor=(0.5,0.7,0.7)

ai = 1e-6
af = 1e5

xoi = 0
xof = 500

sigmai = 0.01
sigmaf = 100


a1_ = plt.axes([0.15, 0.13, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a1bar= Slider(a1_, 'a1', ai, af, valinit=a, valfmt='%.2e')

xo1_ = plt.axes([0.15, 0.10, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
xo1bar= Slider(xo1_, "Xo1", xoi, xof, valinit=xo)

sigma1_ = plt.axes([0.15, 0.07, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
sigma1bar= Slider(sigma1_, "sigma1", sigmai, sigmaf, valinit=sigma)


a2_ = plt.axes([0.60, 0.13, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
a2bar= Slider(a2_, 'a2', ai, af, valinit=a, valfmt='%.2e')

xo2_ = plt.axes([0.60, 0.10, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
xo2bar= Slider(xo2_, "Xo2", xoi, xof, valinit=xo)

sigma2_ = plt.axes([0.60, 0.07, 0.20, 0.03], facecolor=axcolor) #(pos(x da barra),pos(y da barra),comprimento,largura)
sigma2bar= Slider(sigma2_, "sigma2", sigmai, sigmaf, valinit=sigma)

#-------------------------------------------------------------------------------------------------------

"""
# ---------Barra Resete-----------------------------------------------
resetax = plt.axes([0.8, 0.15, 0.1, 0.04])
buttonreset = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
#---------------------------------------------------------------------
savex = plt.axes([0.5, 0.15, 0.1, 0.04])
buttonsave = Button(savex, 'Save', color=axcolor, hovercolor='0.975')

"""

def update(val):#este val nao tem nada a ver com ...

	#atualizar o valor
	
	a1 = a1bar.val
	xo1 = xo1bar.val
	sigma1 = sigma1bar.val

	a2 = a2bar.val
	xo2 = xo2bar.val
	sigma2 = sigma2bar.val
	
	#global e
	
	G1 = []
	G2 = []
	G = []

	for x in np.arange(0,200):

		gauss1 = gauss(x,a1,xo1,sigma1) 
		G1.append(float(gauss1))

		gauss2 = gauss(x,a2,xo2,sigma2) 
		G2.append(gauss2)
 
		G.append(gauss1+gauss2)
	
	g1.set_ydata(G1)
	g2.set_ydata(G2)
	g.set_ydata(G)
	
	#Alterar Gráfico
	plt.draw()

a1bar.on_changed(update)
xo1bar.on_changed(update)
sigma1bar.on_changed(update)

a2bar.on_changed(update)
xo2bar.on_changed(update)
sigma2bar.on_changed(update)

plt.show()
"""
def reset(event):
	dbar.reset()
	erbar.reset()
	eibar.reset()
	urbar.reset()
	uibar.reset()
"""

"""
def save(event):
	#PARA DAR CERTO, TIVE QUE COLOCAR OS VALORES COMO GLOBAL NA FUNÇÃO DE CÁLCULO	
	new = open("./amostra"+str(round(d/1e-3,2))+".txt", 'w')
	new.write("Freq\tRL\te'\te''\tu'\tu''\n")
	
	for i in range(0,len(F_grafic)):
		escrever = "%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n"%(F_grafic[i],S11[i],e.real,e.imag,u.real,u.imag)
		new.write(escrever)
	new.close()


buttonreset.on_clicked(reset)
buttonsave.on_clicked(save)
"""
