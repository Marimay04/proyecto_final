"""
API del Proyecto Final - Programacion Aplicada
===============================================
Backend (FastAPI) que consulta y administra los datos del proyecto,
guardados en MongoDB.

Como ejecutar (en una terminal, dentro de esta carpeta):
    pip install -r requirements.txt
    uvicorn api:app --reload

Luego abre en el navegador:  http://localhost:8000/docs
(ahi puedes probar todos los endpoints sin escribir nada de codigo)

IMPORTANTE - Seguridad:
    La cadena de conexion a Mongo NUNCA se escribe en este archivo.
    Se lee de una variable de entorno llamada MONGO_URI (mira .env.example).
"""
import requests  # === NUEVO (IA): para llamar a la API del modelo ===
import os
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

# Si existe un archivo .env, carga sus variables (opcional pero recomendado)
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# ---------------------------------------------------------------------------
# 1. CONFIGURACION   👈 AJUSTA ESTOS NOMBRES A TU PROYECTO
# ---------------------------------------------------------------------------
NOMBRE_BD = "proyecto_streaming"            # 👈 tu base de datos en Atlas
NOMBRE_COLECCION = "peliculas"   # 👈 tu coleccion con los datos ya limpios

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
MODELO_IA = "gemini-3.6-flash"   # 👈 usa el mode

# ---------------------------------------------------------------------------
# 2. CONEXION A MONGODB (segura: la clave viene de una variable de entorno)
# ---------------------------------------------------------------------------
MONGO_URI = os.environ.get("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError(
        "Falta la variable de entorno MONGO_URI. "
        "Crea un archivo .env con tu cadena de conexion de Atlas (mira el README)."
    )

cliente = MongoClient(MONGO_URI)
coleccion = cliente[NOMBRE_BD][NOMBRE_COLECCION]

# ---------------------------------------------------------------------------
# 3. LA APLICACION
# ---------------------------------------------------------------------------
app = FastAPI(
    title="API Proyecto Final",
    description="Consulta y administra los datos del proyecto.",
)


def _a_json(doc):
    """El _id de Mongo es un objeto especial; lo pasamos a texto para el JSON."""
    doc["_id"] = str(doc["_id"])
    return doc


@app.get("/")
def inicio():
    """Mensaje de bienvenida y lista de endpoints."""
    return {
        "mensaje": "API del Proyecto Final - ve a /docs para probarla",
        "endpoints": ["GET /datos", "GET /estadisticas", "POST /datos", "/docs"],
    }


# ==== LEER =================================================================
@app.get("/datos")
def listar(campo: Optional[str] = None, valor: Optional[str] = None, limite: int = 20):
    """Lista documentos. Opcionalmente filtra por un campo = valor.

    Ejemplos:
        /datos?limite=50
        /datos?campo=sucursal&valor=Norte
    """
    filtro = {campo: valor} if campo and valor else {}
    documentos = [_a_json(d) for d in coleccion.find(filtro).limit(limite)]
    return {"cantidad": len(documentos), "datos": documentos}


@app.get("/estadisticas")
def estadisticas(agrupar_por: str, sumar: str):
    """Agrupa por un campo y suma otro (agregacion de MongoDB).

    Ejemplo:
        /estadisticas?agrupar_por=sucursal&sumar=total
    """
    pipeline = [
        {
            "$group": {
                "_id": f"${agrupar_por}",
                "suma": {"$sum": f"${sumar}"},
                "conteo": {"$sum": 1},
            }
        },
        {"$sort": {"suma": -1}},
    ]
    grupos = [
        {agrupar_por: r["_id"], "suma": r["suma"], "conteo": r["conteo"]}
        for r in coleccion.aggregate(pipeline)
    ]
    return {"grupos": grupos}


# ==== CREAR ================================================================
# 👈 CAMBIA estos campos por los de TU coleccion (mismos nombres y tipos).
class NuevoRegistro(BaseModel):
    titulo: str
    popularidad: float
    calificacion_promedio: float
    conteo_votos: int
    fecha_lanzamiento: str
    idioma_original: str
 
    model_config = {
        "json_schema_extra": {
            "example": {
                "titulo": "pokemon go",
                "popularidad": 100000000,
                "calificacion_promedio": 10,
                "conteo_votos": 15000,
                "fecha_lanzamiento": "2026-08-20",
                "idioma_original": "en",
        }
    }
}

@app.post("/datos")
def crear(registro: NuevoRegistro):
    """Inserta un nuevo documento en la coleccion."""
    doc = registro.model_dump()
    resultado = coleccion.insert_one(doc)
    return {"mensaje": "Registro creado", "id": str(resultado.inserted_id)}

# === NUEVO (IA): preguntar a los datos en lenguaje natural =================
class Pregunta(BaseModel):
    pregunta: str
 
    model_config = {
        "json_schema_extra": {
            "example": {"pregunta": "¿Cuál sucursal vendió más?"}
        }
    }
 
 
@app.post("/preguntar")
def preguntar(p: Pregunta):
    """Responde una pregunta en lenguaje natural usando los datos de la coleccion."""
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=503, detail="Falta la GEMINI_API_KEY.")
 
    # 1. Una muestra de los datos como contexto para la IA
    muestra = [_a_json(d) for d in coleccion.find().limit(30)]
 
    # 2. El prompt: instrucciones + datos + pregunta
    prompt = (
        "Eres un asistente que responde preguntas sobre estos datos. "
        "Responde en español, breve y claro. Si la respuesta no está en los datos, dilo.\n\n"
        f"DATOS (muestra):\n{muestra}\n\nPREGUNTA: {p.pregunta}"
    )
 
    # 3. Llamamos a la API del modelo (¡es otra API REST!)
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{MODELO_IA}:generateContent?key={GEMINI_API_KEY}"
    )
    try:
        r = requests.post(
            url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=30
        )
        r.raise_for_status()
        data = r.json()
        respuesta = data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Error al llamar al modelo: {e}")
 
    return {"respuesta": respuesta}
# === FIN NUEVO (IA) ========================================================