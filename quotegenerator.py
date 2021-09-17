import streamlit as st
import requests
from gtts import gTTS

def app():
    api = 'http://api.quotable.io/random'

    quotes = []
    quotes_no = 0

    st.header("JUNIOR CODERS QUOTE GENERATOR")
    if st.button("Generate Quote"):
        st.write("<h1 style='text-align: center;'>Quote For You</h1>", unsafe_allow_html=True)

        for x in range(1):
            random_quotes = requests.get(api).json()
            content = random_quotes["content"]
            author = random_quotes["author"]
            st.subheader(content)
            quote = content + "\n\n." + "By " + author
            st.subheader("By " + author)
            tts = gTTS(text=quote, lang='en', tld='co.uk')
            tts.save('example.mp3')
            audio_file = open(f"example.mp3", "rb")
            audio_bytes = audio_file.read()
            st.markdown(f"## Quote Audio:")
            st.audio(audio_bytes, format="audio/mp3", start_time=0)

