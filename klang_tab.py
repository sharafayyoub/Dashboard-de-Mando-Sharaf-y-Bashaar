import streamlit as st
from protocolos import PROTOCOLOS, detectar_protocolo

def klang_tab():
    st.header("K-Lang: Manual de Batalla Interactivo")
    st.subheader("Selector de Protocolos")
    protocolo = st.selectbox("Selecciona Protocolo", list(PROTOCOLOS.keys()))
    ficha = PROTOCOLOS[protocolo]
    st.write(f"**Disparador:** {ficha['disparador']}")
    st.write(f"**Secuencia de acciones:** {ficha['acciones']}")

    st.subheader("Simulador de Protocolos")
    viento = st.slider("Velocidad del Viento (km/h)", 0, 150, 30)
    inundacion = st.slider("Nivel de Inundación (cm)", 0, 200, 10)
    protocolo_activo = detectar_protocolo(viento, inundacion)
    st.markdown(f"### :red[PROTOCOLO ACTIVO: {protocolo_activo}]")
