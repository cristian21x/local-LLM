import streamlit as st
from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

st.title("Análisis de Sentimientos")
user_input = st.text_area("Introduce un texto para analizar:")

if st.button("Analizar"):
    result = sentiment_analysis(user_input)
    st.write(result) 