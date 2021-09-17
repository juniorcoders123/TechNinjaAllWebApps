import streamlit as st
import qrcodewebapp as qr
import recipedemo as rd
import text_summarizer as ts
import stockpredictor2 as sp2
import temp as tp
import quotegenerator as qgt

st.set_page_config(page_title='Streamlit Apps | Junior Coders', layout = 'centered', initial_sidebar_state = 'expanded')

PAGES = {
    "QR CODE Generator": qr,
     "Recipe Teller":rd,
     "Stock Predictor":sp2,
     "Text Summarizer":ts,
     "Insulter Praiser Bot":tp,
     "Quote Generator":qgt
    }

st.sidebar.title('All my Apps!')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()