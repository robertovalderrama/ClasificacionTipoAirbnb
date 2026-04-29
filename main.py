from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import pickle
import pandas as pd

app = FastAPI()

# =========================
# 📁 Archivos estáticos
# =========================
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

import joblib

# =========================
# 🧠 Cargar modelos
# =========================

pipeline_procesamiento = joblib.load("pipeline.pkl")
modelo = joblib.load("modelo.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# =========================
# 📦 Input schema
# =========================
class InputData(BaseModel):
    neighbourhood_group: str
    neighbourhood: str
    latitude: float
    longitude: float
    price: float
    minimum_nights: int
    number_of_reviews: int
    reviews_per_month: float
    calculated_host_listings_count: int
    availability_365: int
    number_of_reviews_ltm: int
    city: str

# =========================
# 🧠 Función de predicción
# =========================
def predecir_nuevo_airbnb(datos_usuario):
    df_nuevo = pd.DataFrame([datos_usuario])

    # 🚀 Pipeline ya hace TODO
    pred_idx = pipeline_procesamiento.predict(df_nuevo)[0]

    # 🔤 Decodificar
    clase_predicha = label_encoder.inverse_transform([pred_idx])[0]

    return clase_predicha

# =========================
# 🌐 Frontend
# =========================
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

# =========================
# 🤖 API
# =========================
@app.post("/predict")
def predict(data: InputData):
    resultado = predecir_nuevo_airbnb(data.dict())
    return {"prediction": resultado}