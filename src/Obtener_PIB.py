#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[2]:


def ObtenerDatos(soup, ID, columns):
    # Hay 4 tipos de tablas con los siguientes IDs:
        ## tbA: PIB Anual
        ## tbPC: PIB Per Capita
        ## tbT: PIB Trimestral
        ## tbPCT: PIB Trim Per Capita

    # Analizamos primero la PIB Anual
    tables = soup.find_all('table', {"id": ID})

    # Se inicializa el DataFrame
    df = pd.DataFrame(columns=columns)

    # Se recorre la tabla
    for table in tables:
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')

            # Tras analizar los diferentes valores de la celda, se observa que:
                ## Celda 0: Contiene el nombre del país
                ## Celda 1: Contiene el año en el que se analizó el PIB
                ## Celda 2: Contiene el PIB expresado en euros
                ## Celda 3: Celda vacía reservada al formato
                ## Celda 4: Contiene el PIB expresado en dólares
                ## Celda 5: Celda vacía reservada al formato
                ## Celda 6: Contiene la variación del PIB respecto al año anterior
                ## Celda 7: Celda vacía reservada al formato
            # Por tando, en el dataset se guardarán las Celdas 0,1,2,4 y 6

            if len(cells) > 1:
                # No se cogen los datos acumulados de la zona euro
                if cells[0].text != "Zona Euro [+]":

                    # Se asignan valores
                    country = cells[0].text.replace(" [+]", "")
                    annio = cells[1].text
                    euro = cells[2].text.replace("M.€", "").replace("€", "")#.replace(".", "")
                    dolar = cells[4].text.replace("M.$", "").replace("$", "")#.replace(".", "")
                    variacion = cells[6].text

                    # Se insertan los valores recogidos en el dataframe
                    df2 = pd.DataFrame([[country, annio, euro, dolar, variacion]], columns=columns)
                    df = df.append(df2)

    df = df.set_index("Paises")
    return df


# In[3]:


def GuardarFichero(dataframe, ruta, nombre_fichero):
    import os
    # Se comprueba si existe el directorio CSV para guardar el fichero
    if not os.path.exists(ruta):
        os.makedirs(ruta)

    dataframe.to_csv (ruta + nombre_fichero, index = True, header=True, sep=";")


# In[4]:


def ObtenerDataframePIB(url):
    html = urlopen(url) 
    soup = BeautifulSoup(html, 'html.parser')

    # Se recupera la tabla PIB Anual
    columns_anual = ["Paises", "Año", "PIB Anual (M.€)", "PIB Anual (M.$)", "Var PIB Anual"]
    df_anual = ObtenerDatos(soup, "tbA", columns_anual)

    # Se recupera la tabla PIB Per Capita
    columns_per_capita = ["Paises", "Año", "PIB Per Capita (€)", "PIB Per Capita ($)", "Var PIB Per Capita"]
    df_per_capita = ObtenerDatos(soup, "tbPC", columns_per_capita)

    # Merges entre los DataFrames
    df_final = pd.merge(df_anual, df_per_capita, left_index=True, right_index=True)
    return df_final

    # TO-DO: Analizar Canada porque hay duplicados, aunque igual se hace en la PRA 2
    # df_final.filter(like='nad', axis=0)


# In[5]:


nombre_fichero = 'PIB.csv'
ruta = "../csv/"
url = 'https://datosmacro.expansion.com/pib'

df_pib = ObtenerDataframePIB(url)
GuardarFichero(df_pib, ruta, nombre_fichero)

