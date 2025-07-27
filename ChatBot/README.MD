# 🤖 RobDoc - ChatBot Médico

**RobDoc** es un sistema interactivo de asistencia médica que responde preguntas frecuentes utilizando procesamiento de lenguaje natural (NLP), y cuenta con una interfaz web amigable y un botón flotante para integrarse a cualquier sitio. Este proyecto incluye:

- ChatBot con modelo entrenado en preguntas médicas.
- Interfaz web moderna (`frontend/`) con botón flotante.
- App con Streamlit (`app/app.py`) para la interacción del usuario.
- API con FastAPI (`api/api.py`) para consultas programáticas.
- Script de entrenamiento para generar el modelo (`modelo/train.py`).

---

## 📁 Estructura del Proyecto

ChatBot/
│
├── README.md # Documentación general del proyecto
├── requirements.txt # Dependencias del proyecto
│
├── api/
│ └── api.py # API REST con FastAPI para responder preguntas
│
├── app/
│ └── app.py # Aplicación en Streamlit para el chatbot visual
│
├── datos/
│ └── salud_datos.csv # Dataset con preguntas y respuestas
│
├── frontend/
│ ├── index.html # Página web principal con el botón flotante
│ ├── styles.css # Estilos personalizados
│ └── recursos/ # Imágenes utilizadas en el frontend
│ ├── fondo.webp
│ ├── medicina-general.avif
│ ├── pediatria.jpg
│ └── psicologia.jpg
│
└── modelo/
├── model.pkl # Modelo entrenado y serializado
└── train.py # Script para entrenar y guardar el modelo


---

## 🚀 Cómo ejecutar el proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/2goddie7/robdoc.git
cd ChatBot
2. Instala los requisitos
bash
Copiar
Editar
pip install -r requirements.txt
3. Entrena el modelo (opcional)
bash
Copiar
Editar
python modelo/train.py
Asegúrate de que datos/salud_datos.csv esté presente antes de ejecutar.

4. Ejecuta la API con FastAPI
bash
Copiar
Editar
uvicorn api.api:app --reload
Esto lanzará la API en http://127.0.0.1:8000/docs (Swagger UI disponible).

5. Ejecuta la app con Streamlit
bash
Copiar
Editar
streamlit run app/app.py
Esto abre la interfaz de usuario para consultar a RobDoc.

🌐 Frontend
La carpeta frontend/ contiene una página web (index.html) con botón flotante que abre un iframe apuntando a la app de Streamlit (http://localhost:8501 por defecto). Puedes integrarla fácilmente en tu sitio web o sistema hospitalario.

🧠 Cómo funciona
El archivo train.py entrena un modelo basado en sentence-transformers y guarda los embeddings junto con las preguntas y respuestas.

La API (api/api.py) utiliza FastAPI para exponer un endpoint /consultar donde se recibe una pregunta y se devuelve la respuesta más parecida.

La app (app/app.py) usa Streamlit para mostrar categorías, preguntas frecuentes y un input para que el usuario escriba su consulta.

El frontend/index.html permite incrustar la app vía iframe, simulando una experiencia de chatbot accesible en cualquier página web.

🛠 Tecnologías utilizadas
Python

Streamlit

FastAPI

SentenceTransformers

scikit-learn

HTML + CSS

👥 Autores
Diego Mullo

📌 Notas
Asegúrate de tener corriendo el servidor de Streamlit en localhost:8501 para que el botón del chatbot funcione correctamente.

Puedes adaptar el dataset (salud_datos.csv) para especializar el chatbot en otros dominios como seguros, universidades, turismo, etc.

📄 Licencia
Este proyecto es de uso educativo. Puedes adaptarlo libremente.