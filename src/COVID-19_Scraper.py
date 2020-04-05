from bs4 import BeautifulSoup

class COVID19Scraper():

    def __init__(self):

        self.urlWorldometers = 'https://www.worldometers.info/coronavirus/#countries'
        self.urlPIB = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_PIB_(nominal)'