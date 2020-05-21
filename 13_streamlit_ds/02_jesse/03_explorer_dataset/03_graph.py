#font: https://www.youtube.com/watch?v=SIu2VL-RAXc&list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU&index=5
import os
import streamlit as st

import pandas as pandas

import matplotlib.pyplot as pyplot
import matplotlib
matplotlib.use('Agg')

import seaborn as sns

def main():
    """"Common ML Dataset Explorer"""
    st.title('Common ML Dataset Explorer')
    st.subheader('Simple Data Science Explorer')

    html_temp = """
    <div style='background-color:tomato;'>
    <p style = 'color:white;font-size:50px;text-align: center;'>
    Streamlit is Awesome
    </p>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

if __name__ == '__main__':
    main()
