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

| Prefijo     | Cuándo                                              |
| ----------- | --------------------------------------------------- |
| `feat:`     | Nueva funcionalidad                                 |
| `fix:`      | Corrección de error                                 |
| `docs:`     | Documentación                                       |
| `refactor:` | Reorganización de código sin cambiar comportamiento |
| `test:`     | Agregar o mejorar tests                             |
| `chore:`    | Mantenimiento del repositorio (config, deps)        |

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

## 7. Cómo preparar el entorno local (Python + venv)

### Requisitos previos

- Python 3.12 o superior
- Git
- IDE: VS Code, Antigravity, o cualquier editor con terminal integrada

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/No-Country-simulation/S08-26-EQUIPO-24
cd S08-26-EQUIPO-24
```

### Paso 2: Crear entorno virtual

```bash
python -m venv .venv
```

### Paso 3: Activar el entorno virtual

**Windows (PowerShell):**

```bash
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```bash
.venv\Scripts\activate.bat
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

> **Nota:** En VS Code o Antigravity, al abrir la terminal integrada (en antigravity`Ctrl+shift+ñ`), el entorno se activa automáticamente si la carpeta .venv existe. Si no, ejecuta el comando de activación manual `.venv\Scripts\Activate.ps1`.

### Paso 4: Instalar dependencias (comandos probados, sin errores)

**Importante:** Instala las dependencias en este orden para evitar problemas de resolución:

```bash
# 1. Actualizar pip
.venv\Scripts\python.exe -m pip install --upgrade pip

# 2. Instalar paquetes core
.venv\Scripts\pip.exe install pandas numpy scikit-learn joblib

# 3. Instalar visualización
.venv\Scripts\pip.exe install matplotlib seaborn plotly

# 4. Instalar dashboard
.venv\Scripts\pip.exe install streamlit

# 5. Instalar desarrollo
.venv\Scripts\pip.exe install jupyter ipykernel pytest
```

> **Alternativa rápida (todo de una vez):**
>
> ```bash
> .venv\Scripts\pip.exe install -r requirements.txt
> ```
>
> Si esto falla por timeout, instala en lotes como se indica arriba.

### Paso 5: Verificar instalación

```bash
.venv\Scripts\python.exe -c "import pandas, numpy, sklearn, streamlit, matplotlib, seaborn, plotly; print('OK - Todas las librerias'); print('pandas:', pandas.__version__); print('streamlit:', streamlit.__version__); print('sklearn:', sklearn.__version__)"
```

Salida esperada:

```
OK - Todas las librerias
pandas: 3.0.5
streamlit: 1.63.0
sklearn: 1.9.1
```

### Paso 6: Datasets

Los datasets ya están en `data/raw/` (6 archivos CSV). Se cargarán directamente desde GitHub raw URLs, no es necesario descargarlos de nuevo.

```bash
# Verificar datasets
ls data/raw/
```

### Paso 7: Ejecutar notebooks

**Opción A: VS Code / Antigravity (recomendado)**

- Abre `notebooks/01_data_exploration.ipynb`
- Haz click en "Run All" o ejecuta celda por celda (Ctrl+Enter)

**Opción B: Terminal**

```bash
jupyter notebook notebooks/
```

Luego abre la URL que se genera en el navegador.

### Paso 8: Ejecutar el dashboard

```bash
streamlit run dashboard/app.py
```

El dashboard se abre automáticamente en `http://localhost:8501`.

### Cómo usar la terminal del IDE (VS Code / Antigravity)

1. Abre el IDE
2. Abre la carpeta del proyecto (`S08-26-EQUIPO-24`)
3. Abre la terminal integrada: `Ctrl + '` (VS Code) o `Ctrl + Shift + Ñ` (Antigravity)
4. El entorno virtual se activa automáticamente si `.venv` está en la raíz
5. Si no se activó, ejecuta manualmente:
   - PowerShell: `.venv\Scripts\Activate.ps1`
   - CMD: `.venv\Scripts\activate.bat`

### Flujo de contribución

#### Crear una rama

```bash
git checkout -b feature/<id>-detalle
```

Ejemplos: `feature/ML-04-feature-engineering`, `fix/DATA-06-null-handling`, `docs/dataset-selection`

#### Hacer commits

```bash
git add .
git commit -m "feat: add rolling mean feature for sensor data"
```

Prefijos: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`

#### Crear Pull Request

```bash
git push origin feature/<id>-detalle
```

Luego abre un PR en GitHub con al menos un revisor, describiendo los cambios y enlazando la tarea del backlog (ej: `ML-07`).

---

## 8. Flujo de contribución

### 8.1 Crear una rama

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

### 8.2 Commits

Usa un prefijo descriptivo:

| Prefijo     | Cuándo                                              |
| ----------- | --------------------------------------------------- |
| `feat:`     | Nueva funcionalidad                                 |
| `fix:`      | Corrección de error                                 |
| `docs:`     | Documentación                                       |
| `refactor:` | Reorganización de código sin cambiar comportamiento |
| `test:`     | Agregar o mejorar tests                             |
| `chore:`    | Mantenimiento del repositorio (config, deps)        |

Ejemplo:

```
feat: add rolling mean feature for sensor data
```

Mensajes cortos en el asunto, cuerpo con explicación si es necesario.

### 8.3 Pull Requests

- Abre un PR por tarea/feature, no por commit.
- Asigna al menos un revisor.
- Adjunta o enlaza la tarea del backlog (ej: `ML-07`).
- Describe los cambios y por qué se hicieron.
- Incluye outputs de tests si aplica.

### 8.4 Revisión

- Todo el código debe ser revisado por otro integrante.
- Los tests deben pasar.
- La documentación debe estar al día.
- No se hace merge sin aprobación.

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
