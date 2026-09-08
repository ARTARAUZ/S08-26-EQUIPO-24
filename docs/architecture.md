# Arquitectura

---

## Flujo de solución

```
DATASET
    ↓
DATA CLEANING
    ↓
FEATURE ENGINEERING
    ↓
MODEL
    ↓
MODEL ARTIFACT (.pkl / .joblib)
    ↓
STREAMLIT
    ↓
DASHBOARD
    ↓
DECISION
```

---

## Capas

### 1. Dataset
- Datos crudos en `data/raw/`.
- Datos procesados en `data/processed/`.

### 2. Data Cleaning
- Limpieza, tratamientos de nulos, inconsistencias, duplicados.
- Validación de calidad.

### 3. Feature Engineering
- Variables derivadas (rolling_mean, trend, rate_of_change, etc.).
- Transformaciones para el modelo.

### 4. Model
- Modelo de ML entrenado.
- Serializado en `models/`.

### 5. Model Artifact
- `modelo.pkl` o `.joblib`.
- Cargado por el dashboard para inferencia.

### 6. Streamlit
- Frontend del dashboard.
- `dashboard/app.py`.

### 7. Dashboard
- Interfaz para el responsable de mantenimiento.
- Ranking, explicación, prioridad.

### 8. Decision
- Acción de mantenimiento.

---

## FastAPI

**Opcional. No es dependencia del MVP inicial.**

**Razón:**
- 4 semanas de proyecto.
- Equipo junior.
- 1 solo Software Engineer.
- Prioridad: producto funcional.

Si en el futuro se requiere API, se documentará como decisión de arquitectura.