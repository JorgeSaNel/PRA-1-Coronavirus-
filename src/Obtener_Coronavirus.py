#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib2 import urlopen


# In[2]:


def ObtenerDataframeCoronavirus(soup):
    start = False

    # Se inicializa el DataFrame
    columns = ["Paises", "Continente", "Casos Positivos", "CxM Habitantes", "Fallecidos", "Porcentaje Fallecidos", "FxM Habitantes", "Recuperados", "Porcentaje Recuperados"]
    df = pd.DataFrame(columns=columns)
    
    # Se recorren los elementos de la tabla
    tables = soup.find_all('table')
    
    for table in tables:
        rows = table.find_all('tr')

        for row in rows:
            th = row.find_all('th')

            if (len(th) > 1): 
                texto_inicial = th[0].text.strip('\n')

                # Analizando el código HTML, se observa que se puede empezar a coger datos cuando se cumple esta condición
                if texto_inicial.find('territorios o transportes') > 0:
                    start = True
                    continue
                elif (texto_inicial == '#'):
                # Se deja de coger datos cuando se cumple esta otra condición
                    start = False
                    break

                if start:
                    td = row.find_all('td')

                    # TO-DO: eliminar numeros de los paises
                    # TO-DO: eliminar espacios en blanco de los numeros (ej: casos positivos)

                    # Se eliminan del pais los saltos de linea, los espacios en blanco al principio, y los números y parénteris
                    pais = th[0].text.strip('\n').lstrip()
                    continente = th[1].text.strip('\n')
                    # Se sustituye el espacio en blanco por un punto
                    casos_positivos = td[0].text.replace(' ', '.')
                    # Se sustituye el punto por coma para representar a los decimales
                    cxmhab = td[1].text.strip('\n').replace('.', ',')
                    fallecidos = td[2].text.replace(' ', '.')
                    por_fallecidos =td[3].text
                    fxmhab = td[4].text.strip('\n').replace('.', ',')
                    recuperados = td[5].text
                    por_recuperados = td[6].text.strip('\n')

                    # Se insertan los valores recogidos en el dataframe
                    df2 = pd.DataFrame([[pais, continente, casos_positivos, cxmhab, fallecidos, por_fallecidos, fxmhab, recuperados, por_recuperados]], columns=columns)
                    df = df.append(df2)

    df = df.set_index("Paises")
    df.index = df.index.str.replace('[\(\[].*?[\)\]]', '')

    return df


# In[3]:


def GuardarFichero(dataframe, ruta, nombre_fichero):
    import os
    # Se comprueba si existe el directorio CSV para guardar el fichero
    if not os.path.exists(ruta):
        os.makedirs(ruta)

    dataframe.to_csv(ruta + nombre_fichero, index=True, header=True, sep=";", encoding='utf-8')


# In[4]:


def ObtenerCasosCoronavirus(url):
    html = urlopen(url) 
    soup = BeautifulSoup(html, 'html.parser')

    # Se recupera la tabla de casos del Coronavirus
    return ObtenerDataframeCoronavirus(soup)

def CambiarCodificacionFicheroCoronavirus(dataframe):

    for col in dataframe.columns:
        dataframe[col] = dataframe[col].str.encode('utf-8')

    return dataframe



# In[7]:


nombre_fichero = 'CasosCoronavirus.csv'
ruta = "../csv/"
url = 'https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2019-2020'

df_coronavirus = ObtenerCasosCoronavirus(url)
df_coronavirus = CambiarCodificacionFicheroCoronavirus(df_coronavirus)
GuardarFichero(df_coronavirus, ruta, nombre_fichero)

