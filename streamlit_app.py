import streamlit as st
import pandas as pd

# Importar módulos (iremos creando estos archivos)
import comparacion
import graficos
import simulaciones
import diagramas
import exportacion

st.set_page_config(page_title="Análisis de Almacenamiento de Datos", layout="wide")

# Sidebar para navegación
menu = st.sidebar.radio(
    "📌 Navegación",
    ["Contexto", "Comparación", "Gráficos", "Simulaciones", "Diagramas", "Riesgos", "Conclusiones"]
)

if menu == "Contexto":
    st.title("📊 Contexto de la Empresa")
    st.write("Aquí puedes ingresar o editar el escenario de tu empresa.")
    with st.form("contexto_form"):
        nombre = st.text_input("Nombre de la empresa", "Mi Empresa")
        sector = st.text_input("Sector", "Tecnología")
        volumen = st.number_input("Volumen de datos inicial (TB)", 1, 1000, 50)
        presupuesto = st.number_input("Presupuesto anual (USD)", 1000, 1000000, 50000)
        submit = st.form_submit_button("Guardar escenario")
    if submit:
        st.success(f"✅ Escenario guardado para {nombre} en el sector {sector} con {volumen} TB.")

elif menu == "Comparación":
    comparacion.mostrar_comparacion()

elif menu == "Gráficos":
    graficos.mostrar_graficos()

elif menu == "Simulaciones":
    simulaciones.mostrar_simulaciones()

elif menu == "Diagramas":
    diagramas.mostrar_diagramas()

elif menu == "Riesgos":
    st.title("⚠️ Riesgos y Oportunidades")
    st.write("Matriz editable de riesgos vs mitigaciones (pendiente implementar).")

elif menu == "Conclusiones":
    exportacion.mostrar_conclusiones()
