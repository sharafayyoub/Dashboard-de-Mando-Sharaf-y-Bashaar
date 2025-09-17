import streamlit as st
from protocolos import PROTOCOLOS, detectar_protocolo

st.set_page_config(page_title="K-Lang: Manual de Batalla Interactivo", layout="wide")

# Encabezado
st.title("⚔️ K-Lang: Manual de Batalla Interactivo")
st.write("Guía crítica y dinámica para activar protocolos en tiempo real durante la crisis.")

# Componente 1 - Selector de Protocolos
st.subheader("Selector de Protocolos")

seleccion = st.radio("Selecciona un protocolo:", list(PROTOCOLOS.keys()))

ficha = PROTOCOLOS[seleccion]
st.markdown(
    f"""
    <div style='border:2px solid #888; border-radius:10px; padding:16px; margin-bottom:16px; background-color:#f9f9f9;'>
        <h3 style='margin-top:0;'>{seleccion}</h3>
        <b>Disparador:</b> {ficha['disparador']}<br>
        <b>Secuencia de acciones:</b>
        <ul>
            {"".join([f"<li>{accion}</li>" for accion in ficha['acciones'].split(", ")])}
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Componente 2 - Simulador de Protocolos
st.subheader("Simulador de Protocolos")

viento = st.slider("Velocidad del viento (km/h)", min_value=0, max_value=150, value=30)
inundacion = st.slider("Nivel de inundación (cm)", min_value=0, max_value=200, value=10)

protocolo_activo = detectar_protocolo(viento, inundacion)

if "CÓDIGO ROJO" in protocolo_activo:
    color = "red"
    icon = "🚨"
elif "VÍSPERA" in protocolo_activo:
    color = "orange"
    icon = "⚠️"
else:
    color = "green"
    icon = "✅"

st.markdown(
    f"<div style='text-align:center; margin-top:24px;'><h2 style='color:{color};'>{icon} PROTOCOLO ACTIVO: {protocolo_activo}</h2></div>",
    unsafe_allow_html=True
)
    protocolo_activo = "CÓDIGO ROJO: TITÁN"
    color = "red"
elif viento >= 50 or inundacion >= 60:
    protocolo_activo = "VÍSPERA"
    color = "orange"
else:
    protocolo_activo = "RENACIMIENTO"
    color = "green"

st.markdown(
    f"<h2 style='color:{color};'>PROTOCOLO ACTIVO: {protocolo_activo}</h2>",
    unsafe_allow_html=True
)
