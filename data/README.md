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
| `PdM_failures.csv` | Microsoft Azure Predictive Maintenance | Registros de fallas (comp1–comp4) |
| `PdM_machines.csv` | Microsoft Azure Predictive Maintenance | Información de las máquinas (model, age) |
| `PdM_maint.csv` | Microsoft Azure Predictive Maintenance | Historial de mantenimiento (fechas + componente) |
| `PdM_telemetry.csv` | Microsoft Azure Predictive Maintenance | Telemetría horaria (volt, rotate, pressure, vibration) |
| `ai4i2020.csv` | AI4I 2020 | 10,001 registros con sensores y variable de falla |

**Reglas:**
- raw no se modifica.
- **Dataset principal seleccionado:** Microsoft Azure Predictive Maintenance (Azure PdM).
- **Validación secundaria:** AI4I 2020 (benchmark clasificación).
- data/processed/ contendrá el dataset unificado y derivado de Azure PdM.

---

## Dataset Seleccionado: Azure PdM

**Justificación resumida:** Flota de 100 máquinas con telemetría horaria 1 año, historial mantenimiento, 4 tipos de falla, permite variables derivadas temporales (rolling mean, trend, RUL). Ver `docs/dataset_selection.md` y `notebooks/01_data_exploration.ipynb` (sección 10) para análisis completo.

### Próximos pasos en data/processed/
1. Unir 5 tablas por `machineID` + `datetime` → dataset unificado.
2. Feature engineering: rolling windows (24h/72h/168h), lags, `hours_since_maintenance`, `RUL`.
3. Train/test split temporal (no aleatorio) para evitar data leakage.
4. Guardar como `data/processed/azure_pdm_unified.parquet` (o CSV).