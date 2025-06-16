import streamlit as st

st.header("Contact Me")

with st.form(key="contact_form"):
    st.text_input("Your Email", key="email")
    st.text_area("Your Message", key="message")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.success("Your message has been sent!")