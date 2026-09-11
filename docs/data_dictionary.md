# Diccionario de Datos

Documentación de variables del **dataset seleccionado: Microsoft Azure Predictive Maintenance (Azure PdM)**.

---

## Dataset A: Azure PdM — Tablas en `data/raw/`

### 1. df_telemetry (Telemetría horaria)

| Variable | Tipo | Unidad | Descripción | Fuente | Observada/Derivada | Uso |
|---|---|---|---|---|---|---|
| machineID | int | - | Identificador único de máquina (1–100) | Sensor | Observada | Agrupación, ranking, join |
| datetime | datetime | - | Timestamp de la lectura (horario) | Sensor | Observada | Series de tiempo, join |
| volt | float | V | Tensión eléctrica | Sensor | Observada | Feature, proxy estabilidad |
| rotate | float | RPM | Velocidad de rotación | Sensor | Observada | Feature, proxy movimiento |
| pressure | float | psi | Presión de trabajo | Sensor | Observada | Feature, proxy esfuerzo |
| vibration | float | mm/s² | Nivel de vibración | Sensor | Observada | Feature, **mejor indicador deterioro** |

### 2. df_errors (Errores/Alarmas)

| Variable | Tipo | Unidad | Descripción | Fuente | Observada/Derivada | Uso |
|---|---|---|---|---|---|---|
| datetime | datetime | - | Timestamp del error | Sistema | Observada | Feature, eventos pre-falla |
| machineID | int | - | Identificador de máquina | Sistema | Observada | Join, agrupación |
| errorID | string | - | Código de error (error1–error5) | Sistema | Observada | Feature, tipo de alarma |

### 3. df_failures (Fallas registradas)

| Variable | Tipo | Unidad | Descripción | Fuente | Observada/Derivada | Uso |
|---|---|---|---|---|---|---|
| datetime | datetime | - | Timestamp de la falla | Sistema | Observada | **Target**, eventos críticos |
| machineID | int | - | Identificador de máquina | Sistema | Observada | Join, agrupación |
| failure | string | - | Componente fallido (comp1–comp4) | Sistema | Observada | **Target multi-clase**, modo de falla |

### 4. df_machines (Información de máquinas)

| Variable | Tipo | Unidad | Descripción | Fuente | Observada/Derivada | Uso |
|---|---|---|---|---|---|---|
| machineID | int | - | Identificador único | Sistema | Observada | Join, agrupación |
| model | string | - | Modelo/tipo de máquina | Especificación | Observada | Feature, segmentación |
| age | int | años | Antigüedad de la máquina | Especificación | Observada | Feature, criticidad |

### 5. df_maint (Historial de mantenimiento)

| Variable | Tipo | Unidad | Descripción | Fuente | Observada/Derivada | Uso |
|---|---|---|---|---|---|---|
| datetime | datetime | - | Fecha de mantenimiento | Sistema | Observada | Feature, cálculo RUL |
| machineID | int | - | Identificador de máquina | Sistema | Observada | Join, agrupación |
| comp | string | - | Componente reemplazado (comp1–comp4) | Sistema | Observada | Feature, vida útil componente |

---

## Dataset B: AI4I 2020 — Validación secundaria

| Variable | Tipo | Unidad | Descripción | Fuente | Observada/Derivada | Uso |
|---|---|---|---|---|---|---|
| UDI | int | - | Identificador único de registro | Índice | Observada | Índice |
| Product ID | string | - | Identificador de producto/máquina | Sistema | Observada | Agrupación (limitada) |
| Type | string | - | Tipo de máquina (L, M, H) | Especificación | Observada | Feature, segmentación |
| Air temperature [K] | float | K | Temperatura ambiente | Sensor | Observada | Feature |
| Process temperature [K] | float | K | Temperatura de proceso | Sensor | Observada | Feature |
| Rotational speed [rpm] | float | rpm | Velocidad de rotación | Sensor | Observada | Feature |
| Torque [Nm] | float | Nm | Par de torsión | Sensor | Observada | Feature, proxy esfuerzo |
| Tool wear [min] | float | min | Desgaste acumulado herramienta | Sensor | Observada | Feature, proxy RUL |
| Machine failure | int | - | Fallo binario (0/1) | Sistema | Observada | **Target binario** |
| TWF, HDF, PWF, OSF, RNF | int | - | Tipos de falla específicos (multi-label) | Sistema | Observada | Target multi-label |

---

## Variables derivadas planificadas (Azure PdM → data/processed/)

| Variable | Tipo | Fórmula / Regla | Justificación |
|---|---|---|---|
| hours_since_maint | float | `(datetime - last_maint_datetime).total_seconds() / 3600` | Vida útil residual, degradación |
| rolling_mean_24h | float | `sensor.rolling(24).mean()` | Tendencia suavizada, reduce ruido |
| rolling_std_24h | float | `sensor.rolling(24).std()` | Volatilidad, inestabilidad |
| rolling_mean_168h | float | `sensor.rolling(168).mean()` | Tendencia semanal |
| vibration_trend_24h | float | `slope(vibration.rolling(24))` | Aceleración del deterioro |
| lag_1h, lag_24h | float | `sensor.shift(1), sensor.shift(24)` | Autocorrelación, memoria |
| failure_next_24h | bool | `failure in next 24h` | Target anticipado |
| failure_next_168h | bool | `failure in next 168h` | Target horizonte semanal |
| RUL_hours | float | `hours_to_next_failure` | Remaining Useful Life |

---

## Convenciones

- **Observada:** dato registrado directamente por sensores o sistemas.
- **Derivada:** variable calculada a partir de datos observados (con justificación técnica).
- **Target:** variable objetivo del modelo (ej: failure, failure_next_Nh, RUL).

---

## Estado actual

**Dataset principal: Azure PdM** — Diccionario completado para 5 tablas raw.
**Validación secundaria: AI4I 2020** — Diccionario documentado para benchmark.

Próximo: Generar `data/processed/` con dataset unificado y variables derivadas.