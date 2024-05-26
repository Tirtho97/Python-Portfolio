import streamlit as st

# st.set_page_config(layout='wide')

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your Message:")
    button = st.form_submit_button("Submit")

    if button:
        print("Submit Button pressed!")