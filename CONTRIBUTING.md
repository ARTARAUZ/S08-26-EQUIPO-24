# Contributing to PredictiveMaintenance

Gracias por tu interés en contribuir al proyecto. Este documento define las convenciones, flujo de trabajo y expectativas para todos los integrantes.

---

## 1. ¿Qué es este proyecto?

PredictiveMaintenance es una solución de mantenimiento predictivo en desarrollo. El objetivo es permitir a un responsable de mantenimiento:

1. **Identificar** qué máquinas tienen mayor riesgo de falla.
2. **Comprender** qué señales justifican ese riesgo.
3. **Priorizar** qué máquina debería atenderse primero.

Actualmente el repositorio está en **FASE: Discovery / Project Setup**. No hay modelo entrenado ni dashboard funcional todavía.

---

## 2. Regla de priorización

Antes de aceptar una nueva funcionalidad, pregúntate:

> "¿Esto ayuda a identificar riesgo, comprender riesgo o priorizar una intervención?"

- **SI** → prioridad (MUST / SHOULD).
- **NO** → backlog secundario (COULD).

Todo el desarrollo debe estar subordinado al criterio de éxito del proyecto.

---

## 3. Flujo de trabajo

### 3.1 Crear una rama

Usa el formato:

```
feature/<id>- descripcion
fix/<id>- descripcion
docs/< descripcion>
```

Ejemplos:

```
feature/ML-04-feature-engineering
feature/DASH-04-risk-ranking
docs/dataset-selection
fix/DATA-06-null-handling
```

### 3.2 Commits

Usa un prefijo descriptivo:

| Prefijo | Cuándo |
|---|---|
| `feat:` | Nueva funcionalidad |
| `fix:` | Corrección de error |
| `docs:` | Documentación |
| `refactor:` | Reorganización de código sin cambiar comportamiento |
| `test:` | Agregar o mejorar tests |
| `chore:` | Mantenimiento del repositorio (config, deps) |

Ejemplo:

```
feat: add rolling mean feature for sensor data
```

Mensajes cortos en el asunto, cuerpo con explicación si es necesario.

### 3.3 Pull Requests

- Abre un PR por tarea/feature, no por commit.
- Asigna al menos un revisor.
- Adjunta o enlaza la tarea del backlog (ej: `ML-07`).
- Describe los cambios y por qué se hicieron.
- Incluye outputs de tests si aplica.

### 3.4 Revisión

- Todo el código debe ser revisado por otro integrante.
- Los tests deben pasar.
- La documentación debe estar al día.
- No se hace merge sin aprobación.

---

## 4. Definition of Done

Una tarea solo pasa a **DONE** cuando:

- [ ] Desarrollada
- [ ] Funciona
- [ ] Probada (tests)
- [ ] Revisada por otro integrante
- [ ] Integrada en GitHub
- [ ] Documentada cuando corresponda

**No se considera suficiente:** "funciona en mi PC". Debe ser reproducible por el equipo.

---

## 5. Reglas de datos

- **No subas datasets grandes** innecesariamente a Git. Usa LFS o guárdalos localmente hasta que se decida.
- **No subas credenciales**, `.env`, secrets, tokens o datos sensibles.
- **No inventar datos históricos.** Crear variables derivadas es válido cuando existe justificación técnica o de negocio y el proceso es reproducible.
- Los datasets crudos van en `data/raw/` y **no se modifican**.
- Los datasets procesados van en `data/processed/`.
- Documenta siempre: origen, versión y transformaciones aplicadas.

---

## 6. Estructura del repositorio

```
data/           → datasets (raw y processed)
notebooks/      → exploración y análisis
src/            → código de producción (data, features, models, utils)
models/         → artefactos del modelo (.pkl, .joblib)
dashboard/      → aplicación Streamlit
tests/          → pruebas
docs/           → documentación del proyecto
.github/        → templates de issues y workflows CI
```

---

## 7. Cómo preparar el entorno local

```bash
# 1. Clonar
git clone https://github.com/No-Country-simulation/S08-26-EQUIPO-24
cd S08-26-EQUIPO-24

# 2. Dependencias
pip install -r requirements.txt

# 3. (Opcional) Streamlit
streamlit --version
```

---

## 8. Cómo ejecutar el dashboard (cuando exista)

```bash
streamlit run dashboard/app.py
```

---

## 9. Tests

```bash
pytest tests/
```

---

## 10. Notas

- Mantén el README actualizado.
- Comunica bloqueos en el canal del equipo.
- Prioriza el criterio de éxito por encima de todo.