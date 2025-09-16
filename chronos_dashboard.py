import streamlit as st

st.set_page_config(page_title="Chronos: Visión Estratégica 2040", layout="wide")

st.title("Chronos: Visión Estratégica 2040")
st.header("Selector de Estrategia")

estrategia = st.radio(
    "Elige la visión estratégica para 2040:",
    ("Fortaleza Verde", "Búnker Tecnológico")
)

if estrategia == "Fortaleza Verde":
    st.success("Has seleccionado: Fortaleza Verde")
    st.write("Visión enfocada en sostenibilidad, resiliencia ecológica y energías limpias.")
else:
    st.success("Has seleccionado: Búnker Tecnológico")
    st.write("Visión centrada en infraestructura avanzada, automatización y protección digital.")

# --- Componente 2: Visualizador de Futuros ---
st.header("Visualizador de Futuros")

if estrategia == "Fortaleza Verde":
    st.image("https://i.imgur.com/2nCt3Sbl.jpg", caption="Fortaleza Verde - Madrid 2040", use_column_width=True)
    st.markdown("""
    **Defensa argumentada:**  
    La Fortaleza Verde representa el compromiso de ChronoLogistics con la sostenibilidad y la resiliencia ecológica.  
    Esta visión apuesta por infraestructuras verdes, energías limpias y una integración total con el entorno natural de Madrid.  
    Garantiza la protección de activos frente a crisis climáticas y posiciona a la empresa como líder en innovación ambiental, atrayendo inversores y generando confianza social.
    """)
else:
    st.image("https://i.imgur.com/8QfQbQk.png", caption="Búnker Tecnológico - Madrid 2040", use_column_width=True)
    st.markdown("""
    **Defensa argumentada:**  
    El Búnker Tecnológico simboliza la máxima seguridad y eficiencia operativa para ChronoLogistics.  
    Esta visión prioriza la automatización, la protección digital y la infraestructura avanzada, asegurando la continuidad del negocio ante cualquier amenaza.  
    Refuerza la posición de la empresa como referente tecnológico en Europa y garantiza la confianza de los inversores en un futuro incierto.
    """)
