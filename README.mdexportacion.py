import streamlit as st

def mostrar_conclusiones():
    st.title("✅ Conclusiones Técnicas")

    st.write("""
    En base al análisis, una **solución híbrida** (SSD para velocidad + Nube para escalabilidad y respaldo)
    es generalmente la mejor opción.
    """)

    st.download_button(
        "📥 Descargar informe (texto)",
        "Conclusión: la mejor opción es una solución híbrida SSD + Nube.".encode("utf-8"),
        "informe.txt",
        "text/plain"
    )
