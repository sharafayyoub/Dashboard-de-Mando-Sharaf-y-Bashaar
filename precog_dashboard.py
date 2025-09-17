import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Precog: Monitor de Riesgo Táctico", layout="wide")

# Encabezado
st.title("🛰️ Precog: Monitor de Riesgo Táctico")
st.write("Visión instantánea de los clústeres críticos y simulación de riesgo en tiempo real.")

# Mapa de Calor de Riesgo
st.subheader("Mapa de Calor de Riesgo")
st.image("https://i.imgur.com/8QfQbQk.png", caption="Clústeres de riesgo con Triángulo del Peligro", use_column_width=True)

# Simulador de Riesgo Interactivo
st.subheader("Simulador de Riesgo")

velocidad_media = st.slider("Velocidad Media (km/h)", min_value=0, max_value=200, value=80)
intensidad_lluvia = st.slider("Intensidad de Lluvia (mm/h)", min_value=0, max_value=100, value=20)

def predecir_riesgo(velocidad, lluvia):
    riesgo = 0.4 * (velocidad / 200) + 0.6 * (lluvia / 100)
    riesgo_pct = int(riesgo * 100)
    if riesgo_pct >= 70:
        nivel = "ALTO"
        color = "red"
        emoji = "🚨"
    elif riesgo_pct >= 40:
        nivel = "MEDIO"
        color = "orange"
        emoji = "⚠️"
    else:
        nivel = "BAJO"
        color = "green"
        emoji = "✅"
    return riesgo_pct, nivel, color, emoji

riesgo_pct, nivel, color, emoji = predecir_riesgo(velocidad_media, intensidad_lluvia)

st.markdown(
    f"<h2 style='color:{color};'>{emoji} Nivel de Riesgo en Cascada: {riesgo_pct}% - {nivel}</h2>",
    unsafe_allow_html=True
)
intensidad_lluvia = st.slider("Intensidad de Lluvia (mm/h)", min_value=0, max_value=100, value=20)

# Función de predicción de riesgo
def predecir_riesgo(velocidad, lluvia):
    # Ejemplo simple: riesgo aumenta con velocidad y lluvia
    riesgo = 0.4 * (velocidad / 200) + 0.6 * (lluvia / 100)
    riesgo_pct = int(riesgo * 100)
    if riesgo_pct >= 70:
        nivel = "ALTO"
    elif riesgo_pct >= 40:
        nivel = "MEDIO"
    else:
        nivel = "BAJO"
    return riesgo_pct, nivel

riesgo_pct, nivel = predecir_riesgo(velocidad_media, intensidad_lluvia)

st.subheader("Nivel de Riesgo en Cascada")
st.markdown(f"<h2 style='color: red;'>{riesgo_pct}% - {nivel}</h2>", unsafe_allow_html=True)
