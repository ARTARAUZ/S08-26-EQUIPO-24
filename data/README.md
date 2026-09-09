# Data

Este directorio contiene los datasets del proyecto.

---

## Estructura

### data/raw/
Datos crudos, sin modificar.
- No se aplican transformaciones.
- No se limpian.
- Documentar origen y versión.

### data/processed/
Datasets derivados, limpios y listos para uso.
- Puede incluir limpieza, feature engineering.
- Documentar transformaciones aplicadas.

---

## Reglas

- **raw no se modifica.**
- **processed** contiene datasets derivados.
- Documentar origen del dataset.
- Documentar transformaciones.
- No inventar registros.
- No subir datos sensibles.
- Registrar versión y fuente.

---

## Principio de transparencia

- Datos observados: registrados directamente.
- Variables derivadas: calculadas con justificación técnica o de negocio.
- Reglas de negocio: definidas por el equipo.

**No se deben inventar datos históricos** para aparentar que el dataset contiene información que realmente no posee.

---

## Estado actual

### data/raw/

Archivos cargados (sin modificar):

| Archivo | Origen | Descripción |
|---|---|---|
| `PdM_errors.csv` | Microsoft Azure Predictive Maintenance | Alarmas y errores por máquina |
| `PdM_failures.csv` | Microsoft Azure Predictive Maintenance | Registros de fallas |
| `PdM_machines.csv` | Microsoft Azure Predictive Maintenance | Información de las máquinas |
| `PdM_maint.csv` | Microsoft Azure Predictive Maintenance | Historial de mantenimiento |
| `PdM_telemetry.csv` | Microsoft Azure Predictive Maintenance | Telemetría (temperatura, vibración, etc.) |
| `ai4i2020.csv` | AI4I 2020 | 10,001 registros con sensores y variable de falla |

**Reglas:**
- raw no se modifica.
- Los datasets se evalúan para decidir cuál se usa en el MVP.
- data/processed/ contendrá los datasets limpios y derivados.

Dataset no seleccionado aún. Evaluación en curso.