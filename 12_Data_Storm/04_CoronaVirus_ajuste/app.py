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


#sns.set() #Estilo
#options = st.multiselect('Choose a country?',['date','total_cases','total_deaths','new_deaths','new_cases'])

# SelectBox
location = st.selectbox('location',['Brazil','Italy','United Kingdom'],key= 'Brazil')
#st.write('You selected this option: ',occupation)

if location:
    df = data(location)
    #print(location)

    defaultcols = ['total_cases','total_deaths']
    cols = st.multiselect("Colunas Plotar", df.columns.tolist(), default=defaultcols)

    # Exemplo com Streamlit ( eles tem line_chart e area_chart apenas)---
    intervalo =st.slider("eixo x - dia",0,len(df.index))
    
    st.line_chart(df[cols][intervalo:])

#if st.checkbox('print'):
#    print(cols)
