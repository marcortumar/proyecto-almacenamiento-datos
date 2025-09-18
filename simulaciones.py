import streamlit as st
import pandas as pd
import plotly.express as px

def mostrar_simulaciones():
    st.title("🔮 Simulación de Crecimiento de Datos")

    volumen_inicial = st.number_input("Volumen inicial (TB)", 1, 1000, 100)
    tasa_crecimiento = st.slider("Crecimiento anual (%)", 0, 200, 50)
    anos = st.slider("Años a simular", 1, 10, 5)

    datos = []
    for year in range(anos + 1):
        volumen = volumen_inicial * ((1 + tasa_crecimiento / 100) ** year)
        datos.append({"Año": year, "Volumen (TB)": volumen})

    df = pd.DataFrame(datos)
    st.dataframe(df)

    fig = px.line(df, x="Año", y="Volumen (TB)", markers=True)
    st.plotly_chart(fig, use_container_width=True)
