# Proyecto 10: Predictor Lúdico Mundial 2026

Proyecto demostrativo de Data Science aplicado al fútbol.

## Objetivo

Crear un predictor simple de partidos del Mundial 2026 usando ponderaciones heurísticas, predicciones de marcador, comparación contra resultados reales parciales, métricas de efectividad y ajuste de intuición del usuario.

## Importante

Este proyecto es lúdico y demostrativo. No corresponde a un modelo estadístico oficial ni a una recomendación de apuestas.

## Archivos

- `Proyecto_10_Predictor_Ludico_Mundial_2026.ipynb`: notebook principal.
- `app_streamlit.py`: app interactiva.
- `data_fuerza_equipos.csv`: fuerza base por selección.
- `data_predicciones_fase_grupos.csv`: predicciones iniciales.
- `data_resultados_reales_parciales.csv`: resultados reales usados para evaluar.
- `data_proyeccion_eliminatoria.csv`: proyección eliminatoria.
- `requirements.txt`: dependencias.

## Cómo ejecutar

```bash
pip install -r requirements.txt
jupyter notebook Proyecto_07_Predictor_Ludico_Mundial_2026.ipynb
```

Para ejecutar la app:

```bash
streamlit run app_streamlit.py
```

## Métricas iniciales

Con los partidos evaluados en la conversación:

- Acierto de ganador/resultado: alrededor de 74%.
- Acierto de marcador exacto: alrededor de 21%.
- Acierto de total de goles: alrededor de 26%.

## Próximas mejoras

- Incorporar ranking FIFA o Elo.
- Agregar goles a favor y en contra.
- Agregar forma reciente.
- Agregar simulación de torneo completo.
- Publicar versión Streamlit.
- Crear visualizaciones para LinkedIn.
