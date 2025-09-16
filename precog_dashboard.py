import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Precog: Monitor de Riesgo Táctico", layout="wide")

st.title("Precog: Monitor de Riesgo Táctico")
st.header("Mapa de Calor de Riesgo")

# Simulación de datos de clústeres
np.random.seed(42)
clusters = np.random.rand(10, 2) * 100
risk_scores = np.random.rand(10) * 100

# Selecciona los 3 clústeres más críticos
critical_indices = np.argsort(risk_scores)[-3:]
critical_clusters = clusters[critical_indices]

fig, ax = plt.subplots(figsize=(8, 6))
# Mapa de calor (scatter con color por riesgo)
sc = ax.scatter(clusters[:, 0], clusters[:, 1], c=risk_scores, cmap='hot', s=200, alpha=0.7)
plt.colorbar(sc, ax=ax, label='Nivel de Riesgo')

# Marca el "Triángulo del Peligro"
triangle = plt.Polygon(critical_clusters, closed=True, fill=None, edgecolor='cyan', linewidth=2, label='Triángulo del Peligro')
ax.add_patch(triangle)
ax.scatter(critical_clusters[:, 0], critical_clusters[:, 1], color='cyan', s=300, edgecolors='black', label='Clúster Crítico')

for i, (x, y) in enumerate(clusters):
    ax.text(x, y, f"C{i+1}", fontsize=9, ha='center', va='center', color='white')

ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Mapa de Clústeres de Riesgo")

st.pyplot(fig)

# --- Componente 2: Simulador de Riesgo Interactivo ---
st.header("Simulador de Riesgo Interactivo")

# Sliders para variables de entrada
velocidad_media = st.slider("Velocidad Media (km/h)", min_value=0, max_value=200, value=80)
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
