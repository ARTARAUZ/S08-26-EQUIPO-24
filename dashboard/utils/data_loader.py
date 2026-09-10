"""Carga de datos de ejemplo (mock data placeholder).

Este módulo simula la carga de datasets reales (PdM_telemetry, PdM_failures, etc.).
Cuando el modelo ML esté listo, reemplazar esta lógica por lectura real de data/raw/.
"""

import pandas as pd
import numpy as np


def load_mock_data():
    """Retorna datasets de ejemplo para el dashboard skeleton.

    Returns:
        df_machines: DataFrame con información de las máquinas.
        df_risk: DataFrame con ranking de riesgo calculado.
        df_telemetry: DataFrame con datos de telemetría por máquina y tiempo.
        df_errors: DataFrame con histórico de errores/alarmas.
    """
    # ── Máquinas ──
    df_machines = pd.DataFrame({
        'machine_id': ['CNC-001', 'CNC-002', 'LATHE-003', 'MILL-004', 'PUMP-005', 'CONV-006'],
        'type': ['CNC', 'CNC', 'Torno', 'Fresadora', 'Bomba', 'Transportador'],
        'location': ['Planta A', 'Planta A', 'Planta B', 'Planta B', 'Planta C', 'Planta C'],
        'operating_hours': [8420, 6210, 12350, 5180, 9470, 7320],
        'last_maintenance': ['2026-07-24', '2026-08-12', '2026-06-30', '2026-08-20', '2026-07-05', '2026-08-15'],
        'days_since_maintenance': [45, 27, 70, 19, 65, 24],
        'next_maintenance': ['2026-10-15', '2026-09-20', '2026-10-01', '2026-09-25', '2026-10-10', '2026-09-30'],
    })

    # ── Riesgo (mock del modelo ML futuro) ──
    df_risk = pd.DataFrame({
        'machine_id': ['CNC-001', 'CNC-002', 'LATHE-003', 'MILL-004', 'PUMP-005', 'CONV-006'],
        'risk_score': [87, 62, 12, 91, 45, 38],
        'risk_level': ['Crítico', 'Moderado', 'Estable', 'Crítico', 'Moderado', 'Estable'],
        'criticality': ['Alta', 'Alta', 'Media', 'Alta', 'Media', 'Baja'],
        'priority_score': [36, 70, 6, 45, 9, 6],
        'priority': ['Inspeccionar', 'Monitorear', 'Ninguna', 'Intervenir', 'Revisar', 'Ninguna'],
    })

    # ── Telemetría (mock de sensores) ──
    np.random.seed(42)
    days = pd.date_range('2026-09-01', periods=30, freq='D')
    machines = df_machines['machine_id'].tolist()
    rows = []
    for m in machines:
        base_temp = np.random.uniform(60, 70)
        base_vib = np.random.uniform(2, 4)
        for d in days:
            rows.append({
                'machine_id': m,
                'timestamp': d,
                'temperature': base_temp + np.random.normal(0, 3) + (5 if m == 'MILL-004' else 0),
                'vibration': base_vib + np.random.normal(0, 0.5) + (2 if m == 'MILL-004' else 0),
                'pressure': np.random.uniform(5.5, 6.5),
            })
    df_telemetry = pd.DataFrame(rows)

    # ── Errores (mock de PdM_errors) ──
    df_errors = pd.DataFrame({
        'machine_id': ['CNC-001', 'MILL-004', 'CNC-001', 'PUMP-005', 'LATHE-003'],
        'timestamp': ['2026-09-05', '2026-09-03', '2026-08-28', '2026-09-01', '2026-08-15'],
        'error_code': ['E102', 'E205', 'E101', 'E300', 'E102'],
        'description': [
            'Sobrecalentamiento en spindle',
            'Vibración excesiva en eje principal',
            'Pérdida de posición del husillo',
            'Fuga de fluido hidráulico',
            'Desalineación de corredera'
        ],
    })

    return df_machines, df_risk, df_telemetry, df_errors