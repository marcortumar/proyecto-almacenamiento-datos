import streamlit as st
import pandas as pd

def mostrar_comparacion():
    st.title("📋 Comparación de Tecnologías de Almacenamiento")
    data = {
        "Tecnología": ["HDD", "SSD", "Cintas", "Nube"],
        "Velocidad (MB/s)": [150, 500, 50, 300],
        "Capacidad (TB)": [10, 4, 1000, "Ilimitada"],
        "Costo USD/GB": [0.03, 0.10, 0.01, 0.05],
        "Fiabilidad (MTBF)": [1_200_000, 2_000_000, 3_000_000, 5_000_000],
        "Consumo (W)": [6, 3, 2, "Variable"],
        "Seguridad": ["Baja", "Alta", "Media", "Alta"],
        "Escalabilidad": ["Media", "Media", "Baja", "Alta"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    st.download_button(
        "📥 Descargar CSV",
        df.to_csv(index=False).encode("utf-8"),
        "comparacion.csv",
        "text/csv"
    )
