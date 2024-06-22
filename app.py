import streamlit as st
import numpy as np
import cv2
from PIL import Image
from color_extractor import extract_colors, plot_colors

st.title("Color Picker from Image")
st.write("Upload an image to extract the most dominant colors")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, channels="BGR")

    num_colors = st.slider("Number of dominant colors", 1, 10, 5)
    colors = extract_colors(image, num_colors)

    st.write("Dominant Colors:")
    plot_colors(colors)
    
    for color in colors:
        st.write(f"RGB: {color}")
        st.markdown(
            f'<div style="width:50px;height:50px;background-color:rgb({color[0]},{color[1]},{color[2]});"></div>',
            unsafe_allow_html=True,
        )