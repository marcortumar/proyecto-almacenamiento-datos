import streamlit as st
import graphviz

def mostrar_diagramas():
    st.title("🖇️ Diagrama de Infraestructura")
    dot = graphviz.Digraph()
    dot.node("Servidor", "Servidor Local")
    dot.node("Disco", "HDD/SSD")
    dot.node("Backup", "Cintas")
    dot.node("Cloud", "Nube")
    dot.edges([("Servidor", "Disco"), ("Servidor", "Backup"), ("Servidor", "Cloud")])
    st.graphviz_chart(dot)
