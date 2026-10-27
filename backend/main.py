from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from rotas import clientes, senioridade, tatuadores, agendamento, estilos, usuarios, login

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOADS_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOADS_DIR), name="uploads")

app.include_router(login.router, tags=["Login"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
app.include_router(senioridade.router, prefix="/senioridade", tags=["Senioridade"])
app.include_router(estilos.router, prefix="/estilos", tags=["Estilos"])
app.include_router(tatuadores.router, prefix="/tatuadores", tags=["Tatuadores"])
app.include_router(agendamentos.router, prefix="/agendamentos", tags=["Agendamentos"])

@app.get("/")
def inicio():
    return {"mensagem": "API do estúdio de tatuagem funcionando!"}

