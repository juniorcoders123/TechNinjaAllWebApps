from PIL import Image
import streamlit as st

def app():
    def pixelate(input_file_path, pixel_size):
        image = Image.open(input_file_path)
        image = image.resize(
            (image.size[0] // pixel_size, image.size[1] // pixel_size),
            Image.NEAREST
        )
        image = image.resize(
            (image.size[0] * pixel_size, image.size[1] * pixel_size),
            Image.NEAREST
        )
        image.save("demo.png")

    heading = st.title("Image to NFT Art")
    st.markdown('''
       Developed with 💖 by **Swarnim 'TechNinja' Chaudhuri**
       ### 
       ### ''')
    image_path = st.file_uploader("Upload Image File", type=['jpg', 'png', 'jfif', 'jpeg', 'webp'])

    if image_path is None:
        st.warning("Please upload an Image file to proceed")
    else:
        image_1 = Image.open(image_path)
        final_image = image_1
        original_image_holder, final_image_holder = st.columns(2)
        with original_image_holder:
            st.image(image_1, 'Original Image', use_column_width=True)
        max_dimension = min(image_1.size[0], image_1.size[1])
        select_dimension = st.slider("Adjust pixel size", 1, max_dimension, 5)
        pixelate(image_path, select_dimension)
        with final_image_holder:
            st.image("demo.png", 'Final Image', use_column_width=True)
        with open("demo.png", "rb") as file:
            btn = st.download_button(
                label="Download image",
                data=file,
                file_name="NFT_Art.png",
                mime="image/png"
            )
