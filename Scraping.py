"""
scraping.py: este script recibe como input el nombre de un medio de prensa 
y la URL de una noticia. Devuelve el título y fecha de publicación de esta noticia.
"""
#Falta Comprobar que el Medio de prensa posea esa noticia.

import sys
import requests
import re
from bs4 import BeautifulSoup #pip install bs4


def Titulo(soup):
    formato = ["h1","title","h2"]

    for i in formato:
        T_encontrado = soup.find(i)
        if T_encontrado:
            print("Titulo de la Noticia: " + T_encontrado.text.strip()) 
            return
        else:
            T_encontrado = "Vacio"
    if T_encontrado == "Vacio":
        print("No se ha encontrado Titulo de la Noticia")
    return

def Fecha(soup):
    #Con esto se abarca cada posibilidad de formato para fecha, ya que si se busca la etiqueta date o time, etc..
    #no asegura encontrar la fecha siempre.
    Formato = [
    r"\d{2}/\d{2}/\d{4}",              # dd/mm/yyyy
    r"\d{2}-\d{2}-\d{4}",              # dd-mm-yyyy
    r"\d{4}/\d{2}/\d{2}",              # yyyy/mm/dd
    r"\d{4}-\d{2}-\d{2}",              # yyyy-mm-dd
    r"\d{2} de [A-Za-z]+ de \d{4}",     # dd de [mes] de yyyy
    r"[A-Za-z]+ \d{2}, \d{4}",          # [mes] dd, yyyy
    r"\d{2}/\d{2}/\d{2}",              # dd/mm/yy
    r"\d{2}-\d{2}-\d{2}",              # dd-mm-yy
    r"\d{2}/\d{2}/\d{2}",              # mm/dd/yy
    r"\d{2}-\d{2}-\d{2}",              # mm-dd-yy
    r"\d{2}/\d{2}/\d{2}",              # yy/mm/dd
    r"\d{2}-\d{2}-\d{2}",              # yy-mm-dd
    r"\d{1,2} [A-Za-z]+ \d{4}",         # d [mes] yyyy
    r"\d{1,2} [A-Za-z]+, \d{4}",        # d [mes], yyyy
    r"\d{1,2} [A-Za-z]+ \d{2}",         # d [mes] yy
    r"\d{1,2} [A-Za-z]+, \d{2}",        # d [mes], yy
    r"[A-Za-z]+ \d{1,2}, \d{4}",        # [mes] d, yyyy
    r"[A-Za-z]+ \d{1,2}, \d{2}",        # [mes] d, yy
    r"\d{1,2}-[A-Za-z]+-\d{2,4}",       # d-[mes]-yy or d-[mes]-yyyy
    r"\d{1,2} [A-Za-z]+",               # d [mes]
    r"[A-Za-z]+ \d{1,2}"                # [mes] d
    ]

    for i in Formato:
        F_encontrada = re.findall(i, str(soup))
        if F_encontrada:
            print("Fecha de la Noticia: " + F_encontrada[0]) 
            return
        else:
            F_encontrada = "Vacio"
    if F_encontrada == "Vacio":
        print("No se ha encontrado la Fecha de la Noticia")
        return

def main():
    if len(sys.argv) != 3:
        print("El formato para ejecutar el script desde una terminal es el siguiente:" )
        print("python Scraping.py <nombre_medio> <url_noticia>")
        sys.exit(1)

    N_Medio = sys.argv[1]
    URL_Noticia = sys.argv[2]

    #obtencion datos de HTML y comprobacion conexion
    reqs = requests.get(URL_Noticia)
    if reqs.status_code != 200:
        print("Error al conectarse a la pagina")
        sys.exit()
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    #imprimir datos proporcionados
    print("Nombre del medio:", N_Medio)
    print("URL de la noticia:", URL_Noticia)

    #imprimir Titulo de noticia
    Titulo(soup)
    #imprimir Fecha de noticia
    Fecha(soup)
main()

