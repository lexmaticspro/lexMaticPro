
# LexMatic Pro IA - Abogado Virtual en la Nube

from fastapi import FastAPI
import pandas as pd
from fuzzywuzzy import fuzz

# Cargar modelos (asegúrate que modelos.csv esté cargado en el repo)
modelos = pd.read_csv("modelos.csv")

# Crear la aplicación FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "LexMatic Pro IA online. Use /buscar?categoria=XXX para consultar."}

@app.get("/buscar")
def buscar(categoria: str):
    # Filtramos por categoría exacta
    filtrados = modelos[modelos['categoria'].str.lower() == categoria.lower()]

    # Si no hay resultados exactos, intentamos búsqueda aproximada
    if filtrados.empty:
        modelos['similitud'] = modelos['categoria'].apply(lambda x: fuzz.partial_ratio(x.lower(), categoria.lower()))
        filtrados = modelos.sort_values(by='similitud', ascending=False).head(5)
        resultados = filtrados.drop(columns=['similitud']).to_dict(orient="records")
        return {"resultados_aproximados": resultados}
    
    # Si hay coincidencias exactas:
    return {"resultados": filtrados.to_dict(orient="records")}
