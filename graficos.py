import streamlit as st
import pandas as pd
import plotly.express as px

def mostrar_graficos():
    st.title("📈 Gráficos Comparativos")

    data = {
        "Tecnología": ["HDD", "SSD", "Cintas", "Nube"],
        "Lectura (MB/s)": [150, 500, 50, 300],
        "Escritura (MB/s)": [120, 480, 40, 250],
        "Fiabilidad": [3, 4, 2, 5],
        "Escalabilidad": [2, 3, 1, 5],
        "Seguridad": [2, 4, 3, 5]
    }
    df = pd.DataFrame(data)

    st.subheader("📊 Velocidad de lectura")
    fig = px.bar(df, x="Tecnología", y="Lectura (MB/s)", color="Tecnología")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🛡️ Radar: Fiabilidad, Escalabilidad y Seguridad")
    radar_df = df.melt(id_vars="Tecnología", value_vars=["Fiabilidad", "Escalabilidad", "Seguridad"])
    fig2 = px.line_polar(radar_df, r="value", theta="variable", color="Tecnología", line_close=True)
    st.plotly_chart(fig2, use_container_width=True)
