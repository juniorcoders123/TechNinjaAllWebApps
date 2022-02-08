import streamlit as st
from bokeh.models.widgets import Div

st.set_page_config(page_title='Streamlit Apps | TechNinja - Junior Coders', page_icon='💸', layout = 'wide', initial_sidebar_state = 'expanded')

#all my apps
import qrcodewebapp as qr
import recipedemo as rd
import text_summarizer as ts
import stockpredictor2 as sp2
import temp as tp
import quotegenerator as qgt
import imagetosketchwebapp as imgsktch
import horoscopewebappy as hwpy
import imageresizerwebapp as irwa
import midi2aud as m2a
import ytvideodownloader as ytvd
import imagetotextwebapp as ittwa
import pixelartconvertor as itnac

PAGES = {
    "Image to NFT Art Convertor[LATEST ✨]":itnac,
    "Image to Text Web App[BRAND NEW]":ittwa,
    "YouTube Video Downloader":ytvd,
    "Midi to Audio":m2a,
    "Image Resizer":irwa,
    "Horoscope Teller":hwpy,
    "Sketch Artist": imgsktch,
    "QR Generator": qr,
     "Recipe Teller": rd,
     "Stock Predictor": sp2,
     "Text Summarizer": ts,
     "Insulter/Praiser Bot": tp,
     "Quote Generator": qgt
    }

query_params = st.experimental_get_query_params()
default = int(query_params["activity"][0]) if "activity" in query_params else 0

st.sidebar.title('All my Apps!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()), index=default)
if selection:
    st.experimental_set_query_params(activity=list(PAGES).index(selection))
page = PAGES[selection]
page.app()

visit_polybit = "[Visit Polybit's Site!](https://share.streamlit.io/juniorcoders123/polybit-apps-streamlit/main/homepage.py?activity=0)"
github_repo = '[Visit the GitHub repository](https://github.com/juniorcoders123/TechNinjaAllWebApps)'
st.sidebar.markdown(visit_polybit, unsafe_allow_html=True)
st.sidebar.markdown(github_repo, unsafe_allow_html=True)
