import gdown
import os

# URLs con el ID de tu Google Drive para cada archivo modelo
MODELS = {
    "modelos.pkl": "1lk4ZTUQUho-atF4cBI8elEg-s73_OAz-",
    "model_metrics.json": "1rQ-Z2pYhmPFqJxxrMsj6v2P4s536omZo",
    "model_columns.pkl": "1r1GL4klh1sR76oLIjbov9Dyarc67QVF7"
}

MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")

os.makedirs(MODEL_DIR, exist_ok=True)

for filename, file_id in MODELS.items():
    filepath = os.path.join(MODEL_DIR, filename)
    if not os.path.exists(filepath):
        url = f"https://drive.google.com/uc?id={file_id}"
        print(f"Descargando {filename}...")
        gdown.download(url, filepath, quiet=False)
    else:
        print(f"{filename} ya existe, no se descarga.")
