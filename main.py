import streamlit as st

st.set_page_config(page_title="Dashboard de Mando y Control", layout="wide")

st.title("Dashboard de Mando y Control - ChronoLogistics")

st.info("Accede a la interfaz en: http://localhost:8501")

tab = st.sidebar.selectbox(
    "Selecciona una pestaña:",
    ["Precog: Monitor de Riesgo Táctico", "Chronos: Visión Estratégica 2040", "K-Lang: Manual de Batalla Interactivo"]
)

if tab == "Precog: Monitor de Riesgo Táctico":
    import precog_dashboard
elif tab == "Chronos: Visión Estratégica 2040":
    import chronos_dashboard
elif tab == "K-Lang: Manual de Batalla Interactivo":
    import klang_dashboard

if __name__ == "__main__":
    st.warning(
        "Para ver la interfaz web, ejecuta este archivo con el comando:\n\n"
        "`streamlit run main.py`\n\n"
        "Luego abre el navegador en http://localhost:8501"
    )