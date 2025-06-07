
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # (por ahora lo dejamos abierto, luego lo podemos restringir)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
