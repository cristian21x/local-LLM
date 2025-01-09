import streamlit as st
from transformers import pipeline

text_generation_pipeline = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

st.title("Preguntas y Respuestas")
question = st.text_input("Pregunta:")

if st.button("Obtener Respuesta"):
    result = text_generation_pipeline(question, max_length=50, num_return_sequences=1)
    st.write(result[0]['generated_text']) 