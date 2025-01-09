import streamlit as st
from models import ModelIterator
from PIL import Image

def select_icons():
    question_icon = st.selectbox("Selecciona un icono para las preguntas:", ["🧑", "🤖", "❓"])
    answer_icon = st.selectbox("Selecciona un icono para las respuestas:", ["🤖", "🧑", "✅"])
    return question_icon, answer_icon

models = [
    "Qwen/Qwen2.5-0.5B-Instruct",
    "google/vit-base-patch16-224",
]

if 'model_iterator' not in st.session_state:
    st.session_state.model_iterator = ModelIterator(models)

st.title("Iterar entre Modelos")

question_icon, answer_icon = select_icons()

if st.button("Cambiar Modelo"):
    st.session_state.model_iterator.switch_model()

st.write(f"Modelo actual: {models[st.session_state.model_iterator.current_model_index]}")

current_model = models[st.session_state.model_iterator.current_model_index]
if "Qwen" in current_model:
    st.markdown(f"### {question_icon} Pregunta:")
    question = st.text_input("", key='text_input')
    if st.button("Obtener Respuesta"):
        if question:
            answer = st.session_state.model_iterator.query(text=question)
            st.markdown(f"### {answer_icon} Respuesta:")
            st.write(answer)
elif "vit" in current_model:
    st.markdown("### 🖼️ Sube una imagen:")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"], key='image_input')
    if uploaded_file is not None:
        answer = st.session_state.model_iterator.query(image=uploaded_file)
        st.markdown("### 📊 Resultado:")
        st.write(answer)
