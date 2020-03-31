import json
import pandas as pd

with open("source_file_2.json", 'r') as json_file:
    dados = json.load(json_file)
print(dados[0])


df = pd.DataFrame(dados)

print(df)


#print(type(dados))



