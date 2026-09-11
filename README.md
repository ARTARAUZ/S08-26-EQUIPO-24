# PredictiveMaintenance

**Código:** S08-26-EQUIPO-24

**Estado:** En desarrollo — Fase: Discovery / Project Setup

---

## ¿Qué es?

PredictiveMaintenance es una solución de mantenimiento predictivo que permite a un responsable de mantenimiento pasar de la reactividad a la proactividad.

## Objetivo

Construir una solución que permita responder:

- ¿Qué máquinas están mostrando señales de deterioro?
- Cuáles tienen mayor riesgo de fallar?
- Qué podemos hacer ahora para evitar una parada?

## Criterio de éxito

El sistema debe permitir que un responsable de mantenimiento, sin revisar manualmente grandes cantidades de sensores o múltiples registros históricos, pueda:

1. IDENTIFICAR qué máquinas presentan mayor riesgo de falla.
2. COMPRENDER qué señales o variables justifican ese riesgo.
3. PRIORIZAR qué máquina debería atenderse primero.

## Alcance MVP

### MUST HAVE
- Dataset seleccionado y justificado ✅ **Azure PdM**
- Limpieza y tratamiento de datos
- EDA
- Modelo ML con baseline, predicción de riesgo y explicabilidad
- Dashboard con resumen, ranking de riesgo, prioridad y detalle de máquina
- Integración, pruebas y deploy

### SHOULD HAVE
- SHAP o explicación avanzada
- Filtros avanzados
- Comparación de máquinas
- Exportación
- Recomendación preventiva específica

### COULD HAVE
- RUL
- Horas hasta falla
- Alertas
- API independiente
- Base de datos
- Autenticación
- Docker

## Flujo de solución

Dataset → Limpieza → Feature Engineering → Modelo ML → Artefacto → Streamlit → Dashboard → Decisión

## Arquitectura inicial

- Dataset en data/ (Azure PdM seleccionado)
- Limpieza y feature engineering en src/
- Modelo serializado en models/
- Dashboard en dashboard/app.py (Streamlit)
- FastAPI: opcional, no es dependencia del MVP

## Stack tecnológico

- Python
- Pandas, NumPy
- Scikit-learn
- Joblib
- Plotly / Matplotlib / Seaborn
- Streamlit
- Jupyter / Google Colab
- Git, GitHub
- Deploy: Streamlit Community Cloud

## Roles del equipo

### Data Scientists (3)
- Luis Fernando Tapia — Modelado, baseline, modelos, métricas
- Oscar Arauz — Feature Engineering, transformaciones, variables temporales
- Lennin Billey Temoche Gómez — Pipeline ML, validación, serialización, integración

### Data Analysts (4)
- Lorena Urrutia — Product & Business, historias de usuario, KPIs, criticidad
- Alexander Tovar Morcillo — Data Quality, profiling, nulos, outliers
- Héctor García — EDA, visualización, tendencias
- Carlos Vega — Dashboard, UX, Streamlit

### Software Engineer
- Albeiro Burbano — Arquitectura, GitHub, integración, deploy, CI

## Estructura del repositorio

data/ — datasets (raw y processed)
notebooks/ — exploración y análisis
src/ — código de producción (data, features, models, utils)
models/ — artefactos del modelo
dashboard/ — aplicación Streamlit
tests/ — pruebas
docs/ — documentación del proyecto
.github/ — templates y workflows CI

## Estado actual

El repositorio se encuentra en **fase de preparación / discovery**.

**Dataset seleccionado:** Microsoft Azure Predictive Maintenance (Azure PdM) ✅
- Evaluación completada con matriz de 20 criterios ponderados.
- Análisis automatizado en `notebooks/01_data_exploration.ipynb` (sección 10).
- Documentación en `docs/dataset_selection.md` y `docs/decisions.md` (DEC-009).

**Próximo:** Data Engineering (unir 5 tablas) → Feature Engineering temporal → Modelado.

## Roadmap de 4 semanas

- Semana 1: Discovery + Dataset + Data Foundation + EDA inicial + dashboard skeleton
- Semana 2: ML + integración inicial
- Semana 3: Producto (ranking, criticidad, explicabilidad)
- Semana 4: Testing + Deploy + Demo

Ver docs/roadmap.md para el calendario detallado.

## Backlog

Ver docs/backlog.md para el backlog completo organizado por épicas.

## Reglas de desarrollo

- Crear branch feature/<id>-descripcion, fix/<id>- descripcion, docs/< descripcion>
- Commits con prefijo: feat:, fix:, docs:, refactor:, test:, chore:
- PR por tarea, con al menos un revisor
- Definition of Done: desarrollada, funciona, probada, revisada, integrada, documentada

## Cómo preparar el entorno local

```bash
git clone https://github.com/No-Country-simulation/S08-26-EQUIPO-24
cd S08-26-EQUIPO-24
pip install -r requirements.txt
```

## Cómo ejecutar el dashboard

```bash
streamlit run dashboard/app.py
```

## Cómo contribuir

Ver CONTRIBUTING.md.

## Limitaciones conocidas

- Modelo no entrenado.
- Dashboard v0.2 (componentes modulares, mock data).
- FastAPI no está incluido en el MVP.
- Dataset AI4I 2020 solo para validación secundaria.

## Nota sobre datasets

Dataset principal: **Azure PdM** en `data/raw/` (5 archivos). Validación secundaria: AI4I 2020.
Los datos crudos van en data/raw/ y no se modifican.

## Principio de transparencia

Crear variables derivadas es válido cuando existe justificación técnica o de negocio y el proceso es reproducible. No se deben inventar datos históricos.

## Demo futura

Cuando el MVP esté listo, se ejecutará dashboard/app.py para demostrar:
1. Identificar máquinas con mayor riesgo.
2. Comprender las señales del riesgo.
3. Priorizar qué atender primero.