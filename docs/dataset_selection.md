# Selección de Dataset

Este documento define el marco para evaluar y seleccionar el dataset del proyecto.

**IMPORTANTE:** Aún no se ha seleccionado dataset. Esta es la guía para la evaluación estructurada.

---

## 1. Principios

- No se deben inventar datos históricos.
- Crear variables derivadas es válido cuando existe fundamento técnico, matemático o de negocio.
- Todo proceso de derivación debe ser reproducible.

---

## 2. Criterios de evaluación

| Criterio | Peso | Descripción |
|---|---|---|
| Alineación con NoCountry | Alto | Contexto industrial real |
| Realismo industrial | Alto | Sensores y máquinas creíbles |
| Múltiples máquinas | Alto | Permite ranking y comparación |
| Identificador de máquina | Alto | machine_id disponible |
| Sensores | Alto | temperature, vibration, pressure, etc. |
| Variables físicas interpretables | Medio | Permite explicabilidad |
| Temporalidad | Alto | Timestamps o frecuencia de medición |
| Historial de fallas | Alto | Eventos de fallo registrados |
| Cantidad de fallas | Medio | Suficientes para ML supervisado |
| Modos de falla | Bajo | Tipo de componente afectado |
| Historial de mantenimiento | Medio | Permite variables derivadas |
| Posibilidad de crear variables derivadas | Alto | rolling_mean, trend, etc. |
| Capacidad de detectar deterioro | Alto | Señales pre-falla observables |
| Explicabilidad | Alto | Variables interpretables |
| Criticidad | Medio | Permite priorización |
| Posibilidad de priorización | Alto | Combinar riesgo y criticidad |
| Calidad | Alto | Nulos, outliers, consistencia |
| Complejidad | Medio | Viabilidad dentro de 4 semanas |
| Viabilidad | Alto | Se puede usar en el tiempo disponible |

---

## 3. Datos observados vs Variables derivadas vs Reglas de negocio

### Datos observados
Registros directamente medidos por sensores o sistemas. Ej: temperature, vibration, timestamp.

### Variables derivadas
Se calculan a partir de datos observados usando una regla técnica o matemática. Ej: rolling_mean, hours_since_maintenance, trend.

**Regla:** "Creator variables derivadas es válido cuando existe una justificación técnica o de negocio y el proceso es reproducible."

### Reglas de negocio
Decisiones o clasificaciones definidas por el equipo. Ej: criticidad de una máquina, prioridad de intervención.

---

## 4. Ejemplos de variables derivadas permitidas

- hours_since_maintenance
- days_since_maintenance
- previous_failures
- maintenance_count
- rolling_mean
- rolling_std
- trend
- rate_of_change
- anomaly_score
- failure_next_N_periods
- criticality
- priority_score

---

## 5. Matriz de comparación de datasets

| Criterio | Peso | Dataset A | Dataset B | Dataset C |
|---|---|---|---|---|
| Alineación con NoCountry | Alto | | | |
| Realismo industrial | Alto | | | |
| Múltiples máquinas | Alto | | | |
| Identificador de máquina | Alto | | | |
| Sensores | Alto | | | |
| Variables físicas interpretables | Medio | | | |
| Temporalidad | Alto | | | |
| Historial de fallas | Alto | | | |
| Cantidad de fallas | Medio | | | |
| Modos de falla | Bajo | | | |
| Historial de mantenimiento | Medio | | | |
| Variables derivadas posibles | Alto | | | |
| Detección de deterioro | Alto | | | |
| Explicabilidad | Alto | | | |
| Criticidad | Medio | | | |
| Priorización | Alto | | | |
| Calidad | Alto | | | |
| Complejidad | Medio | | | |
| Viabilidad (4 semanas) | Alto | | | |

---

## 6. Candidatos iniciales (sin selección)

- Microsoft Azure Predictive Maintenance (dataset público)
- AI4I 2020 Industrial Machine Failure Prediction
- Otros que evalúe el equipo

---

## 7. Proceso de selección

1. Evaluar 2-3 datasets candidatos.
2. Completar la matriz de comparación.
3. Revisar con el equipo.
4. Decidir dataset final.
5. Documentar en `docs/data_dictionary.md` y `data/README.md`.

---

## Estado actual

**Pendiente de selección.** No se ha tomado decisión.