import streamlit as st
from gtts import gTTS
import requests

def app():
    def horoscope(sign, day):
        params = (
            ('sign', sign), ('day', day)
        )
        response = requests.post('https://aztro.sameerkumar.website/', params=params)
        json = response.json()
        about = ("Horoscope - " + sign.upper() + "\n" +
                 "Predictions for - " + json.get("current_date") + "\n" +
                 "About - " + json.get("description") + "\n" +
                 "Compatibility - " + json.get("compatibility") + "\n" +
                 "Mood - " + json.get("mood") + "\n" +
                 "Color - " + json.get("color") + "\n" +
                 "Lucky Number - " + json.get("lucky_number") + "\n" +
                 "Lucky Time - " + json.get("lucky_time"))
        return about

    st.title("Junior Coders Online Horoscope")
    zodiacs = (
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius",
    "Pisces")
    bd = st.selectbox("Choose Zodiac Sign", zodiacs)
    date = st.selectbox("Choose date for prediction", (("Today", "Tomorrow", "Yesterday")))
    aud = st.checkbox("Want Audio for Horoscope ?")
    if st.button("Get Horoscope"):
        text = st.code(horoscope(bd, date))
        if aud:
            text_1 = horoscope(bd, date)
            tts = gTTS(text=text_1, lang='en', tld='co.uk')
            tts.save('example.mp3')
            audio_file = open(f"example.mp3", "rb")
            audio_bytes = audio_file.read()
            st.markdown(f"## Horoscope audio:")
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
