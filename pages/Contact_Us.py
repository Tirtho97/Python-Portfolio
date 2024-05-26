import streamlit as st
from send_email import send_email

# st.set_page_config(layout='wide')

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message:")
    button = st.form_submit_button("Submit")
    message = f"""\
Subject: New Mail from {user_email}

From: {user_email} \n
{raw_message}
"""

    if button:
        send_email(message)
        st.success("Your email was sent successfully!")