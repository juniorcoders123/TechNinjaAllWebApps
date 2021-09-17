import streamlit as st
import qrcode
import base64
from io import BytesIO

def app():
    def get_image_download_link(img):
        """Generates a link allowing the PIL image to be downloaded
        in:  PIL image
        out: href string
        """
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        href = f'<a href="data:file/png;base64,{img_str}">Download result</a>'
        return href
    st.header("QR Code Web App")
    text = st.text_input("Enter text or link for which you want QR CODE")
    if st.button("Generate QR CODE"):
        if text == '':
            st.warning("Can not generate QR CODE if no text is given.")
        else:
            imgqr = qrcode.make(text)
            imgqr.save("sample.png")
            st.image("sample.png")
            st.success("QR CODE Generated Succesfully.")
            file = "sample.png"
            st.markdown(get_image_download_link(imgqr), unsafe_allow_html=True)



