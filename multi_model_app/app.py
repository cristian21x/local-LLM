import streamlit as st
from models import ModelIterator

models = [
    "Qwen/Qwen2.5-0.5B-Instruct",
    "google/vit-base-patch16-224",
]

if 'model_iterator' not in st.session_state:
    st.session_state.model_iterator = ModelIterator(models)

st.title("Iterar entre Modelos")

if st.button("Cambiar Modelo"):
    st.session_state.model_iterator.switch_model()

st.write(f"Modelo actual: {models[st.session_state.model_iterator.current_model_index]}")

current_model = models[st.session_state.model_iterator.current_model_index]
if "Qwen" in current_model:
    question = st.text_input("Pregunta:", key='text_input')
    if st.button("Obtener Respuesta"):
        if question:
            answer = st.session_state.model_iterator.query(text=question)
            st.write("Respuesta:", answer)
elif "vit" in current_model:
    uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"], key='image_input')
    if uploaded_file is not None:
        answer = st.session_state.model_iterator.query(image=uploaded_file)
        st.write("Resultado:", answer)
