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

Dataset no seleccionado. Las carpetas están listas para recibir datos cuando se defina.