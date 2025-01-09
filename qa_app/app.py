import streamlit as st
from transformers import pipeline

def select_icons():
    question_icon = st.selectbox("Selecciona un icono para las preguntas:", ["🧑", "🤖", "❓"])
    answer_icon = st.selectbox("Selecciona un icono para las respuestas:", ["🤖", "🧑", "✅"])
    return question_icon, answer_icon

text_generation_pipeline = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

st.title("Preguntas y Respuestas")

question_icon, answer_icon = select_icons()

st.markdown(f"### {question_icon} Pregunta:")
question = st.text_input("")

if st.button("Obtener Respuesta"):
    prompt = f"Contexto: eres un asistente que responde preguntas sencillas:\nPregunta: {question}\nRespuesta:"
    result = text_generation_pipeline(prompt, max_length=150, num_return_sequences=1)
    st.markdown(f"### {answer_icon} Respuesta:")
    st.write(result[0]['generated_text'].split("Respuesta:")[1].strip())