# Dashboard MVP — Diseño Visual y UI

**Responsable:** DS/DA (Data Analyst — Dashboard / UX)
**Framework:** Streamlit (componentes nativos + Plotly + HTML/CSS personalizado)
**Estado:** MVP Implementado (Premium Dark Theme)

---

## 1. Estructura general

El dashboard se compone de:

- `dashboard/app.py` — Entry point principal
- `dashboard/components/` — Componentes modulares
- `dashboard/utils/data_loader.py` — Datos de ejemplo (mock)

Los componentes son:

- `risk_table.py` — Tabla de ranking de riesgo con colores por nivel.
- `sensor_chart.py` — Gráfico de telemetría de sensores en tiempo real.
- `machine_detail.py` — Histórico de errores (expander).
- `priority_list.py` — Lista de tareas prioritarias (con progress bars y UI rica).

---

## 2. Wireframe — Pantalla principal

### 2.1 Barra lateral (st.sidebar)

| Elemento           | Streamlit                     | Datos                                      |
| ------------------ | ----------------------------- | ------------------------------------------ |
| Logo + código     | `st.title` + `st.caption` | S08-26-EQUIPO-24                           |
| Selector máquina  | `st.selectbox`              | `machine_id` (CNC-001, MILL-004, etc.)   |
| Filtro estado      | `st.multiselect`            | Crítico, Moderado, Estable                |
| Filtro criticidad  | `st.multiselect`            | Alta, Media, Baja                          |
| Metadatos rápidos | `st.write`                  | ID, Tipo, Ubicación, Horas, Mantenimiento |

### 2.2 Header principal

- `st.title`: PredictiveMaintenance
- `st.caption`: Fase: Discovery / MVP Dashboard
- `st.divider()`

### 2.3 Fila de KPIs (st.columns + st.metric)

| KPI                    | Label                  | Delta                | Color                          |
| ---------------------- | ---------------------- | -------------------- | ------------------------------ |
| Total máquinas        | Máquinas Monitoreadas | -                    | Azul                           |
| Riesgo crítico        | Riesgo Crítico        | "requiere atención" | Rojo (`delta_color=inverse`) |
| Próximo mantenimiento | Próximo Mantenimiento | fecha                | Naranja                        |
| Riesgo promedio        | Riesgo Promedio        | porcentaje           | Verde                          |

---

## 3. Pestañas principales (st.tabs)

### 3.1 Tab 1 — 🎯 Identificar (Riesgo)

Elementos:

- `st.error`: Alerta de máquinas en nivel crítico (atención inmediata)
- `st.dataframe`: Tabla interactiva con colores por nivel de riesgo
- **Gráfico Plotly (Bar Chart Horizontal)**: Distribución de riesgo ordenada descendentemente, con colores semánticos (Rojo, Naranja, Verde) y tooltips interactivos detallados. Línea vertical marcando el umbral crítico (75%).

Colores por nivel:

- **Crítico:** fondo rojo claro, texto rojo oscuro
- **Moderado:** fondo amarillo claro, texto marrón
- **Estable:** fondo verde claro, texto verde oscuro

### 3.2 Tab 2 — 📡 Comprender (Señales)

Layout: `st.columns([2, 1])`

**Columna 1 (2/3 ancho):**

- `st.selectbox`: Selector de sensor (temperatura, vibración, presión)
- `st.line_chart`: Gráfico de línea de telemetría temporal de la máquina seleccionada
- `st.expander`: Último registro con valores numéricos

**Columna 2 (1/3 ancho):**

- `st.expander`: Histórico de errores por máquina (fecha, código, descripción)

**Métricas dinámicas (st.metric):**
- Valores en tiempo real (último registro) comparados con el inicio (delta).
- 🌡️ Temperatura, 📳 Vibración, 💧 Presión.

### 3.3 Tab 3 — 🚀 Priorizar (Acción)

Elementos:

- `st.info`: Explicación de criterio de priorización (riesgo × criticidad × impacto)
- **Lista enriquecida**:
  - Ranking con iconos (🥇, 🥈, 🥉).
  - Progress bars (`st.progress`) para visualizar el riesgo de cada máquina.
- **Card HTML de Recomendación**: Resumen visual con fondo con gradiente, bordes de color y los datos principales (ID, tipo, ubicación, días sin mantenimiento, acción a tomar).

---

## 4. Paleta de colores

| Estado   | Hex         | Uso                                  |
| -------- | ----------- | ------------------------------------ |
| Crítico | `#ff4b4b` | Alertas, delta rojo, riesgo crítico |
| Moderado | `#ffa500` | Warning, riesgo moderado             |
| Estable  | `#28a745` | Success, riesgo estable              |
| Neutro   | `#6c757d` | Info, caption, metadata              |
| Fondo    | `#ffffff` | Fondo limpio                         |
| Texto    | `#262730` | Texto del cuerpo                     |

---

## 5. Responsive y Diseño Personalizado

- `layout=wide`: Contenedor principal ancho
- `st.columns()`: Se adapta automáticamente a móviles.
- **CSS Personalizado (`app.py`)**:
  - Tipografía `Inter`.
  - Glassmorphism en tarjetas de KPI (bordes y fondos semitransparentes).
  - Emojis expresivos en headers, tabs y métricas.
  - Efectos hover y transiciones fluidas.
- **Tema Streamlit (`.streamlit/config.toml`)**:
  - Tema Base Oscuro (`dark`).
  - Color Primario: `#3b82f6` (Azul Moderno).
  - Fondos personalizados tipo Navy (`#0f172a`, `#1e293b`).

---

## 6. Mock data placeholder

El archivo `utils/data_loader.py` contiene datos de ejemplo:

- 6 máquinas (CNC, Torno, Fresadora, Bomba, Transportador)
- Riesgo calculado (score 0-100)
- Telemetría 30 días (temperatura, vibración, presión)
- Histórico de errores (5 registros)

Cuando el modelo ML esté listo: reemplazar esta lógica por lectura real de `data/processed/` y predicciones del modelo.

---

## 7. Flujo de usuario

1. El usuario abre el dashboard
2. Selecciona una máquina en la barra lateral
3. Filtra por estado y criticidad
4. Revisa la pestaña 1 para ver ranking de riesgo
5. Selecciona una máquina crítica
6. Va a la pestaña 2 para ver señales y histórico
7. Va a la pestaña 3 para ver la acción recomendada

---

## 8. Archivos del dashboard

```
dashboard/
├── app.py
├── components/
│   ├── __init__.py
│   ├── risk_table.py
│   ├── sensor_chart.py
│   ├── machine_detail.py
│   └── priority_list.py
└── utils/
    ├── __init__.py
    └── data_loader.py
```
