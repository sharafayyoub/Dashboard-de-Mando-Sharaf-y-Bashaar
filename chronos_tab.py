import streamlit as st

def chronos_tab():
    st.header("Chronos: Visión Estratégica 2040")
    estrategia = st.selectbox("Selecciona Estrategia", ["Fortaleza Verde", "Búnker Tecnológico"])
    if estrategia == "Fortaleza Verde":
        st.image("assets/fortaleza_verde.png", caption="Fortaleza Verde", use_column_width=True)
        st.info("Defensa: La Fortaleza Verde apuesta por la resiliencia ecológica y la integración urbana sostenible para proteger Madrid a largo plazo.")
    else:
        st.image("assets/bunker_tecnologico.png", caption="Búnker Tecnológico", use_column_width=True)
        st.info("Defensa: El Búnker Tecnológico prioriza la seguridad y la innovación, creando un núcleo hiperprotegido y tecnológicamente avanzado.")
