import streamlit as st
from pytube import YouTube
from PIL import Image

def app():
    st.title("Youtube Video Donwloader")
    st.subheader("Developed with 💖 by TechNinja")
    st.subheader("Enter the URL:")
    url = st.text_input(label='URL')
    choice = st.selectbox("Choose Resolution",("Best Resolution","Low Resolution"))


    if url != '':
        yt = YouTube(url)
        st.image(yt.thumbnail_url, width=300)
        st.subheader('''
        {}
        ## Length: {} seconds
        ## Rating: {} 
        ## Views: {}
        '''.format(yt.title, yt.length, yt.rating,yt.views))
        video = yt.streams
        if len(video) > 0:
            downloaded, download_audio = False, False
            download_video = st.button("Download Video")
            if yt.streams.filter(only_audio=True):
                download_audio = st.button("Download Audio Only")
            if download_video:
                if choice == "Best Resolution":
                    video_1 = video.get_highest_resolution().download()
                    downloaded = True
                else:
                    video_1= video.get_lowest_resolution().download()
                    downloaded = True

            if download_audio:

                video_1 = video.filter(only_audio=True).first().download()
                downloaded = True
            if downloaded:
                st.video(video_1)
                st.subheader("Video Loading Completed. To download click the 3 dots in the media player. You can also preview it here.")
        else:
            st.subheader("Sorry, this video can not be downloaded")
