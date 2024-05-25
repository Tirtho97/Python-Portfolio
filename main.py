import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/profile_pic.jpg', width=400)

with col2:
    st.title('Tirthoraj Bhattacharya')
    content = """
    Hello! My name is Tirthoraj and I enjoy creating applications that enriches user experiences. 
    My fascinations for software development started in 2014 when I was in my 11th Standard and 
    first came in touch with writing code.

    This boosted my confidence and I started creating small to large scale apps that can help people in some ways atleast 
    and also enriches their web experience. Some of them are mentioned here below. 
    Do check those out and please provide your feedback so that the app can be made better and better!
    """
    st.info(content)

content2 = """
<h5>Below you can find some of the Python projects I've made. Feel free to contact me.</h4>
"""

st.markdown(content2, unsafe_allow_html=True)

col3, col4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])