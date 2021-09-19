import streamlit as st
import webbrowser

st.set_page_config(page_title='Streamlit Apps | TechNinja - Junior Coders', page_icon='😎', layout = 'wide', initial_sidebar_state = 'expanded')

#all my apps
import qrcodewebapp as qr
import recipedemo as rd
import text_summarizer as ts
import stockpredictor2 as sp2
import temp as tp
import quotegenerator as qgt

PAGES = {
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

visit_polybit_site = st.sidebar.button("Visit Polybit's Site!")
if visit_polybit_site:
    webbrowser.open('https://share.streamlit.io/juniorcoders123/polybit-apps-streamlit/main/homepage.py?activity=0')
