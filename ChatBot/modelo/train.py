import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def train_model(data_path='data/salud_dataset.csv'):
    data = pd.read_csv(data_path)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data['question'])

    model = {
        'vectorizer': vectorizer,
        'matrix': X,
        'answers': data['answer'].tolist(),
        'questions': data['question'].tolist()
    }

    with open('modelo/model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("✅ Modelo entrenado y guardado.")
    return model
