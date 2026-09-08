# Criterios de Éxito

Este documento define cómo medimos el éxito del proyecto PredictiveMaintenance.

---

## Criterio de éxito oficial

El sistema debe permitir que un responsable de mantenimiento, **sin revisar manualmente grandes cantidades de sensores o múltiples registros históricos**, pueda:

1. **IDENTIFICAR** ¿Qué máquinas presentan mayor riesgo de falla?
2. **COMPRENDER** ¿Qué señales o variables justifican ese riesgo?
3. **PRIORIZAR** ¿Qué máquina debería atenderse primero?

---

## Matriz de criterios

| Criterio | Qué debe permitir | Evidencia final |
|---|---|---|
| Identificar riesgo | Detectar máquinas de mayor riesgo | Ranking de máquinas con score de riesgo |
| Comprender riesgo | Conocer señales relevantes | Explicación del score por variable |
| Priorizar | Decidir qué atender primero | Riesgo + criticidad → prioridad |
| Evitar análisis manual | Sintetizar información | Dashboard con resumen y alertas |
| Apoyar decisión preventiva | Indicar prioridad/acción | Recomendación de intervención |

---

## Prueba de aceptación final

El producto solo podrá considerarse exitoso si:

1. El sistema responde **qué máquina tiene mayor riesgo**.
2. El sistema explica **por qué**.
3. El sistema permite identificar **cuál debe atenderse primero**.
4. El usuario **no necesita revisar manualmente** grandes volúmenes de datos.
5. La información permite tomar una **decisión preventiva**.

---

## Criterios de aceptación por capa

### Capa de datos
- [ ] Dataset seleccionado y justificado
- [ ] Diccionario de datos disponible
- [ ] Limpieza aplicada (nulos, inconsistencias, duplicados)
- [ ] Variables relevantes identificadas
- [ ] Separación train/validation/test definida

### Capa de modelo
- [ ] Baseline definido
- [ ] Modelo(s) candidato(s) evaluado(s)
- [ ] Score de riesgo interpretable
- [ ] Validación realizada
- [ ] Explicabilidad incluida

### Capa de dashboard
- [ ] Resumen general
- [ ] Estado de máquinas
- [ ] Ranking de riesgo
- [ ] Prioridad
- [ ] Detalle de máquina
- [ ] Explicación del riesgo

---

## Estado actual

**FASE:** Discovery / Project Setup

**Estado:** Documentación de criterios definida. El modelo, dataset y dashboard aún no existen.