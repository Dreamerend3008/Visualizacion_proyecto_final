Diccionario de variables

Clima

ONI: promedio móvil de 3 meses de la anomalía de temperatura del Pacífico ecuatorial. TOTAL es la temperatura; ANOM es la desviación frente a la normal. ≥ +0,5 °C es El Niño; ≤ -0,5 °C, La Niña.
RONI: ONI relativo, es decir, ajustado restando el calentamiento promedio de todo el trópico. Es la versión que NOAA/CPC está adoptando como oficial.
precipitacion_total_mm: lluvia diaria promedio del mes (mm/día), promedio de los 12 departamentos.
temp_promedio_c / temp_maxima_c: temperatura media y máxima diaria, promediadas por mes y departamento.

Hidrología

aportes_hidricos: energía equivalente al agua que entra a los embalses (GWh). Mide la oferta hídrica del momento.
media_historica_aportes: valor promedio histórico de los aportes para ese periodo. Aportes / media = anomalía hidrológica (por debajo de 1, hay sequía).
volumen_util_energia: energía almacenada en los embalses y realmente utilizable (GWh). Es el nivel de “tanque” del sistema. Se da total y por embalse.

Operación

generacion_real: energía efectivamente generada por el SIN (GWh), de todas las fuentes. No separa hidráulica y térmica.
demanda_real_sin: energía consumida en el SIN según medición (GWh).
demanda_comercial_reg: demanda facturada por los comercializadores (GWh). Difiere de la real por pérdidas y diferencias de medición/liquidación.

Mercado

precio_bolsa_nacional: precio promedio de la energía en el mercado mayorista (COP/kWh). Sube cuando hay que despachar térmicas.

Proyección UPME

demanda_sin_esc_medio: demanda proyectada del SIN en el escenario central (GWh).
ic_sup / ic_inf 68 y 95: límites superior e inferior de los intervalos de confianza al 68 % y 95 % de esa proyección.

Columnas estructurales

year-month, year, month: llaves temporales.
Id, Name, Value_GWh (embalses): código, nombre y valor del volumen útil por embalse.