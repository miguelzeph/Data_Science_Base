#font: https://www.youtube.com/watch?v=SIu2VL-RAXc&list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU&index=5
import os
import streamlit as st

import pandas as pd

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

    # ------Explorador de Documentos-------
    def file_selector(folder_path = './datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Select A file',filenames)
        return os.path.join(folder_path, selected_filename)
    filename = file_selector()
    st.info(f'You selected {filename}')
    

    # Read Date
    df = pd.read_csv(filename)

    # Show Datasets
    if st.checkbox('Show Dataset'):
        number = st.number_input('Number of Rows to View',5,df.shape[0])
        st.dataframe(df.head(number))

    # Show Columns
    if st.button('Column Names'):
        st.write(df.columns)

    # Show Shape
    if st.checkbox('Shape of Dataset'):
        st.write(df.shape)
        data_dim = st.radio('Show dimension by', ('Rows', 'Columns'))
        if data_dim == 'Columns':
            st.text('Number of Columns')
            st.write(df.shape[1])
        if data_dim == 'Rows':
            st.text('Number of Rows')
            st.write(df.shape[0])
    # Select Columns
        if st.checkbox('Select columns to Show'):
            all_columns = df.columns.tolist()
            selected_columns = st.multiselect('Select', all_columns)
            new_df = df[selected_columns]
            st.dataframe(new_df)
    # Show Summary
    if st.checkbox('Summary'):
        st.write(df.describe().T)

    #-------- Plot and Visualization ----------
    st.subheader('Data Visualization')

    
    # Seaborn plot
    if st.checkbox('Corralation plot(Seaborn)'):
        st.write(sns.heatmap(df.corr(),annot = True))
        st.pyplot()
    
    # Pie Chart
    if st.checkbox('Pie Plot'):
        all_columns_names = df.columns.tolist()
        if st.button('Generate Plot1'):
            st.success('Generating a Pie Plot')
            st.write(df.iloc[:,1].value_counts().plot.pie(autopct = "%1.1f%%"))
            st.pyplot()
    # Count Plot
    if st.checkbox('Plot of Value Counts'):
        st.text('Value Counts by Targets')
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox('Primary Column to GroupBy',all_columns_names)
        selected_columns_names = st.multiselect('Select columns',all_columns_names)
        if st.button('Plot'):
            st.text('Generate Plot')
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind='bar'))
            st.pyplot()
    
    #Customized Plot
    st.subheader('Customizable Plot')
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox('Select Type of Plot',['area','bar','line','hist','box','kde'])
    selected_columns_names = st.multiselect('Select Column to Plot',all_columns_names)
    
    if st.button('Generate Plot'):
        st.success(f'Generatin Customizable Plot of {type_of_plot} for {selected_columns_names}')
        # Plot by Streamlit
        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)
        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)
        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)
        #Custom Plot
        elif type_of_plot:
            cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()


if __name__ == '__main__':
    main()
