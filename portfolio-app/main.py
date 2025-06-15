import streamlit as st

st.set_page_config(layout="wide", page_title="Portfolio App")

colLeft, colRight = st.columns(2)
with colLeft:
    st.image("images/my-photo.jpg")

with colRight:
    st.title("Zdravko Gospodinov")
    content = """
    Passionate software engineer with a focus on web development, distributed applications, 
    and microservices architecture. Experienced in system optimizations and scalable solutions.
    """
    st.info(content)