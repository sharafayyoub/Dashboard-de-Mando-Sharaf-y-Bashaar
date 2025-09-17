import streamlit as st
from PIL import Image

st.set_page_config(page_title="Chronos: Visión Estratégica 2040", layout="wide")

# Encabezado
st.title("🔮 Chronos: Visión Estratégica 2040")
st.write("Explora nuestras posibles trayectorias de futuro y su impacto en la Junta Directiva, los inversores y la ciudad de Madrid.")

# Componente 1 - Selector de Estrategia
estrategia = st.radio(
    "Elige la visión estratégica para 2040:",
    ("Fortaleza Verde", "Búnker Tecnológico")
)

# Componente 2 - Visualizador de Futuros
st.subheader("Visualizador de Futuros")

col1, col2 = st.columns([1, 2])

if estrategia == "Fortaleza Verde":
    # Imagen generada (puedes reemplazar la ruta por tu propia imagen local)
    with col1:
        img_verde = Image.new("RGB", (400, 250), color=(34, 139, 34))  # Verde bosque
        st.image(img_verde, caption="Fortaleza Verde - Madrid 2040", use_column_width=True)
    with col2:
        st.markdown("""
        **Defensa argumentada:**  
        La Fortaleza Verde representa el compromiso de ChronoLogistics con la sostenibilidad y la resiliencia ecológica.  
        Esta visión apuesta por infraestructuras verdes, energías limpias y una integración total con el entorno natural de Madrid.  
        Garantiza la protección de activos frente a crisis climáticas y posiciona a la empresa como líder en innovación ambiental, atrayendo inversores y generando confianza social.
        """)
elif estrategia == "Búnker Tecnológico":
    with col1:
        img_bunker = Image.new("RGB", (400, 250), color=(70, 130, 180))  # Azul acero
        st.image(img_bunker, caption="Búnker Tecnológico - Madrid 2040", use_column_width=True)
    with col2:
        st.markdown("""
        **Defensa argumentada:**  
        El Búnker Tecnológico simboliza la máxima seguridad y eficiencia operativa para ChronoLogistics.  
        Esta visión prioriza la automatización, la protección digital y la infraestructura avanzada, asegurando la continuidad del negocio ante cualquier amenaza.  
        Refuerza la posición de la empresa como referente tecnológico en Europa y garantiza la confianza de los inversores en un futuro incierto.
        """)
