entrada = [[0,0],[0,1],[1,0],[1,1]]
peso = [0,0]
saida = [0,0,0,1] # Operador Booleano - E (AND)
#saida =[0,1,1,1] # Operador Booleano - OU (OR)
#saida = [0,1,1,0] # Operador XOR ... Esse nao vai dar

taxaAprendizado = 0.1

def degrau(valor):
    
    if valor >= 1:
        return 1
    else:
        return 0
    
def soma():
    
    resultado = []
    
    for e in entrada:
        
        calculo = e[0]*peso[0] + e[1]*peso[1]
        
        resultado.append(degrau(calculo))
    
    print(f"Para os Pesos = {peso}, resultado = {resultado}")
    return resultado

def treinar():
    
    k = soma()
    epoca = 0
    while k != saida:
        
        for i in range(len(saida)):
            
            
            erro = (saida[i] - soma()[i])
            
            for j in range(len(peso)):
                
                peso[j] = round(peso[j] + (taxaAprendizado*entrada[i][j]*erro),2)
                
                k = soma()
            epoca += 1
    return print(f'Época: {epoca}')
        
treinar()
