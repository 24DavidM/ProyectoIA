from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import json
import pandas as pd

# === Crear la app FastAPI ===
app = FastAPI()

# === Rutas a modelos y archivos ===
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "../models/modelos.pkl")
metricas_path = os.path.join(BASE_DIR, "../models/model_metrics.json")
columns_path = os.path.join(BASE_DIR, "../models/model_columns.pkl")

# === Cargar modelo y recursos ===
modelo = joblib.load(model_path)

with open(metricas_path, "r", encoding="utf-8") as f:
    metricas = json.load(f)

# Cargar las columnas originales usadas para entrenar el modelo
model_columns = joblib.load(columns_path)

# === Definir esquema de entrada ===
class InputData(BaseModel):
    Age: float
    BMI: float
    Cholesterol: float
    Systolic_BP: float
    Diastolic_BP: float
    Smoking_Status: str
    Alcohol_Intake: float
    Physical_Activity_Level: str
    Family_History: str
    Diabetes: str
    Stress_Level: float
    Salt_Intake: float
    Sleep_Duration: float
    Heart_Rate: float
    LDL: float
    HDL: float
    Triglycerides: float
    Glucose: float
    Gender: str
    Education_Level: str
    Employment_Status: str

# === Endpoint raíz ===
@app.get("/")
def read_root():
    return {
        "msg": "Bienvenido a la API de predicción de hipertensión."
    }

# === Endpoint de predicción ===
@app.post("/predecir")
def predecir(data: InputData):
    try:
        # Convertir la entrada a DataFrame
        d = data.dict()
        df = pd.DataFrame([d])

        # Codificar variables categóricas con get_dummies
        df_encoded = pd.get_dummies(df)

        # Reindexar para que coincida con las columnas del modelo
        df_encoded = df_encoded.reindex(columns=model_columns, fill_value=0)

        # Obtener probabilidad de clase 1
        proba = modelo.predict_proba(df_encoded)[0][1]

        # Umbral personalizado
        umbral = 0.3
        pred = int(proba >= umbral)

        return {
            "Hypertension_Prediction": "High" if pred == 1 else "Low",
            "Probability": round(proba, 4),
            "Threshold": umbral
        }

    except Exception as e:
        return {"error": str(e)}

# === Endpoint de métricas ===
@app.get("/metricas")
def get_metrics():
    return metricas
