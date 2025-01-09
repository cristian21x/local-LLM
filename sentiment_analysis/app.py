import streamlit as st
from transformers import pipeline

# Cargar el modelo de análisis de sentimientos
sentiment_analysis = pipeline("sentiment-analysis")

st.title("Análisis de Sentimientos")
st.markdown("### 📝 Introduce un texto para analizar:")
user_input = st.text_area("")

if st.button("Analizar"):
    result = sentiment_analysis(user_input)
    st.markdown("### 📊 Resultado:")
    for res in result:
        st.write(f"**Etiqueta:** {res['label']}, **Confianza:** {res['score']:.2f}") 