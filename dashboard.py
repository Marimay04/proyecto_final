"""
Dashboard del Proyecto Final - Programacion Aplicada
=====================================================
Frontend (Streamlit) que consume la API (api.py): lista, filtra, grafica
y permite agregar registros nuevos.

Como ejecutar (en OTRA terminal, con la API ya corriendo):
    streamlit run dashboard.py

La API debe estar activa en http://localhost:8000
"""

import pandas as pd
import requests
import streamlit as st
import base64
from pathlib import Path

import os

API = os.getenv("API_URL", "http://127.0.0.1:8000")

# =====================================================
# CARGAR FONDO CINEMATOGRÁFICO
# =====================================================

# Buscar la imagen dentro de la carpeta assets
ruta_fondo = Path(__file__).parent / "assets" / "fondo_cine.png"

# Leer la imagen y convertirla para utilizarla en CSS
with open(ruta_fondo, "rb") as imagen:
    fondo_base64 = base64.b64encode(imagen.read()).decode()
# =====================================================
# DISEÑO CINEMATOGRÁFICO - CINEMA ANALYTICS
# =====================================================

st.set_page_config(
    page_title="Cinema Analytics",
    page_icon="🎬",
    layout="wide"
)

# Personalización visual de la aplicación
# =====================================================
# DISEÑO CINEMATOGRÁFICO - CINEMA ANALYTICS
# =====================================================

css = """
<style>

/* Fondo cinematográfico */
.stApp {
    background-image:
        linear-gradient(
            rgba(0, 0, 0, 0.65),
            rgba(0, 0, 0, 0.80)
        ),
        url("data:image/png;base64,FONDO_IMAGEN");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
    color: #F5F0E8;
}

/* Barra lateral */
section[data-testid="stSidebar"] {
    background-color: #15120F;
    border-right: 1px solid #B89646;
}

/* Encabezados */
h1, h2, h3 {
    color: #E7C779 !important;
    font-family: Georgia, serif !important;
}

/* Indicadores */
div[data-testid="stMetric"] {
    background: rgba(28, 24, 20, 0.92);
    border: 1px solid #B89646;
    border-radius: 14px;
    padding: 20px;
}

/* Botones */
.stButton > button,
.stFormSubmitButton > button {
    background-color: #B89646;
    color: #101010;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background-color: #E7C779;
    color: #101010;
}

/* Separadores */
hr {
    border-color: #B89646;
}

</style>
"""

# Insertar la imagen cinematográfica en el CSS
css = css.replace("FONDO_IMAGEN", fondo_base64)

# Aplicar el diseño
st.markdown(css, unsafe_allow_html=True)

# Encabezado principal
st.title("🎬 CINEMA ANALYTICS")
st.markdown(
    "#### ✨ Explora, descubre y analiza el mundo del cine"
)

st.divider()

# --- Funciones que hablan con la API ---------------------------------------
@st.cache_data(ttl=30)
def listar(campo=None, valor=None, limite=200):
    params = {"limite": limite}
    if campo and valor:
        params.update({"campo": campo, "valor": valor})
    r = requests.get(f"{API}/datos", params=params, timeout=10)
    r.raise_for_status()
    return pd.DataFrame(r.json()["datos"])


@st.cache_data(ttl=30)
def estadisticas(agrupar_por, sumar):
    r = requests.get(
        f"{API}/estadisticas",
        params={"agrupar_por": agrupar_por, "sumar": sumar},
        timeout=10,
    )
    r.raise_for_status()
    return pd.DataFrame(r.json()["grupos"])


# --- Verifica que la API este arriba ---------------------------------------
try:
    df = listar()
except Exception:
    st.error(
        f"No pude conectarme a la API en {API}. "
        f"Revisa que este corriendo:  uvicorn api:app --reload"
    )
    st.stop()

if df.empty:
    st.warning("La coleccion esta vacia.")
    st.stop()

columnas = [c for c in df.columns if c != "_id"]
numericas = df.select_dtypes("number").columns.tolist()

# --- Filtro en la barra lateral --------------------------------------------
st.sidebar.header("Filtros")
campo = st.sidebar.selectbox("Filtrar por campo", ["(todos)"] + columnas)
if campo != "(todos)":
    opciones = sorted(df[campo].dropna().astype(str).unique())
    valor = st.sidebar.selectbox("Valor", opciones)
    df = listar(campo=campo, valor=valor)

# --- Metricas ---------------------------------------------------------------
c1, c2 = st.columns(2)
c1.metric("Registros", len(df))
if numericas:
    # 👈 elige una columna con sentido (p. ej. 'total', no 'venta_id')
    col_metrica = numericas[-1]
    c2.metric(f"Suma de {col_metrica}", int(df[col_metrica].sum()))

# --- Estadisticas (usa la agregacion de la API) ----------------------------
st.subheader("Estadisticas")
categoricas = [c for c in columnas if c not in numericas]
if categoricas and numericas:
    a1, a2 = st.columns(2)
    agrupar = a1.selectbox("Agrupar por", categoricas)
    sumar = a2.selectbox("Sumar", numericas)
    if st.button("Calcular"):
        g = estadisticas(agrupar, sumar)
        st.bar_chart(g.set_index(agrupar)["suma"])
        st.dataframe(g, use_container_width=True)

# --- Tabla de datos ---------------------------------------------------------
st.subheader("Datos")
st.dataframe(df, use_container_width=True)

# --- Agregar un registro (POST a la API) -----------------------------------
# 👈 CAMBIA estos campos por los de TU coleccion (mismos nombres que en la API).
# =====================================================
# FORMULARIO PARA REGISTRAR PELÍCULAS
# =====================================================

st.subheader("🎬 Agregar nueva película")

with st.form("nueva_pelicula"):

    titulo = st.text_input("Título de la película")

    popularidad = st.number_input(
        "Popularidad",
        min_value=0.0,
        step=1.0
    )

    calificacion = st.number_input(
        "Calificación promedio",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    votos = st.number_input(
        "Cantidad de votos",
        min_value=0,
        step=1
    )

    fecha = st.date_input("Fecha de lanzamiento")

    idioma = st.text_input("Idioma original (ejemplo: es, en, fr)")

    enviar = st.form_submit_button("🎬 Guardar película")

if enviar:

    if not titulo.strip():
        st.warning("Debes escribir el título de la película.")

    else:
        payload = {
            "titulo": titulo,
            "popularidad": float(popularidad),
            "calificacion_promedio": int(calificacion),
            "conteo_votos": int(votos),
            "fecha_lanzamiento": fecha.isoformat(),
            "idioma_original": idioma
        }

        try:
            respuesta = requests.post(
                f"{API}/datos",
                json=payload,
                timeout=10
            )

            if respuesta.ok:
                st.success("🎉 ¡Película registrada correctamente!")
                st.cache_data.clear()

            else:
                st.error(
                    f"No se pudo registrar la película: {respuesta.text}"
                )

        except requests.exceptions.RequestException as error:
            st.error(f"Error de conexión con la API: {error}")

# === NUEVO (IA): pregúntale a tus datos ====================================
st.subheader("🤖 Pregúntale a tus datos")
pregunta = st.text_input(
    "🎬 Pregúntale a nuestra IA sobre películas",
    placeholder="Ejemplo: ¿Qué películas tienen mayor popularidad?"
)
if st.button("Preguntar") and pregunta:
    with st.spinner("Pensando..."):
        r = requests.post(f"{API}/preguntar", json={"pregunta": pregunta}, timeout=60)
    if r.ok:
        st.success(r.json()["respuesta"])
    else:
        st.error(f"Error: {r.text}")
# === FIN NUEVO (IA) ========================================================