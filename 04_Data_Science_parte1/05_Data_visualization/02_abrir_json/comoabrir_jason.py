
#ABRIR DADOS
import json
import pandas as pd

with open("source_file_2.json", 'r') as json_file:
    dados = json.load(json_file)

#print(dados[0])


df = pd.DataFrame(dados)

print(df)

#SALVAR DADOS

with open('./teste.json', 'w') as json_file:
    json.dump(dados, json_file,indent=2)


#Podemos importar do PANDA e também EXPORTAR do Panda






