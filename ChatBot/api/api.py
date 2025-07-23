from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

with open('modelo/model.pkl', 'rb') as f:
    model = pickle.load(f)

class Consulta(BaseModel):
    pregunta: str

@app.post("/consultar")
def consultar_salud(consulta: Consulta):
    vec = model['vectorizer'].transform([consulta.pregunta])
    sim = cosine_similarity(vec, model['matrix'])
    idx = sim.argmax()
    return {"respuesta": model['answers'][idx]}