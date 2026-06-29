import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Predictor Lúdico Mundial 2026", layout="centered")
st.title("⚽ Predictor Lúdico Mundial 2026")
st.caption("Proyecto demostrativo de Data Science: ponderaciones, intuición y pronóstico de partidos.")
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
fuerza = pd.read_csv(DATA_DIR / "data_fuerza_equipos.csv")
strength_dict = dict(zip(fuerza["equipo"], fuerza["fuerza_base"]))
equipos = sorted(strength_dict.keys())
st.info("Este predictor es lúdico y demostrativo. No es un modelo estadístico oficial ni una recomendación de apuestas.")

def probabilidad_desde_fuerza(f1, f2):
    diff = f1 - f2
    p1 = 1 / (1 + np.exp(-diff / 10))
    return round(p1 * 100, 1), round((1-p1) * 100, 1)

def marcador_desde_probabilidad(p1, p2):
    diff = abs(p1 - p2)
    if diff < 8: return 1, 1
    if diff < 18: return (2,1) if p1 > p2 else (1,2)
    if diff < 30: return (2,0) if p1 > p2 else (0,2)
    if diff < 45: return (3,0) if p1 > p2 else (0,3)
    return (4,0) if p1 > p2 else (0,4)

col1, col2 = st.columns(2)
with col1:
    equipo1 = st.selectbox("Equipo 1", equipos, index=equipos.index("Brasil") if "Brasil" in equipos else 0)
    ajuste1 = st.slider("Ajuste intuición equipo 1", -15, 15, 0)
with col2:
    equipo2 = st.selectbox("Equipo 2", equipos, index=equipos.index("Japón") if "Japón" in equipos else 1)
    ajuste2 = st.slider("Ajuste intuición equipo 2", -15, 15, 0)

f1 = strength_dict[equipo1] + ajuste1
f2 = strength_dict[equipo2] + ajuste2
p1, p2 = probabilidad_desde_fuerza(f1, f2)
g1, g2 = marcador_desde_probabilidad(p1, p2)
st.subheader("Resultado estimado")
st.write(f"**{equipo1}: {p1}%**")
st.write(f"**{equipo2}: {p2}%**")
st.success(f"Pronóstico: {equipo1} {g1} - {g2} {equipo2}")
st.subheader("Fuerza utilizada")
st.dataframe(pd.DataFrame({"Equipo":[equipo1,equipo2],"Fuerza base":[strength_dict[equipo1],strength_dict[equipo2]],"Ajuste usuario":[ajuste1,ajuste2],"Fuerza final":[f1,f2]}))
