# Dashboard MVP — Diseno Visual

> Responsable: Carlos Vega (Data Analyst — Dashboard / UX)
> Framework: Streamlit (componentes nativos, responsive)
> Estado: Diseno inicial aprobado

---

## 1. Estructura general

El dashboard se compone de:
- `dashboard/app.py` — Entry point principal
- `dashboard/components/` — Componentes modulares
- `dashboard/utils/data_loader.py` — Datos de ejemplo (mock)

Los componentes son:
- `risk_table.py` — Tabla de ranking de riesgo con colores por nivel
- `sensor_chart.py` — Grafico de telemetria de sensores
- `machine_detail.py` — Historico de errores (expander)
- `priority_list.py` — Lista de tareas prioritarias

---

## 2. Barra lateral (st.sidebar)

Componentes:
- Logo + codigo: st.title + st.caption (S08-26-EQUIPO-24)
- Selector de maquina: st.selectbox con machine_id (CNC-001, MILL-004, etc.)
- Filtro estado: st.multiselect (Critico, Moderado, Estable)
- Filtro criticidad: st.multiselect (Alta, Media, Baja)
- Metadatos rapidos: st.write con ID, Tipo, Ubicacion, Horas, Mantenimiento

---

## 3. Contenido principal

### 3.1 Header
- st.title: PredictiveMaintenance
- st.caption: Fase: Discovery / MVP Dashboard
- st.divider()

### 3.2 KPIs (st.columns + st.metric)

| KPI | Label | Delta | Color |
|---|---|---|---|
| Total maquinas | Maquinas Monitoreadas | - | Azul |
| Riesgo critico | Riesgo Critico | "requiere atencion" | Rojo (delta_color='inverse') |
| Prximo mantenimiento | Prximo Mantenimiento | fecha | Naranja |
| Riesgo promedio | Riesgo Promedio | porcentaje | Verde |

---

## 4. Pestanas principales (st.tabs)

### 4.1 Tab 1 — Identificar (Riesgo)
- st.error: Alerta de maquinas en nivel critico (atencion inmediata)
- st.dataframe: Tabla interactiva con colores por nivel de riesgo
- st.bar_chart: Grafico de barras de riesgo por maquina

### 4.2 Tab 2 — Comprender (Senales)
- Columna 1: st.selectbox (sensor) + st.line_chart (telemetria)
- Columna 2: st.expander con historico de errores por maquina
- Layout: st.columns([2, 1]) para dos columnas

### 4.3 Tab 3 — Priorizar (Accion)
- st.info: Explicacion de criterio de priorizacion (riesgo x criticidad x impacto)
- Lista de tareas ordenadas por prioridad
- st.success: Recomendacion de intervencion con justificacion

---

## 5. Paleta de colores

| Estado | Color | Uso |
|---|---|---|
| Critico | Rojo #ff4b4b | Alertas, delta rojo |
| Moderado | Naranja #ffa500 | Warning |
| Estable | Verde #28a745 | Success |
| Neutro | Gris #6c757d | Info, caption |
| Fondo | Blanco #ffffff | Clean background |

---

## 6. Responsive

- layout='wide': Contenedor principal ancho
- st.columns(): Se adapta automaticamente a moviles (1 columna en pantallas pequenas)
- st.sidebar(): Se oculta en moviles (boton hamburguesa)
- Sin CSS personalizado: solo componentes nativos de Streamlit

---

## 7. Mock data placeholder

El archivo utils/data_loader.py contiene datos de ejemplo:
- 6 maquinas (CNC, Torno, Fresadora, Bomba, Transportador)
- Riesgo calculado (score 0-100)
- Telemetria 30 dias (temperatura, vibracion, presion)
- Historico de errores (5 registros)

Cuando el modelo ML este listo: Reemplazar esta logica por lectura real de data/processed/ y predicciones del modelo.

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