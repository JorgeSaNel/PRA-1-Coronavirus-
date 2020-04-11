# PRA 1 - Relación entre el PIB Per Cápita y Casos de Coronavirus confirmados 

## Descripción
Esta práctica se ha realizado bajo el contexto de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer información relevante al coronavirus a través de Wikipedia - Pandemia de enfermedad por coronavirus de 2019-2020 y del PIB de cada país con el periódico "Expansión" para generar un dataset que en posterioridad se buscarán posibles correlaciones relacione estos los datos.

## Miembros del equipo
La actividad se ha realizado en un grupo de dos personas formado por:

* Jorge Santos Neila - JorgeSaNel - [GitHub](https://github.com/JorgeSaNel).
* Javier Cela López - PENDIENTE

## Ficheros del código fuente

* **src/main.py**: punto de entrada al programa. Inicia el proceso de scraping.
* **src/COVID19Scraper**: contiene la implementación de la clase _COVID19Scraper_ cuyos métodos generan el conjunto de datos a partir de la información obtenida a través del periódico [Expansión - PIB Per Cápita](https://datosmacro.expansion.com/pib) y [Wikipedia - Casos por coronavirus](https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2019-2020). En la primera página se obtienen los datos relativos al PIB Per Cápita de cada país, y se cruzan con los casos de coronavirus en el mundo, obtenidos a través de la segunda página web.

## Recursos

1. Pandemia de enfermedad por coronavirus de 2019-2020 (2020)
2. Datos del PIB Per Cápita Mundial (2019)
3. Subirats, L., Calvo, M. (2018). Web Scraping. Editorial UOC.
4. Masip, D. El lenguaje Python. Editorial UOC.
5. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
6. Simon Munzert, Christian Rubba, Peter Meißner, Dominic Nyhuis. (2015). _Automated Data Collection with R: A Practical Guide to Web Scraping and Text Mining_. John Wiley & Sons.
