import streamlit as st

st.title("¿Tienes dudas?")
st.write("""RobDoc te ayuda!""")

# Aquí el chatbot
with st.expander("Haz clic para ver las opcoines"):
    user_input = st.text_input("Pregunta aquí:")
    if user_input:
        # Aquí iría el código para responder usando el modelo entrenado
        st.write(f"Respuesta simulada para: {user_input}")
