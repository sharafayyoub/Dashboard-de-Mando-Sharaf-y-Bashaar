import streamlit as st
from precog import predecir_riesgo

def precog_tab():
    st.header("Precog: Monitor de Riesgo Táctico")
    st.subheader("Mapa de Calor de Riesgo")
    st.image("assets/mapa_clusters.png", caption="Triángulo del Peligro", use_column_width=True)

    st.subheader("Simulador de Riesgo Interactivo")
    velocidad = st.slider("Velocidad Media (km/h)", 0, 150, 60)
    lluvia = st.slider("Intensidad de Lluvia (mm/h)", 0, 100, 20)
    riesgo, nivel = predecir_riesgo(velocidad, lluvia)
    st.metric("Nivel de Riesgo en Cascada", f"{riesgo}% - {nivel}")

    # Indicador de color según nivel de riesgo
    if nivel == "ALTO":
        st.error("¡Riesgo ALTO! Actuar inmediatamente.")
    elif nivel == "MEDIO":
        st.warning("Riesgo MEDIO. Mantener vigilancia.")
    else:
        st.success("Riesgo BAJO. Situación controlada.")
