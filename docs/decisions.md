# Decisiones del Proyecto

Registro de decisiones arquitectónicas y de producto.

---

## DEC-001
**Priorizar MVP sobre plataforma completa.**

- **Fecha:** 2026-09-08
- **Contexto:** 4 semanas, equipo junior, 1 Software Engineer.
- **Decisión:** Construir MVP funcional y demostrable antes de ampliar alcance.
- **Consecuencia:** FastAPI, autenticación, base de datos y alertas quedan como futuras.

---

## DEC-002
**Streamlit como primera opción de frontend.**

- **Fecha:** 2026-09-08
- **Contexto:** Necesidad de prototipado rápido y visualización de datos.
- **Decisión:** Usar Streamlit para el dashboard MVP.
- **Consecuencia:** No se requiere frontend complejo ni API inicial.

---

## DEC-003
**FastAPI opcional.**

- **Fecha:** 2026-09-08
- **Contexto:** Solo 1 Software Engineer disponible.
- **Decisión:** No incluir FastAPI en el MVP. Es un componente futuro.
- **Consecuencia:** El dashboard consume el modelo directamente sin capa de API.

---

## DEC-004
**No seleccionar dataset antes de evaluación estructurada.**

- **Fecha:** 2026-09-08
- **Contexto:** Riesgo de elegir dataset inadecuado.
- **Decisión:** Evaluar 2-3 candidatos con la matriz de `docs/dataset_selection.md`.
- **Consecuencia:** La selección正式 delayed until evaluation completes.

---

## DEC-005
**Variables derivadas permitidas, pero no datos inventados.**

- **Fecha:** 2026-09-08
- **Contexto:** Necesidad de features para el modelo.
- **Decisión:** Permitir variables derivadas con justificación técnica o de negocio. Prohibir datos históricos inventados.
- **Consecuencia:** El pipeline debe distinguir dato original, variable derivada y regla de negocio.

---

## DEC-006
**El criterio de éxito guía el backlog.**

- **Fecha:** 2026-09-08
- **Contexto:** Riesgo de scope creep.
- **Decisión:** Toda tarea se evalúa contra: identificar riesgo, comprender riesgo o priorizar.
- **Consecuencia:** Funcionalidades que no apoyan el criterio van a backlog secundario.

---

## DEC-007
**Deploy inicial en Streamlit Community Cloud.**

- **Fecha:** 2026-09-08
- **Contexto:** Necesidad de demostración rápida.
- **Decisión:** Usar Streamlit Community Cloud como primera opción.
- **Consecuencia:** Validar limitaciones de ancho de banda, privacidad y rendimiento.

---

## DEC-008
**Modelo simple antes que complejo.**

- **Fecha:** 2026-09-08
- **Contexto:** 4 semanas, datos limitados.
- **Decisión:** Baseline + modelo simple (Logistic Regression / Random Forest) antes de probar XGBoost o modelos complejos.
- **Consecuencia:** Mayor tiempo para integración y dashboard.

---

## Próximas decisiones

- DEC-009: Dataset final seleccionado.
- DEC-010: Modelo final seleccionado.
- DEC-011: Estrategia de deploy final.