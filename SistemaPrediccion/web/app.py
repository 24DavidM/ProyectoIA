import streamlit as st
import requests
import json
import os

# Base directory es 'web'
BASE_DIR = os.path.dirname(__file__)
categorical_model = os.path.join(BASE_DIR, "models", "categorical_allowed_values.json")

with open(categorical_model, 'r', encoding='utf-8') as f:
    categorias = json.load(f)

st.title("🌐 Sistema Web de Predicción de Hipertensión")

# Navbar lateral simple
menu = st.sidebar.radio("Navegación", ["Inicio", "Formulario", "Métricas"])

if menu == "Inicio":
    st.header("Bienvenido al Sistema de Predicción de Hipertensión")
    st.write(
        """
        Aquí puedes ingresar tus datos médicos para predecir el riesgo de hipertensión.
        Usa el menú lateral para navegar entre las secciones.
        """
    )

elif menu == "Formulario":
    with st.form("formulario_prediccion"):
        st.header("Datos Personales y Médicos")
        st.subheader("Información General")
        Age = st.number_input("Edad", min_value=0, max_value=120, value=30)
        BMI = st.number_input("IMC", min_value=10.0, max_value=60.0, value=22.00)
        Cholesterol = st.number_input("Colesterol", 50, 500, value=170)

        st.subheader("Presión Arterial")
        Systolic_BP = st.number_input("Presión Sistólica", 80, 250, value=115)
        Diastolic_BP = st.number_input("Presión Diastólica", 40, 150, value=75)

        st.subheader("Estilo de Vida")
        Smoking_Status = st.selectbox("Fuma", categorias["Smoking_Status"])
        Alcohol_Intake = st.number_input("Alcohol (g/día)", 0.0, 100.0, value=5.0)
        Physical_Activity_Level = st.selectbox("Actividad Física", categorias["Physical_Activity_Level"])

        st.subheader("Antecedentes y Salud")
        Family_History = st.selectbox("Antecedentes Familiares", categorias["Family_History"])
        Diabetes = st.selectbox("Diabetes", categorias["Diabetes"])
        Stress_Level = st.number_input("Estrés (0-10)", 0.0, 10.0, value=3.0)
        Salt_Intake = st.number_input("Sal (g/día)", 0.0, 30.0, value=6.0)
        Sleep_Duration = st.number_input("Sueño (horas)", 0.0, 16.0, value=7.5)
        Heart_Rate = st.number_input("Frecuencia Cardíaca", 40, 200, value=70)

        st.subheader("Laboratorio")
        LDL = st.number_input("LDL", 50, 400, value=90)
        HDL = st.number_input("HDL", 20, 120, value=60)
        Triglycerides = st.number_input("Triglicéridos", 50, 600, value=100)
        Glucose = st.number_input("Glucosa", 50, 400, value=90)

        st.subheader("Datos Demográficos")
        Gender = st.selectbox("Género", categorias["Gender"])
        Education_Level = st.selectbox("Nivel Educativo", categorias["Education_Level"])
        Employment_Status = st.selectbox("Estado Laboral", categorias["Employment_Status"])

        submit = st.form_submit_button("Predecir")

    if submit:
        try:
            input_data = {
                "Age": Age,
                "BMI": BMI,
                "Cholesterol": Cholesterol,
                "Systolic_BP": Systolic_BP,
                "Diastolic_BP": Diastolic_BP,
                "Smoking_Status": Smoking_Status,
                "Alcohol_Intake": Alcohol_Intake,
                "Physical_Activity_Level": Physical_Activity_Level,
                "Family_History": Family_History,
                "Diabetes": Diabetes,
                "Stress_Level": Stress_Level,
                "Salt_Intake": Salt_Intake,
                "Sleep_Duration": Sleep_Duration,
                "Heart_Rate": Heart_Rate,
                "LDL": LDL,
                "HDL": HDL,
                "Triglycerides": Triglycerides,
                "Glucose": Glucose,
                "Gender": Gender,
                "Education_Level": Education_Level,
                "Employment_Status": Employment_Status
            }

            url_api = "http://backend:8000/predecir"  # Cambiar si no usas Docker

            response = requests.post(url_api, json=input_data)
            result = response.json()

            if "Hypertension_Prediction" in result:
                pred = result["Hypertension_Prediction"]
                proba = result.get("Probability", None)
                if pred == "High":
                    st.error(f"⚠️ Riesgo de Hipertensión detectado. Probabilidad: {proba}")
                else:
                    st.success(f"✅ No se detecta hipertensión. Probabilidad: {proba}")
            else:
                st.error(f"Error: {result.get('error', 'Respuesta inesperada')}")

        except Exception as e:
            st.error(f"Error al procesar la predicción: {str(e)}")

elif menu == "Métricas":
    st.header("Métricas del Sistema")
    st.write("Aquí se mostrarán las métricas relevantes del modelo y sistema.")

    try:
        url_metrics = "http://backend:8000/metricas"
        res = requests.get(url_metrics)
        data = res.json()

        st.metric("Total de Predicciones", data.get("total_predictions", "N/A"))
        st.metric("Exactitud del Modelo", f'{data.get("accuracy", 0)*100:.2f}%')
        st.write(f"Última actualización: {data.get('last_updated', 'N/A')}")

    except Exception as e:
        st.error(f"No se pudieron cargar las métricas: {str(e)}")
