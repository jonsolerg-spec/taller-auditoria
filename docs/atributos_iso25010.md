# Bloque 1: problemas del caso y atributos ISO/IEC 25010:2023

| # | Problema del caso | Característica ISO/IEC 25010:2023 | Subcaracterística | Justificación |
|---|---|---|---|---|
| 1 | Defectos escapados a producción | Fiabilidad | Faultlessness (ausencia de fallos) | Los defectos llegan al usuario final sin detectarse antes del despliegue |
| 2 | Pruebas 100% manuales | Mantenibilidad | Testability | Sin automatización, el costo de verificar cada cambio crece y limita detectar regresiones |
| 3 | Despliegues concentrados el viernes | Fiabilidad | Recoverability | Ante una falla, el equipo tiene menos tiempo hábil para recuperarse, lo que aumenta el MTTR |
| 4 | Ausencia de pipeline automatizado | Mantenibilidad | Modifiability / Analysability | Los cambios pequeños requieren verificación manual costosa |
| 5 | Manejo de datos sensibles de pacientes | Seguridad (Security) | Confidentiality, Integrity, Accountability | Los datos de salud requieren protección estricta bajo la Ley 1581 de 2012 |
| 6 | Ciclo fijo de dos semanas sin holgura | Flexibilidad | Adaptability | El proceso no se adapta cuando aparecen defectos críticos cerca del cierre del sprint |
| 7 | Falta de alertas ante citas duplicadas | Seguridad física (Safety) | Risk identification, Fail safe | Un error en la asignación de citas puede afectar la atención del paciente |
| 8 | Errores frecuentes en el flujo de agendamiento | Capacidad de interacción | User error protection | Los defectos rompen los flujos de uso y generan frustración en el usuario |
