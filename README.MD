# 🩺 Sistema de Predicción de Hipertensión

---

## 🖥️ Despliegue

- **Backend:** 🚀 [https://stalind-static.hf.space/](https://stalind-static.hf.space/)  
- **Frontend:** 🌐 [https://sistemaprediccionweb.streamlit.app/](https://sistemaprediccionweb.streamlit.app/)

---


## 📊 Descripción

Este proyecto es un sistema de **predicción de hipertensión** basado en un dataset obtenido de Kaggle.  
El objetivo es predecir si un paciente tiene **hipertensión alta (High)** o baja (Low) a partir de variables clínicas y demográficas.

---

## 🧠 Entrenamiento y Mejora

- Se entrenó un modelo de **Random Forest** con balanceo de clases usando **SMOTE** para mejorar la predicción frente a datos desbalanceados.  
- Se usaron técnicas de preprocesamiento como codificación one-hot (`get_dummies`) y alineación de columnas para manejar variables categóricas.  

---

## 🚀 API y Endpoints

Se implementó una API REST usando **FastAPI** con los siguientes endpoints:

| Endpoint      | Método | Descripción                             |
|---------------|--------|-----------------------------------------|
| `/`           | GET    | Mensaje de bienvenida                   |
| `/predecir`   | POST   | Recibe datos del paciente y devuelve predicción de hipertensión (`High` o `Low`) y probabilidad |
| `/metricas`   | GET    | Devuelve métricas de evaluación del modelo |

---

## 💻 Uso del endpoint `/predecir`

Envía un JSON con los datos del paciente (variables clínicas y demográficas). Aquí dos ejemplos para copiar y pegar según la predicción esperada:

### ⚠️ Caso **High** (Alto riesgo hipertensión)
```json
{
  "Age": 65,
  "BMI": 35.0,
  "Cholesterol": 250,
  "Systolic_BP": 170,
  "Diastolic_BP": 95,
  "Smoking_Status": "Current",
  "Alcohol_Intake": 20.0,
  "Physical_Activity_Level": "Low",
  "Family_History": "Yes",
  "Diabetes": "Yes",
  "Stress_Level": 9.0,
  "Salt_Intake": 15.0,
  "Sleep_Duration": 5.0,
  "Heart_Rate": 90,
  "LDL": 180,
  "HDL": 40,
  "Triglycerides": 200,
  "Glucose": 180,
  "Gender": "Female",
  "Education_Level": "Primary",
  "Employment_Status": "Unemployed"
}
```

### ✅ Caso **Low** (Bajo riesgo hipertensión)
```json
{
  "Age": 30,
  "BMI": 22.0,
  "Cholesterol": 170,
  "Systolic_BP": 115,
  "Diastolic_BP": 75,
  "Smoking_Status": "Never",
  "Alcohol_Intake": 5.0,
  "Physical_Activity_Level": "High",
  "Family_History": "No",
  "Diabetes": "No",
  "Stress_Level": 3.0,
  "Salt_Intake": 6.0,
  "Sleep_Duration": 7.5,
  "Heart_Rate": 70,
  "LDL": 90,
  "HDL": 60,
  "Triglycerides": 100,
  "Glucose": 90,
  "Gender": "Male",
  "Education_Level": "Tertiary",
  "Employment_Status": "Employed"
}
```
