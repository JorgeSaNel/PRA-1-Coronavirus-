#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os
from bs4 import BeautifulSoup
from urllib2 import urlopen

class COVID19Scraper():

    def __init__(self):

        self.urlCoronavirus = 'https://es.wikipedia.org/wiki/Pandemia_de_enfermedad_por_coronavirus_de_2019-2020'
        self.urlPIB = 'https://datosmacro.expansion.com/pib'

    def ObtenerDatosCoronavirus(self, soup):
        start = False

        # Se inicializa el DataFrame
        columns = ["Paises", "Continente", "Casos Positivos", "CxM Habitantes", "Fallecidos", "Porcentaje Fallecidos",
                   "FxM Habitantes", "Recuperados", "Porcentaje Recuperados"]
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
                    if (texto_inicial == '233 territorios o transportes'):
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
                        por_fallecidos = td[3].text
                        fxmhab = td[4].text.strip('\n').replace('.', ',')
                        recuperados = td[5].text
                        por_recuperados = td[6].text.strip('\n')

                        # Se insertan los valores recogidos en el dataframe
                        df2 = pd.DataFrame([[pais, continente, casos_positivos, cxmhab, fallecidos, por_fallecidos,
                                             fxmhab, recuperados, por_recuperados]], columns=columns)
                        df = df.append(df2)

        df = df.set_index("Paises")
        df.index = df.index.str.replace('[\(\[].*?[\)\]]', '')

        return df

    def ObtenerDataframeCoronavirus(self):
        html = urlopen(self.urlCoronavirus)
        soup = BeautifulSoup(html, 'html.parser')

        # Se recupera la tabla de casos del Coronavirus
        return self.ObtenerDatosCoronavirus(soup)

    def ObtenerDatosPIB(self, soup, ID, columns):
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
                        euro = cells[2].attrs[
                            'data-value']  # .text.replace("M.€", "").replace("€", "")#.replace(".", "")
                        dolar = cells[4].attrs[
                            'data-value']  # .text.replace("M.$", "").replace("$", "")#.replace(".", "")
                        variacion = cells[6].attrs['data-value']  # .text

                        # Se insertan los valores recogidos en el dataframe
                        df2 = pd.DataFrame([[country, annio, euro, dolar, variacion]], columns=columns)
                        df = df.append(df2)

        df = df.set_index("Paises")
        return df

    def ObtenerDataframePIB(self):
        html = urlopen(self.urlPIB)
        soup = BeautifulSoup(html, 'html.parser')

        # Se recupera la tabla PIB Anual
        columns_anual = ["Paises", "Anio", "PIB Anual (M.E)", "PIB Anual (M.D)", "Var PIB Anual"]
        df_anual = self.ObtenerDatosPIB(soup, "tbA", columns_anual)

        # Se recupera la tabla PIB Per Capita
        columns_per_capita = ["Paises", "Anio", "PIB Per Capita (E)", "PIB Per Capita (D)", "Var PIB Per Capita"]
        df_per_capita = self.ObtenerDatosPIB(soup, "tbPC", columns_per_capita)

        # Merges entre los DataFrames
        df_final = pd.merge(df_anual, df_per_capita, left_index=True, right_index=True)[
            ['Anio_x', 'PIB Anual (M.E)', 'PIB Anual (M.D)', 'Var PIB Anual', 'PIB Per Capita (E)',
             'PIB Per Capita (D)', 'Var PIB Per Capita']]
        return df_final

    def CodificacionFichero(self, dataframe):

        for col in dataframe.columns:
            dataframe[col] = dataframe[col].str.encode('utf-8')

        return dataframe

    def ObtenerDataframeCompleto(self):

        df_coronavirus = self.ObtenerDataframeCoronavirus()
        df_pib = self.ObtenerDataframePIB()

        return self.CodificacionFichero(pd.merge(df_coronavirus, df_pib, how='inner', on='Paises'))

    def GuardarFichero(self, dataframe, ruta, nombre_fichero):
        # Se comprueba si existe el directorio CSV para guardar el fichero
        if not os.path.exists(ruta):
            os.makedirs(ruta)

        dataframe.to_csv(ruta + nombre_fichero, index=True, header=True, sep=";", encoding='utf-8')