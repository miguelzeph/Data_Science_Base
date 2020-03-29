#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Aulas Sec 3 - Multicamadas
"""

import numpy as np

#------------Definição das Variaveis ---------------
entradas = np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1]])

saidas = np.array([[0],[1],[1],[0]]) # XOR

#CAMADA OCULTA- Pesos de X1 e X2 (três de cada)
#pesos0 = np.array([[-0.424,-0.740,-0.961],
                  #[0.358,-0.577,-0.469]])

#CAMADA SAIDA - Psesos de X1 e X2
#pesos1 = np.array([[-0.017],[-0.893],[0.148]])

pesos0 = np.random.random((2,3))
pesos1 = np.random.random((3,1))

epocas = 100000
#---------------------------------------------------

def sigmoid(soma):
    
    # exp não retorna valor negativo
    return 1/(1+np.exp(-soma))

def sigmoid_derivada(sig):
   return sig*(1-sig) 

taxaAprendizagem = 0.3
momento = 1

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada,pesos0)
    camadaOculta = sigmoid(somaSinapse0)
    somaSinapse1 = np.dot(camadaOculta,pesos1)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamadaSaida = saidas - camadaSaida
    mediaAbsoluta = np.mean(abs(erroCamadaSaida))
    
    print("Erro: "+str(mediaAbsoluta))
    
    derivadaSaida = sigmoid_derivada(camadaSaida)
    deltaSaida = erroCamadaSaida*derivadaSaida
    
    #fazer matriz transposta - nao da para fazer direto 4 linhas por 3 linhas
    pesos1Transposta = pesos1.T
    #agora da para multiplicar
    deltaSaidaXPeso = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPeso * sigmoid_derivada(camadaOculta)
    
    camadaOcultaTransposta = camadaOculta.T
    
    pesosNovo1 = camadaOcultaTransposta.dot(deltaSaida)
    
    pesos1 = pesos1*momento + pesosNovo1*taxaAprendizagem
    
    camadaEntradaTransposta = camadaEntrada.T
    pesosNovo0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = pesos0*momento + pesosNovo0*taxaAprendizagem
    
    
    