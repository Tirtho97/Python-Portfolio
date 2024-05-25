import streamlit as st

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
    """
    st.info(content)