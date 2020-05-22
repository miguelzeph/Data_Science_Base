import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import plotly.express as px

import time

def data(pais):
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    df = pd.read_csv(url)
    df = df[df['location']== pais].reset_index().drop('index',axis=1)
    df = df[['date','total_cases','total_deaths','new_deaths','new_cases']]
    df['date'] = pd.to_datetime(df['date'],format = '%Y/%m/%d')
    df.index = df['date']
    return df

df = data('Brazil')

defaultcols = ['total_cases','total_deaths']
cols = st.multiselect("Atributos", df.columns.tolist(), default=defaultcols)

# Exemplo com Streamlit ( eles tem line_chart e area_chart apenas)---
st.line_chart(df[cols])


# Exemplo com Matplotlib---------------------------------------------
sns.set() #Estilo

#Grafic 1 

ax = plt.subplot(221)
k, = plt.plot(df['date'], df['total_cases'])
#df.plot(x = df['date'], y = df['total_cases'])
#plt.xticks(np.arange(0,df_new.shape[0],step = 30),rotation=20)
plt.title('teste')
plt.xticks(rotation=20)
plt.xlabel('')
#the_plot = st.pyplot(plt)

#time.sleep(2)
#k.set_ydata(df['total_deaths'])
#the_plot.pyplot(plt)


# Grafico 2
ax = plt.subplot(222)
j, = plt.plot(df['date'], df['total_cases'])
#df.plot(x = df['date'], y = df['total_cases'])
#plt.xticks(np.arange(0,df_new.shape[0],step = 30),rotation=20)
plt.title('teste')
plt.xticks(rotation=20)
plt.xlabel('')
the_plot = st.pyplot(plt)

time.sleep(2)
j.set_ydata(df['total_deaths'])
the_plot.pyplot(plt)
plt.close()


#Exemplo com o Seaborn-----------------------------------------------

ax = plt.subplot(222)
sns.lineplot(x='date', y='total_cases', data=df)
plt.xticks(rotation=10)
st.pyplot()

# Plotly

f = px.histogram(df, x=df.index,y = 'total_deaths', title="Distribuição de Preços")
f.update_xaxes(title="data")
f.update_yaxes(title="Total_mortes")
st.plotly_chart(f)