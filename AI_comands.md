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