# 📊 Análisis Técnico de Soluciones de Almacenamiento de Datos

Esta aplicación web interactiva, desarrollada con **Streamlit**, permite realizar un **análisis técnico de diferentes tecnologías de almacenamiento de datos** (HDD, SSD, Cintas y Nube).  
Está lista para desplegarse en **Streamlit Cloud**, sin necesidad de instalaciones locales.

---

## 🚀 Objetivo

- Comparar tecnologías según criterios técnicos: velocidad, capacidad, costo, fiabilidad, consumo energético, seguridad y escalabilidad.  
- Realizar simulaciones de crecimiento de datos.  
- Visualizar gráficos comparativos y diagramas de infraestructura.  
- Analizar riesgos y oportunidades.  
- Generar conclusiones técnicas y exportar informes.

---

## 📁 Estructura del repositorio

/ (raíz)
├─ README.md
├─ requirements.txt
├─ streamlit_app.py
├─ comparacion.py
├─ graficos.py
├─ simulaciones.py
├─ diagramas.py
├─ exportacion.py
└─ data/
├─ ejemplo_comparativa.csv
└─ ejemplo_escenarios.json


---

## 📌 Requisitos (`requirements.txt`)

```txt
streamlit==1.28.0
pandas
numpy
matplotlib
plotly
graphviz
openpyxl
python-docx
reportlab
