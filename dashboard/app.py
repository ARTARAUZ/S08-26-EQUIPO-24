import streamlit as st

st.set_page_config(
    page_title='PredictiveMaintenance',
    page_icon='🔧',
    layout='wide'
)

st.title('PredictiveMaintenance')
st.caption('MVP en desarrollo - Fase: Discovery / Project Setup')

st.divider()

st.subheader('Estado del proyecto')
st.info('El repositorio se encuentra en fase de preparación y discovery. El modelo ML y el dashboard aún no están implementados.')

st.divider()

st.subheader('Las 3 preguntas del producto')

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('### 1. Identificar')
    st.write('¿Qué máquinas tienen mayor riesgo de falla?')

with col2:
    st.markdown('### 2. Comprender')
    st.write('¿Qué señales o variables justifican ese riesgo?')

with col3:
    st.markdown('### 3. Priorizar')
    st.write('¿Qué máquina debería atenderse primero?')

st.divider()

st.warning('Próximamente: ranking de riesgo, explicación y priorización de máquinas.')

