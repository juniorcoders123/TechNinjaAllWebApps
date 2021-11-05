import streamlit as st
import cv2
from PIL import Image
import numpy as np
import base64
from io import BytesIO


def app():
    def get_image_download_link(img):
        """Generates a link allowing the PIL image to be downloaded
        in:  PIL image
        out: href string
        """
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        href = f'<a href="data:file/jpg;base64,{img_str}">Download Resized Image</a>'
        return href

    st.title("Image Resizer Web App")
    uploaded_image = st.file_uploader('Upload Image', type=['png', 'jpeg', 'jpg'])
    ch = st.selectbox("Resize By", ("Percentage (Recommended)", "Dimensions"))
    if ch == "Percentage (Recommended)":

        if not uploaded_image:
            output = st.empty()
            output.warning('Please upload an image to proceed!')
        else:
            images = np.array(Image.open(uploaded_image))
            og_width = images.shape[1]
            og_height = images.shape[0]
            st.markdown("Original Measurements (in px)")
            st.text("Width = " + str(og_width) + " ," + " Height = " + str(og_height))
            percent = st.number_input("Resize Percentage(%)", 1)
            extracte = st.button("Resize Image")
            if extracte:
                nw = int(og_width * (percent / 100))
                nh = int(og_height * (percent / 100))
                img2 = cv2.resize(images, (nw, nh), interpolation=cv2.INTER_AREA)
                st.subheader("Original Image:")
                st.image(images)
                st.subheader("Resized Image:")
                st.image(img2)
                result = Image.fromarray(img2)
                st.markdown(get_image_download_link(result), unsafe_allow_html=True)


    elif ch == "Dimensions":

        if not uploaded_image:
            output = st.empty()
            output.warning('Please upload an image to proceed!')
        else:
            images = np.array(Image.open(uploaded_image))
            og_width = images.shape[1]
            og_height = images.shape[0]
            st.markdown("Original Measurements (in px)")
            st.text("Width = " + str(og_width) + " ," + " Height = " + str(og_height))
            st.markdown("Resizable Measurements (in px)")
            width = st.number_input('Enter Width(in px)', 1)
            height = st.number_input('Enter Height(in px)', 1)
            extracte = st.button("Resize Image")
            if extracte:
                nw = int(width)
                nh = int(height)
                img2 = cv2.resize(images, (nw, nh), interpolation=cv2.INTER_AREA)
                st.subheader("Original Image:")
                st.image(images)
                st.subheader("Resized Image:")
                st.image(img2)
                result = Image.fromarray(img2)
                st.markdown(get_image_download_link(result), unsafe_allow_html=True)


