import streamlit as st
from PIL import Image

with st.expander("Camera Image", expanded=False):
    camera_image = st.camera_input("Camera")

img = Image.open(camera_image) if camera_image else None
gray_image = img.convert("L") if img else None
if gray_image:
    st.image(gray_image, caption="Grayscale Image", use_container_width=True)

# user_choice = st.radio("Number", options=[10, 20, 30], horizontal=True)
# if user_choice == 10:
#     st.info("You selected 10")