import mysql.connector as sql
import pandas as pd


# Sabemos os nossos bancos de dados...
mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    password = 'xxxx',
    database = 'cadastro',#banco de dados que quer acessar
)


df = pd.read_sql('SELECT * FROM pessoas', con=mydb)#Tabela do banco de dados

print(df)


