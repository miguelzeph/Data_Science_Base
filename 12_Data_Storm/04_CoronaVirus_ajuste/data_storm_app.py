import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

import time

@st.cache
def data(pais):
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    df = pd.read_csv(url)
    df = df[df['location']== pais].reset_index().drop('index',axis=1)
    df = df[['date','total_cases','total_deaths','new_deaths','new_cases']]
    df['date'] = pd.to_datetime(df['date'],format = '%Y/%m/%d')
    df.index = df['date']
    df.drop('date',axis=1,inplace=True)
    return df

# Título Página
st.header('COVID-19 - Fique por Dentro')

#images Exemplo com URL
from PIL import Image
from io import BytesIO
img = Image.open('./img/logo1.png')
st.image(img, width = 100)




# SelectBox
location = st.selectbox('location',sorted(['Germany','Brazil','Italy','United Kingdom','United States','China']),key= 'Brazil')



# Autenticação minha
#login = st.text_input('User','...')
#password = st.text_input('Password','...')
#submit = st.button('Submit')
#if submit == True  and (login != 'Miguel' or password != '123'):
#    st.warning('User or Pass wrong')
#if submit and login == 'Miguel' and password == '123':
    #....

if location:
    df = data(location)
    defaultcols = ['total_cases','total_deaths']
    cols = st.multiselect("Colunas Plotar", df.columns.tolist(), default=defaultcols)

    # Selecionar intervalo
    intervalo = st.slider("Intervalo de Dias", 0, int(len(df.index)),(0, len(df.index)))
    #intervalo =st.slider("eixo x - dia",0,len(df.index))
    
    html_temp = f"""
    <div style='background-color:tomato;'>
    <p style = 'color:white;font-size:25px;text-align: center;'>
    {location}
    </p>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    st.subheader(f"Informações - Data: {str(df.index[intervalo[0]]).split(' ')[0].replace('-','/')} - {str(df.index[intervalo[1]-1]).split(' ')[0].replace('-','/')}")
    st.write(f"(Intervalo Selecionado) Casos: {df['new_cases'][intervalo[0]:intervalo[1]].sum()} - Mortes: {df['new_deaths'][intervalo[0]:intervalo[1]].sum()}")
    st.write(f"Total Casos: {df['new_cases'].sum()}")
    st.write(f"Total Mortes: {df['new_deaths'].sum()}")
    st.line_chart(df[cols][intervalo[0]:intervalo[1]],height = 200)

#if st.checkbox('print'):
#    print(cols)
