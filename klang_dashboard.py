import streamlit as st

st.set_page_config(page_title="K-Lang: Manual de Batalla Interactivo", layout="wide")

st.title("K-Lang: Manual de Batalla Interactivo")
st.header("Selector de Protocolos")

protocolos = {
    "VÍSPERA": {
        "Disparador": "Alerta temprana de amenaza inminente.",
        "Secuencia de acciones": [
            "Activar monitoreo reforzado.",
            "Notificar a los equipos clave.",
            "Preparar recursos de contingencia."
        ]
    },
    "CÓDIGO ROJO": {
        "Disparador": "Confirmación de crisis activa y riesgo extremo.",
        "Secuencia de acciones": [
            "Evacuación inmediata de zonas críticas.",
            "Aislamiento de sistemas sensibles.",
            "Despliegue de equipos de respuesta rápida."
        ]
    },
    "RENACIMIENTO": {
        "Disparador": "Superación de la crisis y transición a recuperación.",
        "Secuencia de acciones": [
            "Evaluar daños y recopilar informes.",
            "Restaurar operaciones esenciales.",
            "Comunicar estado a stakeholders."
        ]
    }
}

seleccion = st.selectbox("Selecciona un protocolo:", list(protocolos.keys()))

ficha = protocolos[seleccion]
st.subheader(f"Ficha Técnica: {seleccion}")
st.markdown(f"**Disparador:** {ficha['Disparador']}")
st.markdown("**Secuencia de acciones:**")
for accion in ficha["Secuencia de acciones"]:
    st.markdown(f"- {accion}")

st.header("Simulador de Protocolos")

# Sliders de sensores en tiempo real
viento = st.slider("Velocidad del Viento (km/h)", min_value=0, max_value=150, value=30)
inundacion = st.slider("Nivel de Inundación (cm)", min_value=0, max_value=200, value=10)

# Lógica para activar protocolo según condiciones
if viento >= 90 or inundacion >= 120:
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
