import streamlit as st

from components.risk_table import render_risk_table
from components.sensor_chart import render_sensor_chart
from components.machine_detail import render_machine_detail
from components.priority_list import render_priority_list
from utils.data_loader import load_mock_data

st.set_page_config(
    page_title='PredictiveMaintenance',
    page_icon='🔧',
    layout='wide',
    initial_sidebar_state='expanded'
)

# ── Carga de datos de ejemplo (placeholder) ──
df_machines, df_risk, df_telemetry, df_errors = load_mock_data()

# ═══════════════════════════════════════════════
# BARRA LATERAL
# ═══════════════════════════════════════════════
with st.sidebar:
    st.title('🔧 PredictiveMaintenance')
    st.caption('Código: S08-26-EQUIPO-24')
    st.divider()

    # Selector de máquina
    machine_ids = df_machines['machine_id'].tolist()
    selected_machine = st.selectbox(
        ' Máquina',
        options=machine_ids,
        index=0
    )

    # Filtro de estado
    status_options = ['Crítico', 'Moderado', 'Estable']
    selected_status = st.multiselect(
        ' Filtro de estado',
        options=status_options,
        default=['Crítico', 'Moderado', 'Estable']
    )

    # Filtro de criticidad
    criticality_options = ['Alta', 'Media', 'Baja']
    selected_criticality = st.multiselect(
        ' Filtro de criticidad',
        options=criticality_options,
        default=criticality_options
    )

    st.divider()

    # Metadatos rápidos de la máquina seleccionada
    machine_row = df_machines[df_machines['machine_id'] == selected_machine].iloc[0]
    st.subheader(' Metadatos')
    st.write(f'**ID:** {machine_row["machine_id"]}')
    st.write(f'**Tipo:** {machine_row["type"]}')
    st.write(f'**Ubicación:** {machine_row["location"]}')
    st.write(f'**Horas operación:** {machine_row["operating_hours"]} h')
    st.write(f'**Último mantenimiento:** {machine_row["last_maintenance"]}')
    st.write(f'**Días sin mantenimiento:** {machine_row["days_since_maintenance"]}')

# ═══════════════════════════════════════════════
# CONTENEDOR PRINCIPAL
# ═══════════════════════════════════════════════
st.title('PredictiveMaintenance')
st.caption('Fase: Discovery / MVP Dashboard')

st.divider()

# Fila de KPIs principales
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(
        label=' Máquinas Monitoreadas',
        value=len(df_machines)
    )

with kpi2:
    critical_count = len(df_risk[df_risk['risk_level'] == 'Crítico'])
    st.metric(
        label=' Riesgo Crítico',
        value=critical_count,
        delta='requiere atención',
        delta_color='inverse'
    )

with kpi3:
    st.metric(
        label=' Próximo Mantenimiento',
        value=df_machines['next_maintenance'].min()
    )

with kpi4:
    avg_risk = df_risk['risk_score'].mean()
    st.metric(
        label=' Riesgo Promedio',
        value=f'{avg_risk:.0f}%'
    )

st.divider()

# Pestañas principales — Las 3 preguntas del producto
tab1, tab2, tab3 = st.tabs([
    ' 1. Identificar (Riesgo)',
    ' 2. Comprender (Señales)',
    ' 3. Priorizar (Acción)'
])

# ── Pestaña 1: Identificar ──
with tab1:
    st.subheader('Ranking de Riesgo')

    # Alerta de máquinas críticas
    critical_machines = df_risk[df_risk['risk_level'] == 'Crítico']['machine_id'].tolist()
    if critical_machines:
        st.error(
            f' **Atención inmediata:** {len(critical_machines)} máquina(s) en nivel crítico: '
            f'{", ".join(critical_machines)}'
        )

    # Tabla interactiva de riesgo
    render_risk_table(df_risk, selected_status, selected_criticality)

    st.divider()
    st.subheader(' Distribución de Riesgo')
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.bar_chart(
            df_risk.set_index('machine_id')['risk_score']
        )
    with col_chart2:
        st.dataframe(
            df_risk[['machine_id', 'risk_score', 'risk_level', 'criticality', 'priority']],
            use_container_width=True,
            hide_index=True
        )

# ── Pestaña 2: Comprender ──
with tab2:
    st.subheader(f' Señales — {selected_machine}')

    # Layout de dos columnas
    col_sensors, col_detail = st.columns([2, 1])

    with col_sensors:
        st.write('**Telemetría de sensores**')
        render_sensor_chart(df_telemetry, selected_machine)

    with col_detail:
        st.write('**Histórico de errores**')
        render_machine_detail(df_errors, selected_machine)

    st.divider()
    st.subheader(' Señales relevantes')
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.info('**Vibración**\n\n↑ +32% vs. baseline\n\nUmbral: 4.5 mm/s')
    with col_s2:
        st.warning('**Temperatura**\n\n↑ +18% vs. baseline\n\nUmbral: 72°C')
    with col_s3:
        st.success('**Presión**\n\n→ estable\n\n6.1 bar')

# ── Pestaña 3: Priorizar ──
with tab3:
    st.subheader(' Lista de Prioridad de Mantenimiento')

    st.info(
        ' Las tareas se ordenan por combinación de **riesgo × criticidad × impacto**. '
        'Revisar la máquina con mayor prioridad primero.'
    )

    render_priority_list(df_risk, df_machines)

    st.divider()
    st.subheader(' Recomendación de intervención')
    top_machine = df_risk.sort_values('priority_score', ascending=False).iloc[0]
    st.success(
        f'**Máquina recomendada:** {top_machine["machine_id"]}\n\n'
        f'**Acción:** Inspección programada\n\n'
        f'**Justificación:** Riesgo {top_machine["risk_score"]}%, '
        f'criticidad {top_machine["criticality"]}'
    )