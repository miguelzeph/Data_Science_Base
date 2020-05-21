import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import time

def data(pais):
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    df = pd.read_csv(url)
    df = df[df['location']== pais].reset_index().drop('index',axis=1)
    df = df[['date','total_cases','total_deaths','new_deaths','new_cases']]
    df['date'] = pd.to_datetime(df['date'],format = '%Y/%m/%d')
    return df

df = data('Brazil')

"""
#fig, ax = plt.subplots()

k, = plt.plot(df['date'], df['total_cases'])
#df.plot(x = df['date'], y = df['total_cases'])
#plt.xticks(np.arange(0,df_new.shape[0],step = 30),rotation=20)
plt.title('teste')
plt.xticks(rotation=20)
plt.xlabel('')
the_plot = st.pyplot(plt)

time.sleep(2)
k.set_ydata(df['total_deaths'])
the_plot.pyplot(plt)
"""

sns.lineplot(x='date', y='total_cases', data=df)
plt.xticks(rotation=10)
st.pyplot()
