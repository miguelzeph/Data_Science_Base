#fonte: https://www.youtube.com/watch?v=_9WiB2PDO7k&list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU
import streamlit as st


# Autenticação minha
#login = st.text_input('User','...')# Por texto
login = st.selectbox('User',['Miguel','Ana','Priscila'])
#password = st.text_input('Password','...',type = 'password')
password = st.text_input('Password',type = 'password')
submit = st.button('Submit')
if submit == True  and (login != 'Miguel' or password != '123'):
    st.warning('User or Pass wrong')
if submit and login == 'Miguel' and password == '123':
    st.success('Logado')


#Text/title
st.title('Streamlit Tutorials')

#Header/Subheader
st.header('This is a Header')
st.subheader('This is a Subheader')

#text
st.text('Hello Streamlit')

# markdown
st.markdown('### This is MArkdown')

#error/colorful text
st.success('Sucessful')
st.info('Information')
st.warning('This is a Warning')
st.error('This is a error')
st.exception("NameErro('name three not defined)")

#help infor about python
st.help(print)

# writing text
st.write(range(10))

#images Exemplo com URL
from PIL import Image
import requests
from io import BytesIO
response = requests.get('https://abrilviagemeturismo.files.wordpress.com/2017/03/coliseu2.jpg')
img = Image.open(BytesIO(response.content))
st.image(img, width = 500,caption='Coliseu')
#exemplo sem URL
#img = Image.open('nome.png')
#st.image(img, width = 500,caption='Coliseu')

#Videos
vid_file = open('/home/miguel/Vídeos/miguel_lorentzmodel.mkv','rb').read()
st.video(vid_file)

#Audio
#audio_file = open('Example.mp3','rb').read()
#st.audio(audio_file, format = 'audio/mp3')

#widget

#checkbox
if st.checkbox('Show/Hide'):
    st.text('Showing or Hiding Widget')
#radio
status = st.radio('what is your status',('Active','Inactive'))
if status == "Active":
    st.success('You are Active')
else:
    st.warning("You are Inactive")

# SelectBox
occupation = st.selectbox('Your occupation',['Programmer','DataScientist','Doctor'])
st.write('You selected this option: ',occupation)

#multiselect
location = st.multiselect('where do you wrok?',['London','New York','Accra'])
st.write('you selected ',len(location),' locations')

# Slider

age =st.slider("What is your level",1,5)


# button
b = st.button('Simple button')
if b:
    st.text('Streamlit is cool')

#text input
firstname = st.text_input('Enter your First name','Type Here ...')

if st.button('Submit'):
    result = firstname.title()
    st.success(result)

# Text Area 
message = st.text_area('Enter your message','Type Here ...')
if st.button('Submit2'):
    result = message.title()
    st.success(result)

# Date Input
import datetime
today = st.date_input('Today is', datetime.datetime.now())

# time

the_time = st.time_input('The time is', datetime.time())

# displaying JSON
st.text('Display JSON')
st.json({'name':'Miguel','gender': 'male'})


# display raw code
st.text('Display raw code')
st.code('import numpy as np\n print(np.arange(0,10))')

# display raw code - mode 2
with st.echo():
    #this will also show as a comment
    import pandas as pd
    df = pd.DataFrame()

# Process Bar
import time
my_bar = st.progress(0)
for p in range(100):
    time.sleep(0.02)
    my_bar.progress(p+1)

# Spinner
with st.spinner('waiting...'):
    time.sleep(2)
st.success('Finished')

# balloons
st.balloons()


#sidebar
st.sidebar.header('About')
st.sidebar.text('This is streamlit tutorial')


#functions
@st.cache
def run_fxn():
    return range(100)
st.write(run_fxn())




import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
#Plot
st.pyplot()

#dataframe
st.dataframe(df)

#table
st.table(df)

