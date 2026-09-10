# Diccionario de Datos

Este documento es una plantilla para documentar las variables del dataset.

**IMPORTANTE:** Aún no se ha seleccionado dataset. Las variables listadas son **ejemplos deseados**, no afirmaciones de que existen.

---

## Plantilla

| Variable | Tipo | Unidad | Descripción | Fuente | Observada/Derivada | Uso |
|---|---|---|---|---|---|---|
| machine_id | string | - | Identificador único de máquina | Sistema | Observada | Agrupación, ranking |
| timestamp | datetime | - | Fecha y hora del registro | Sensor | Observada | Series de tiempo |
| temperature | float | °C | Temperatura del componente | Sensor | Observada | Feature |
| vibration | float | mm/s | Vibración del eje | Sensor | Observada | Feature |
| pressure | float | bar | Presión del sistema | Sensor | Observada | Feature |
| speed | float | rpm | Velocidad de rotación | Sensor | Observada | Feature |
| load | float | kW | Carga eléctrica | Sensor | Observada | Feature |
| operating_hours | float | h | Horas de operación acumuladas | Sistema | Observada | Feature |
| alarm | boolean | - | Alarma activa | Sistema | Observada | Feature |
| error | string | - | Código de error | Sistema | Observada | Feature |
| maintenance_date | datetime | - | Fecha de último mantenimiento | Sistema | Observada | Feature |
| maintenance_type | string | - | Tipo de mantenimiento | Sistema | Observada | Feature |
| failure | boolean | - | Indica si hubo falla | Sistema | Observada | Target |
| failure_type | string | - | Tipo de falla | Sistema | Observada | Target |
| component | string | - | Componente afectado | Sistema | Observada | Feature |

---

## Variables mínimas esperadas

- machine_id
- timestamp
- temperature
- vibration
- pressure
- speed
- load
- operating_hours
- alarm
- error
- maintenance_date
- maintenance_type
- failure
- failure_type
- component

---

## Convenciones

- **Observada:** dato registrado directamente por sensores o sistemas.
- **Derivada:** variable calculada a partir de datos observados.
- **Target:** variable objetivo del modelo (ej: failure).

---

## Estado actual

**Pendiente.** Dataset no seleccionado.