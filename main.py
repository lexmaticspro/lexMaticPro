from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS (esto permite que el frontend se comunique con el backend sin bloqueos)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Si querés podés reemplazar "*" por la URL de tu frontend para más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos de ejemplo
modelos = {
    "Salud": [
        {
            "titulo": "Amparo por derivación médica",
            "fundamento": "Ley 23.661 art. 28 - Fallo: 'Sisamed' CSJN 2019.",
            "descripcion": "Modelo de amparo para obtener derivación médica urgente de paciente con diagnóstico grave."
        },
        {
            "titulo": "Medida cautelar de cobertura de tratamiento",
            "fundamento": "Ley 26.682 - Fallo: 'Cañete' CSJN 2020.",
            "descripcion": "Modelo de medida cautelar solicitando la cobertura de tratamiento oncológico integral."
        }
    ],
    "Familia": [
        {
            "titulo": "Alimentos provisorios",
            "fundamento": "Código Civil y Comercial art. 544.",
            "descripcion": "Modelo de solicitud de alimentos provisorios durante el trámite de divorcio."
        }
    ]
}

# Endpoint básico de prueba
@app.get("/")
def home():
    return {"mensaje": "Backend de LexMatic Pro funcionando correctamente."}

# Endpoint principal de búsqueda
@app.get("/buscar")
def buscar_modelos(categoria: str):
    resultados = modelos.get(categoria, [])
    return {"modelos": resultados}
