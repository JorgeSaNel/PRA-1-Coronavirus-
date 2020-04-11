from COVID19Scraper import COVID19Scraper

nombre_fichero = 'Coronavirus.csv'
ruta = '../csv/'

scraper = COVID19Scraper()
df = scraper.ObtenerDataframeCompleto()
scraper.GuardarFichero(df, ruta, nombre_fichero)
