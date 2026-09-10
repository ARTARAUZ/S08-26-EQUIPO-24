# Modelo

Este documento describe el enfoque de modelado para el proyecto.

**IMPORTANTE:** Aún no se ha entrenado ningún modelo. Este es el marco de trabajo.

---

## Objetivo

Predecir el riesgo de falla de cada máquina en un horizonte de tiempo definido.

---

## Target

- **Variable:** failure (boolean) o failure_next_N_periods.
- **Horizonte:** ej. 7, 14 o 30 días.

---

## Baseline

- Reglas simples basadas en umbrales de sensores.
- Ej: `IF vibration > threshold AND temperature trend increasing THEN elevated risk`.

---

## Modelos candidatos

- Logistic Regression
- Random Forest
- XGBoost / LightGBM (evaluar si los datos lo permiten)

---

## Evaluación

- Precision, Recall, F1, PR-AUC.
- False Negatives (importante: no fallar una detección).
- Lead Time (cuánto tiempo antes de la falla se detecta).

---

## Explicabilidad

- SHAP o feature importance.
- Principales señales que explican el riesgo.

---

## Artefacto

- Serializado en `models/` como `.pkl` o `.joblib`.

---

## Estado actual

**Pendiente.** Dataset no seleccionado, modelo no entrenado.