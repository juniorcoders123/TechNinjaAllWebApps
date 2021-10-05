import streamlit as st
import cv2
from PIL import Image
import numpy as np
import base64
from io import BytesIO


def imgsktch():
    def get_image_download_link(img):
        """Generates a link allowing the PIL image to be downloaded
        in:  PIL image
        out: href string
        """
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>'
        return href

    st.title("Image to Sketch Web App")
    uploaded_image = st.file_uploader('Upload Image', type=['png', 'jpeg', 'jpg'])

    output = st.empty()
    extracte = st.button("Get Sketch From Image")
    if not uploaded_image:
        output.warning('Please upload an image to proceed!')
    else:
        if extracte:
            image = images = np.array(Image.open(uploaded_image))
            st.subheader("Given Image :")
            st.image(image)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            inverted_gi = 255 - gray_image
            blurred_img = cv2.GaussianBlur(inverted_gi, (21, 21), 0)
            inverted_bi = 255 - blurred_img
            pencilsketchimg = cv2.divide(gray_image, inverted_bi, scale=256.0)
            st.subheader("Sketch :")
            st.image(pencilsketchimg)
            result = Image.fromarray(pencilsketchimg)
            st.markdown(get_image_download_link(result), unsafe_allow_html=True)
