import streamlit as st
from models import ModelIterator

models = ["distilgpt2", "EleutherAI/gpt-neo-2.7B"]

model_iterator = ModelIterator(models)

st.title("Iterar entre Modelos")
question = st.text_input("Pregunta:")

if st.button("Obtener Respuesta"):
    answer = model_iterator.query(question=question)
    st.write(answer)

if st.button("Cambiar Modelo"):
    model_iterator.switch_model()
    st.write(f"Modelo actual: {models[model_iterator.current_model_index]}") 