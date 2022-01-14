import streamlit as st
from pytube import YouTube
from PIL import Image

def app():
    st.title("Youtube Video Donwloader")
    st.subheader("Developed with 💖 by TechNinja")
    st.subheader("Enter the URL:")
    url = st.text_input(label='URL')
    if url != '':
        yt = YouTube(url)
        st.image(yt.thumbnail_url, width=300)
        st.subheader('''
        {}
        ## Length: {} seconds
        ## Rating: {} 
        '''.format(yt.title, yt.length, yt.rating))
        video = yt.streams
        if len(video) > 0:
            downloaded, download_audio = False, False
            download_video = st.button("Download Video")
            if yt.streams.filter(only_audio=True):
                download_audio = st.button("Download Audio Only")
            if download_video:
                st.spinner("Please Wait Patiently Video File is being downloaded.")
                video.get_lowest_resolution().download()
                downloaded = True
            if download_audio:
                st.spinner("Please Wait Patiently Audio File is being downloaded.")
                video.filter(only_audio=True).first().download()
                downloaded = True
            if downloaded:
                st.subheader("Download Complete")
        else:
            st.subheader("Sorry, this video can not be downloaded")