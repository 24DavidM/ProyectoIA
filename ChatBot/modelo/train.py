import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def train_model(data_path='datos/salud_dataset.csv'):
    print("Ruta actual:", os.getcwd())
    print("Verificando existencia del archivo:", data_path)
    if not os.path.exists(data_path):
        print("El archivo no existe en esa ruta.")
        return

    data = pd.read_csv(data_path)
    print("CSV cargado correctamente.")
    print("Columnas encontradas:", data.columns)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data['question'])

    model = {
        'vectorizer': vectorizer,
        'matrix': X,
        'answers': data['answer'].tolist(),
        'questions': data['question'].tolist()
    }

    output_path = 'modelo/model.pkl'
    print("Guardando modelo en:", output_path)
    with open(output_path, 'wb') as f:
        pickle.dump(model, f)

    print("Modelo entrenado y guardado exitosamente.")
    return model

# Ejecuta si se llama directamente
if __name__ == '__main__':
    train_model()
