import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="contact_form"):
    email = st.text_input("Your Email", key="email")
    message = st.text_area("Your Message", key="message")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        send_email(email, message)
        st.success("Your message has been sent!")