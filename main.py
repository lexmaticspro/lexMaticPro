
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilitamos CORS para que el frontend pueda acceder
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base de datos simulada de modelos
modelos = {
    "Salud": [
        {
            "titulo": "Amparo por derivación médica",
            "fundamento": "Ley 23.661 art. 28 - Fallo: 'Sisamed' CSJN 2019.",
            "contenido": "Modelo de amparo para obtener derivación médica urgente de paciente con diagnóstico grave."
        },
        {
            "titulo": "Medida cautelar de cobertura de tratamiento",
            "fundamento": "Ley 26.682 - Fallo: 'Cañete' CSJN 2020.",
            "contenido": "Modelo de medida cautelar solicitando la cobertura de tratamiento oncológico integral."
        }
    ],
    "Familia": [
        {
            "titulo": "Demanda de Alimentos",
            "fundamento": "Art. 658 CCyC.",
            "contenido": "Modelo de demanda solicitando alimentos provisorios y definitivos."
        }
    ],
    # Puedes ir agregando más categorías
}

@app.get("/")
def home():
    return {"mensaje": "LexMatic Pro Backend activo."}

@app.get("/buscar")
def buscar_modelos(categoria: str):
    resultados = modelos.get(categoria, [])
    return {"resultados": resultados}
