import streamlit as st
from gensim.summarization import summarize
from gtts import gTTS
import base64
import time

def app():
    timestr = time.strftime("%Y%m%d-%H%M%S")

    def text_download(rawtext):
        b64 = base64.b64encode(rawtext.encode()).decode()
        new_filename = "new_text_file_{}_.txt".format(timestr)
        st.markdown("#### Download Files ###")
        href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Download Summary(Text File)</a>'
        st.markdown(href, unsafe_allow_html=True)

    def inp_download(rawtext):
        b64 = base64.b64encode(rawtext.encode()).decode()
        new_filename = "new_text_file_{}_.txt".format(timestr)
        href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Download Text Input(Text File)</a>'
        st.markdown(href, unsafe_allow_html=True)

    st.header("Junior Coders Text Summarizer")
    choice_2 = st.selectbox("Summarization Process", ("By Ratio", "By Number of Words"))
    if choice_2 == "By Ratio":
        text_area = st.text_area("Write Text Here:", height=200)
        inputtext = text_area
        t = st.slider('Summarization Ratio(%)', 10, 100)
        aud = st.checkbox("Do you want Audio For Given Text and Summary?")
        if st.button("Get Summary"):
            if text_area == '':
                st.warning("Cannot Summarize if text is empty")
            else:
                outputtext = summarize(inputtext, ratio=t / 100)
                if outputtext == '':
                    st.warning("Text should be given in English or the text given is too short.")
                else:
                    st.subheader("Summary Text")
                    text_area = st.write(outputtext)
                    text_download(outputtext)
                    inp_download(inputtext)
                    if aud:
                        st.subheader("Audios")
                        tts = gTTS(text=inputtext, lang="en-us", tld='co.in')
                        tts.save('textgiven.mp3')
                        audio_file = open(f"textgiven.mp3", "rb")
                        audio_bytes = audio_file.read()
                        st.markdown(f"## Audio of Given Text:")
                        st.audio(audio_bytes, format="audio/mp3", start_time=0)
                        tts = gTTS(text=outputtext, lang="en-us", tld='co.in')
                        tts.save('textextracted.mp3')
                        audio_file = open(f"textextracted.mp3", "rb")
                        audio_bytes = audio_file.read()
                        st.markdown(f"## Audio of Summarized Text:")
                        st.audio(audio_bytes, format="audio/mp3", start_time=0)

    if choice_2 == 'By Number of Words':
        text_area = st.text_area("Write Text Here:", height=200)
        inputtext = text_area
        if (len(text_area)):
            t = st.slider('No.of Words', 10, len(inputtext.split()))
            aud = st.checkbox("Do you want Audio For Given Text and Summary?")
        if st.button("Get Summary"):
            if text_area == '':
                st.warning("Cannot Summarize if text is empty")
            else:
                outputtext = summarize(inputtext, word_count=t)
                if outputtext == '':
                    st.warning("Text should be given in English or the text given is too short.")
                else:
                    st.subheader("Summary Text")
                    text_area = st.write(outputtext)
                    text_download(outputtext)
                    inp_download(inputtext)

                    if aud:
                        st.subheader("Audios")
                        tts = gTTS(text=inputtext, lang="en-us", tld='co.in')
                        tts.save('textgiven.mp3')
                        audio_file = open(f"textgiven.mp3", "rb")
                        audio_bytes = audio_file.read()
                        st.markdown(f"## Audio of Given Text:")
                        st.audio(audio_bytes, format="audio/mp3", start_time=0)
                        tts = gTTS(text=outputtext, lang="en-us", tld='co.in')
                        tts.save('textextracted.mp3')
                        audio_file = open(f"textextracted.mp3", "rb")
                        audio_bytes = audio_file.read()
                        st.markdown(f"## Audio of Summarized Text:")
                        st.audio(audio_bytes, format="audio/mp3", start_time=0)











