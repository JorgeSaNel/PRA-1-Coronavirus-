# PRA 1 - Relación entre el PIB Per Cápita y Casos de Coronavirus confirmados 

## Descripción
Esta práctica se ha realizado bajo el contexto de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer información relevante al coronavirus a través de Wikipedia - Pandemia de enfermedad por coronavirus de 2019-2020 y del PIB de cada país con el periódico "Expansión" para generar un dataset para que en posterioridad se busquen correlaciones entre estos datos.

## Miembros del equipo
La actividad se ha realizado en un grupo de dos personas formado por:

* Jorge Santos Neila - [JorgeSaNel en GitHub](https://github.com/JorgeSaNel).
* Javier Cela López - [Javcela10 en GitHub](https://github.com/javcela10).

## Ficheros del código fuente

* **src/main.py**: punto de entrada al programa. Inicia el proceso de scraping.
* **src/COVID19Scraper**: contiene la implementación de la clase _COVID19Scraper_ cuyos métodos generan el conjunto de datos a partir de la información obtenida a través del periódico [Expansión - PIB Per Cápita](https://datosmacro.expansion.com/pib) y [Wikipedia - Casos por coronavirus](https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2019-2020). En la primera página se obtienen los datos relativos al PIB Per Cápita de cada país, y se cruzan con los casos de coronavirus en el mundo, obtenidos a través de la segunda página web.

## Licencia
Este proyecto está bajo la licencia CC BY-NC-SA 4.0, [Atribución-NoComercial-CompartirIgual 4.0 Internacional](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode), la cual permite:

* Compartir: copiar y redistribuir el material en cualquier medio o formato
* Adaptar: remezclar, transformar y construir a partir del material 

Siempre y cuando se sigan los siguientes términos:

* Atribución: Se debe dar crédito de manera adecuada, brindar un enlace a la licencia, e indicar si se han realizado cambios. Puede hacerlo en cualquier forma razonable, pero no de forma tal que sugiera que usted o su uso tienen el apoyo del licenciante.
* Sin uso comercial: No puede hacer uso del material con propósitos comerciales.
* Compartir por igual: Si remezcla, transforma o crea a partir del material, debe distribuir su contribución bajo la misma licencia del original. 

## DOI - Zenodo
Asimismo, se puede encontrar información adicional en [Zenodo](https://doi.org/10.5281/zenodo.3749286)

## Recursos

1. Pandemia de enfermedad por coronavirus de 2019-2020 (2020)
2. Datos del PIB Per Cápita Mundial (2019)
3. Subirats, L., Calvo, M. (2018). Web Scraping. Editorial UOC.
4. Masip, D. El lenguaje Python. Editorial UOC.
5. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
6. Simon Munzert, Christian Rubba, Peter Meißner, Dominic Nyhuis. (2015). _Automated Data Collection with R: A Practical Guide to Web Scraping and Text Mining_. John Wiley & Sons.
