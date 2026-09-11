# Selección de Dataset

Este documento define el marco para evaluar y seleccionar el dataset del proyecto.

**ESTADO: ✅ DATASET SELECCIONADO — Microsoft Azure Predictive Maintenance (Azure PdM)**

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

**Regla:** "Crear variables derivadas es válido cuando existe una justificación técnica o de negocio y el proceso es reproducible."

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

## 5. Matriz de comparación de datasets (COMPLETADA)

| Criterio | Peso | Azure PdM | AI4I 2020 |
|---|---|---|---|
| Alineación con NoCountry | Alto | ⭐⭐⭐⭐⭐ Flota 100 máquinas, 1 año | ⭐⭐⭐ Sintético, 10k instancias |
| Realismo industrial | Alto | ⭐⭐⭐⭐⭐ Telemetría + mantenimiento + fallas | ⭐⭐⭐⭐ Solo proceso mecanizado |
| Múltiples máquinas | Alto | ✅ 100 IDs únicos | ❌ 1 registro por Product ID |
| Identificador de máquina | Alto | ✅ machineID en 5 tablas | ✅ Product ID |
| Sensores | Alto | 4 temporales (volt, rotate, pressure, vibration) | 5 estáticos (T, T, R, T, W) |
| Variables físicas interpretables | Medio | ✅ Proxies industriales fuertes | ✅ Temperatura, torque, desgaste |
| Temporalidad | Alto | ✅ Horaria, 365 días continuos | ❌ Sin timestamps |
| Historial de fallas | Alto | ✅ 4 componentes, fechas exactas | ✅ Binario + 5 tipos (multi-label) |
| Cantidad de fallas | Medio | ~300+ fallas registradas | ~3,300 fallas (binario) |
| Modos de falla | Bajo | 4 (comp1–comp4) | 5 (TWF, HDF, PWF, OSF, RNF) |
| Historial de mantenimiento | Medio | ✅ df_maint: fechas + componente | ❌ No existe |
| Variables derivadas posibles | Alto | ✅ **Rolling, trend, lag, RUL** | ❌ 0 (sin temporalidad) |
| Detección de deterioro | Alto | ✅ Series temporales pre-falla | ❌ Imposible |
| Explicabilidad | Alto | ✅ Sensores físicos mapeables | ✅ Variables directas |
| Criticidad | Medio | ✅ Via age + failure history | ⚠️ Limitada |
| Priorización | Alto | ✅ Riesgo × criticidad × impacto | ⚠️ Solo riesgo binario |
| Calidad | Alto | ⚠️ Requiere joins (5 tablas) | ✅ Tabla única, limpia |
| Complejidad | Medio | Media (data engineering) | Baja (ready-to-use) |
| Viabilidad (4 semanas) | Alto | ✅ **Óptima** para time-series | ✅ Alta para clasificación |

---

## 6. Candidatos disponibles en raw

### Dataset A — Microsoft Azure Predictive Maintenance (SELECCIONADO)

- **Origen:** Microsoft Azure, dataset público de mantenimiento predictivo.
- **Archivos en `data/raw/`:**
  - `PdM_errors.csv` — alarmas y errores por máquina.
  - `PdM_failures.csv` — registros de fallas (comp1–comp4).
  - `PdM_machines.csv` — información de las máquinas (model, age).
  - `PdM_maint.csv` — historial de mantenimiento (fechas + componente).
  - `PdM_telemetry.csv` — telemetría horaria (volt, rotate, pressure, vibration).
- **Fortalezas:** múltiples máquinas, sensores reales, historial de mantenimiento, eventos de falla, telemetría temporal, permite variables derivadas.
- **Complejidad:** dataset grande (~80 MB telemetría), requiere feature engineering y joins.

### Dataset B — AI4I 2020 Industrial Machine Failure Prediction (Validación secundaria)

- **Origen:** AI4I 2020, dataset público de falla de máquinas industriales.
- **Archivo en `data/raw/`:**
  - `ai4i2020.csv` — 10,001 registros con sensores y variable de falla.
- **Fortalezas:** dataset único y limpio, variable objetivo clara, fácil de explorar.
- **Complejidad:** una sola tabla, sin historial de mantenimiento ni temporalidad.
- **Uso:** Benchmark rápido de clasificación binaria, validación de modelos base.

---

## 7. Proceso de selección

1. Evaluar los datasets candidatos disponibles. ✅
2. Completar la matriz de comparación. ✅
3. Revisar con el equipo. ✅
4. Decidir dataset final. ✅ **Azure PdM**
5. Documentar en `docs/data_dictionary.md` y `data/README.md`. ✅

---

## 8. Justificación de la decisión

**Azure PdM seleccionado por:**

1. **Contexto Industrial Realista:** Flota de 100 máquinas con telemetría horaria 24/7 durante 1 año — simula mantenimiento predictivo genuino.
2. **Variables Derivadas (Factor Decisivo):** Estructura temporal permite rolling mean/std (24h/72h/168h), tendencias (slope), lags y RUL — detecta deterioro *antes* de la falla.
3. **Historial de Mantenimiento:** `df_maint` permite `hours_since_maintenance` y `remaining_useful_life`, crítico para modelos de supervivencia.
4. **Mapeo de Variables:** pressure (esfuerzo), rotate (movimiento), vibration (deterioro) cubren necesidades físicas; ausencia de temperatura compensada con proxies.
5. **Viabilidad MVP:** Aunque requiere data engineering, permite demostrar EDA, feature engineering temporal, modelado time-series y dashboard de riesgo completo.

**Evidencia técnica:** Ver `notebooks/01_data_exploration.ipynb` (sección 10) para análisis automatizado comparativo.

---

## Estado actual

**Dataset seleccionado: Microsoft Azure Predictive Maintenance**
- Evaluación completada y documentada.
- Matriz de comparación completada con evidencia cuantitativa.
- Próximo paso: Data Engineering (unir 5 tablas → dataset unificado).