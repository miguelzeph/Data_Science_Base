import streamlit as st

# NLP Pkgs
import spacy#Biblioteca de processamento de linguagem natural
# Exemplo Spacym https://leportella.com/npl-com-spacy.html
from textblob import TextBlob#extBlob é uma biblioteca de software 
# livre para processar dados textuais, fornecendo uma API simples para se aprofundar em comum linguagem natural (NLP) 

def text_analyzer(my_text):
    npl = spacy.load('en_core_web_sm')
    #Para dar certo a instalacao do Modelo 'en_core_web_sm', tive que:
    #no terminar digitar: python3.6 -m spacy download en

    docx = npl(my_text)
    #for token in docx:
        #print(token.text)
    tokens = [token.text for token in docx]
    allData = [('"Tokens":{},\n"Lemma":{}'.format(token.text,token.lemma_)) for token in docx]
    return allData



def entity_analyzer(my_text):
    npl = spacy.load('en_core_web_sm')
    docx = npl(my_text)
    entities = [(entity.text,entity.label_) for entity in docx.ents]
    return entities
# Pkgs

def main():
    """NLP APp with Streamlit"""
    st.title('NLPiffy with Streamlit')
    st.subheader("Natural Language Processing on the Go")

    #Tokenization
    if st.checkbox('Show Tokens and Lemma'):
        st.subheader('Extract Entities From Your Text')
        message = st.text_area('Enter your Text','Type Here')

        #radio
        status = st.radio('choose the def function',('text_analyzer','entity_analyzer'))

        if st.button('Extract'):
            if status == "text_analyzer":
                npl_result = text_analyzer(message)
            if status == "entity_analyzer":
                npl_result = entity_analyzer(message)
            #npl_result = text_analyzer(message)
            #st.success(npl_result)
            st.json(npl_result)
    #Name Entity

    #Sentiment Analysis

    #Text Summaization


if __name__ == '__main__':
    main()