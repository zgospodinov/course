import streamlit as st
import pandas as pd

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

general_message = """
## Below you can find my projects and apps I have built in Python. 
Feel free to contact me for any questions or collaborations.
"""
st.write(general_message)

col3, empty_column, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        if index % 2 == 0:  
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"], width=300)
            st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df.iterrows():
        if index % 2 == 1:  
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"], width=300)
            st.write(f"[Source Code]({row['url']})")
