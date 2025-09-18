# 📊 Informe Técnico – Soluciones de Almacenamiento de Datos

## 1. Introducción

Este informe presenta un **análisis técnico de diferentes tecnologías de almacenamiento de datos** (HDD, SSD, Cintas y Nube) para empresas, considerando criterios clave como velocidad, capacidad, costo, fiabilidad, consumo energético, seguridad y escalabilidad.

El objetivo es **evaluar y recomendar la mejor solución** según las necesidades de almacenamiento de datos de cada escenario empresarial.

---

## 2. Escenario de la Empresa

| Empresa       | Sector       | Volumen de datos (TB) | Presupuesto anual (USD) |
|---------------|-------------|----------------------|------------------------|
| Empresa A     | Tecnología  | 50                   | 50,000                 |
| Empresa B     | Salud       | 100                  | 120,000                |
| Empresa C     | Educación   | 20                   | 20,000                 |

> Los datos son ejemplos cargados desde `data/ejemplo_escenarios.json`.

---

## 3. Comparación de Tecnologías

| Tecnología | Velocidad (MB/s) | Capacidad (TB) | Costo USD/GB | Fiabilidad (MTBF) | Consumo (W) | Seguridad | Escalabilidad |
|------------|-----------------|----------------|--------------|-----------------|-------------|-----------|---------------|
| HDD        | 150             | 10             | 0.03         | 1,200,000       | 6           | Baja      | Media         |
| SSD        | 500             | 4              | 0.10         | 2,000,000       | 3           | Alta      | Media         |
| Cintas     | 50              | 1000           | 0.01         | 3,000,000       | 2           | Media     | Baja          |
| Nube       | 300             | Ilimitada      | 0.05         | 5,000,000       | Variable    | Alta      | Alta          |

> Los datos son cargados desde `data/ejemplo_comparativa.csv`.

---

## 4. Análisis Gráfico

- **Barras**: comparación de velocidad de lectura y escritura.  
- **Radar**: fiabilidad, escalabilidad y seguridad.  
- **Líneas**: simulación de crecimiento de datos a lo largo de los años.

> Estos gráficos se generan dinámicamente en la app Streamlit.

---

## 5. Simulación de Crecimiento de Datos

- Volumen inicial: 50 TB  
- Tasa de crecimiento anual: 50%  
- Periodo: 5 años  

| Año | Volumen (TB) |
|-----|--------------|
| 0   | 50           |
| 1   | 75           |
| 2   | 112.5        |
| 3   | 168.8        |
| 4   | 253.1        |
| 5   | 379.7        |

> Esta simulación permite evaluar tiempos de respuesta y planificación de infraestructura.

---

## 6. Diagramas de Infraestructura

- Servidor local conectado a HDD/SSD.  
- Backup en cintas.  
- Integración con Nube para escalabilidad y redundancia.  

> Diagramas generados con Graphviz en la app.

---

## 7. Riesgos y Oportunidades

**Riesgos**:

| Riesgo                         | Mitigación                   |
|--------------------------------|------------------------------|
| Alto costo SSD                  | Solución híbrida HDD+SSD     |
| Dependencia de conectividad nube| Redundancia ISP              |

**Oportunidades**:

- Escalabilidad en la nube.  
- Reducción de costos operativos.  
- Continuidad del negocio garantizada.

---

## 8. Conclusiones Técnicas

- La **mejor solución recomendada** es **híbrida SSD + Nube**:  
  - SSD para velocidad y fiabilidad.  
  - Nube para escalabilidad y respaldo.  
- La planificación de crecimiento de datos permite anticipar inversiones y dimensionar correctamente la infraestructura.

---

## 9. Referencias

- Datos de ejemplo generados en la app Streamlit.  
- Librerías usadas: `pandas`, `numpy`, `matplotlib`, `plotly`, `graphviz`.  
- Informe generado como `docs/informe.md` para documentación interna y GitHub.
