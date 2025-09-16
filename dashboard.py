import streamlit as st
from precog_tab import precog_tab
from chronos_tab import chronos_tab
from klang_tab import klang_tab

st.set_page_config(page_title="Dashboard de Mando y Control", layout="wide")
st.title("ChronoLogistics - Dashboard de Mando y Control")

tabs = st.tabs(["Precog: Monitor de Riesgo", "Chronos: Visión 2040", "K-Lang: Manual de Batalla"])
with tabs[0]:
    precog_tab()
with tabs[1]:
    chronos_tab()
with tabs[2]:
    klang_tab()
