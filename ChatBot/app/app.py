import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# configuración de la página
st.set_page_config(page_title="Chatbot Medicina", layout="centered")

# titulo principal
st.title("Un Chatbot de Atención Médica")
st.write("Este chatbot te ofrece respuestas sobre salud. Sin embargo te recomandamos una consulta médica profesional.")

# cargar modelo entrenado
try:
    with open('modelo/model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("No se encontró el modelo o aun no ha sido entrenado")
    st.stop()

# input del usuario
input_usuario = st.text_input("Escribe tu pregunta: ")

# procesamiento
if input_usuario:
    vec = model['vectorizer'].transform([input_usuario])
    sim = cosine_similarity(vec, model['matrix'])
    idx = sim.argmax()
    respuesta = model['answers'][idx]

    # respuesta
    st.success(f"💬 {respuesta}")
