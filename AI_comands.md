1. Utilizamos el modelo gpt-5.6-sol desplegado en microsoft AI foundry para agrupar, limpiar, estandarizar la data, de manera que facilite la exploracion de la data debido a las multiples fuentes que estamos utilizando ademas de la cantidad de variables que se vieron involucradas.

hello, your job is to make a python script as simple as posible, that does the following,
 reads data/raw and outputs multiple .csv of clean data, multiple .csv are in raw so your
 task is to evaluate which of them are on days/months/year your output can only have 2
 intervals of time months and years, so if data is on days please get the average and make
 it monthly. Also i believe there is data in multiple formats kWh/GWh please standarize
 them into GWh, the script should be called cleaning and i could call it inside of a
 notebook as a function. mantain the integrity of the data.

if you see the output data there are some problems. 1: some columns still are in fact in hour/day data so please read the columns of each dataset including 1 row of example data, and
 make sure the output includes that info in that format. also include at the end 2 files that contains info of each dataset possible one that has every parameter analized in months and
 one that has each parameter analized in years. make it so the monnthly data is only from the datasets that have info monthly/daily/hourly not yearly by dividing it by 12. but yearly
 that has the information for each year for example the file data/raw/aportes_hidricos.csv the column value would need to appear in monthly but also in yearly.

 for the last .csv the information of each column needs to be related with the name of the original file, assing a name for each columns

 if a file has the data segmented in locations or something like that check if exists a table that has all that info resumed for the coountry otherwise make an average.


Tambien utilizamos ia para obtener una funcion para mostrar la temporalidad de cada columna del conjunto de dataset mensual y anual.
Para facilitar el proceso de decision de las visualizaciones.


# Parte de creación del reporte...

### Prompt de recomendaciones de workflow y de herramientas

Hola claude
Estoy trabajando en un reporte para visualización de datos. Tengo los siguientes datasets  cargados en pandas:

all_parameters_yearly
<class 'pandas.DataFrame'>
RangeIndex: 91 entries, 0 to 90
Data columns (total 19 columns):
 #   Column                                                   Non-Null Count  Dtype  
---  ------                                                   --------------  -----  
 0   year                                                     91 non-null     int64  
 1   aportes_hidricos__Value_GWh                              27 non-null     float64
 2   clima_colombia_diario_2000_2026__precipitacion_total_mm  27 non-null     float64
 3   clima_colombia_diario_2000_2026__temp_promedio_c         27 non-null     float64
 4   clima_colombia_diario_2000_2026__temp_maxima_c           27 non-null     float64
 5   cpc_oni_historico__TOTAL                                 77 non-null     float64
 6   cpc_oni_historico__ANOM                                  77 non-null     float64
 7   cpc_roni_historico__ANOM                                 77 non-null     float64
 8   demanda_comercial_reg__Value_GWh                         27 non-null     float64
 9   demanda_real_sin__Value_GWh                              27 non-null     float64
 10  generacion_real__Value_GWh                               27 non-null     float64
 11  media_historica_aportes__Value_GWh                       27 non-null     float64
 12  precio_bolsa_nacional__Value                             27 non-null     float64
 13  upme_proyeccion_sin_mensual__demanda_sin_esc_medio_gwh   15 non-null     float64
 14  upme_proyeccion_sin_mensual__ic_sup_95_gwh               15 non-null     float64
 15  upme_proyeccion_sin_mensual__ic_inf_95_gwh               15 non-null     float64
 16  upme_proyeccion_sin_mensual__ic_sup_68_gwh               15 non-null     float64
 17  upme_proyeccion_sin_mensual__ic_inf_68_gwh               15 non-null     float64
 18  volumen_util_energia_sistema__Value_GWh                  27 non-null     float64
dtypes: float64(18), int64(1)
memory usage: 13.6 KB

all_parameters_monthly
<class 'pandas.DataFrame'>
RangeIndex: 1092 entries, 0 to 1091
Data columns (total 21 columns):
 #   Column                                                   Non-Null Count  Dtype  
---  ------                                                   --------------  -----  
 0   year-month                                               1092 non-null   str    
 1   year                                                     1092 non-null   int64  
 2   month                                                    1092 non-null   int64  
 3   aportes_hidricos__Value_GWh                              323 non-null    float64
 4   clima_colombia_diario_2000_2026__precipitacion_total_mm  323 non-null    float64
 5   clima_colombia_diario_2000_2026__temp_promedio_c         323 non-null    float64
 6   clima_colombia_diario_2000_2026__temp_maxima_c           323 non-null    float64
 7   cpc_oni_historico__TOTAL                                 921 non-null    float64
 8   cpc_oni_historico__ANOM                                  921 non-null    float64
 9   cpc_roni_historico__ANOM                                 921 non-null    float64
 10  demanda_comercial_reg__Value_GWh                         323 non-null    float64
 11  demanda_real_sin__Value_GWh                              323 non-null    float64
 12  generacion_real__Value_GWh                               323 non-null    float64
 13  media_historica_aportes__Value_GWh                       323 non-null    float64
 14  precio_bolsa_nacional__Value                             323 non-null    float64
 15  upme_proyeccion_sin_mensual__demanda_sin_esc_medio_gwh   177 non-null    float64
 16  upme_proyeccion_sin_mensual__ic_sup_95_gwh               177 non-null    float64
 17  upme_proyeccion_sin_mensual__ic_inf_95_gwh               177 non-null    float64
 18  upme_proyeccion_sin_mensual__ic_sup_68_gwh               177 non-null    float64
 19  upme_proyeccion_sin_mensual__ic_inf_68_gwh               177 non-null    float64
 20  volumen_util_energia_sistema__Value_GWh                  323 non-null    float64
dtypes: float64(18), int64(2), str(1)
memory usage: 179.3 KB

volumen_util_energia_embalse
<class 'pandas.DataFrame'>
RangeIndex: 6870 entries, 0 to 6869
Data columns (total 6 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   Date       6870 non-null   str    
 1   year       6870 non-null   int64  
 2   month      6870 non-null   int64  
 3   Id         6870 non-null   str    
 4   Name       6870 non-null   str    
 5   Value_GWh  6870 non-null   float64
dtypes: float64(1), int64(2), str(3)
memory usage: 322.2 KB

Además, tengo esta documentación de la intención del proyecto (lee solo lo principal).

Tengo que hacer un reporte, estaba pensando en hacerlo en Tableau o en Flourish + html, pero me da miedo que se complique dado que no sé hacer frontend.

Dame recomendaciones. Durante el chat, además, se conciso, no des vueltas ni explicaciones demasiado largas. Al grano.

### Prompt para ir guiando el reporte
`Nótese que` Claude me dijo que con la data limpia que tenemos no se puede contestar adecuadamente la pregunta que habíamos formulado 
```plaintext
¿De qué manera las anomalías climáticas del fenómeno de el niño impactan el margen entre la demanda real y pronosticada de energía en el SIN y como se refleja esta presión operativa en las dinámicas del mercado eléctrico colombiano?
``` 
De tal modo, que usé este prompt para dirigir el trabajo:

Ok, teniendo en cuenta eso, trabajaré en Tableau. Tengo licencia estudiantil.  

Me gustaría que me dieras recomendaciones de gráficas (solo dime relaciones entre variables, que yo escojo el gráfico).

Le sugeriré a mis compañeros cambiar el objetivo de la investigación

Dado el contexto que tienes, también sugiereme algunas preguntas que podamos responder con estos datos, encaminadas un poco a lo que queríamos mirar. Explicame a qué van dirigidas.

#### ¿Qué decido?
En este punto le consulté a Fabián (es el único despierto) sobre las sugerencias de la IA. Vamos a cambiar el objetivo de la investigación a el siguiente (es un poco un mix sobre lo que Claude sugiere):
```plaintext
¿Qué tan rápido el fenómeno del niño (ONI) genera reacciones en el mercado de energía, aportes hídricos, volumen útil de energía y más indicadores relacionados?
```
algo por el estilo....

### Prompt para sugerencia de creación de columna previa a hacer el reporte
Estuve analizando a profundidad las columnas, no crees que crear una columna que sea como fen_nino, que tenga la regla de la desviación estándar de la temperatura de tipo categórico, para que el motor la procese mejor estaría bien?

### Prompt para generar código para crear la columna
