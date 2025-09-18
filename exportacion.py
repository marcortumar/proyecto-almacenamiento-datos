import streamlit as st

def mostrar_conclusiones():
    st.title("✅ Conclusiones Técnicas")
    st.write("""
    En base al análisis, la mejor opción suele ser una **solución híbrida SSD + Nube**:
    - SSD: velocidad y fiabilidad.
    - Nube: escalabilidad y respaldo.
    """)
    st.download_button(
        "📥 Descargar informe (texto)",
        "Conclusión: solución híbrida SSD + Nube.".encode("utf-8"),
        "informe.txt",
        "text/plain"
    )
