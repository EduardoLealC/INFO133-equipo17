"""
crawling.py: este script recibe el nombre de un medio 
y el nombre de una categoría y devuelve los enlaces de una de las páginas de esta categoría.
"""

import sys
import requests
from bs4 import BeautifulSoup
import mariadb

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="Sodimm1107#",
        host="localhost",
        database='Medios_Prensa'
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

def B_enlace_pagina(URL,URL2):
    reqs = requests.get(URL)
    #Comprobamos que la pagina funcione
    if reqs.status_code != 200:
        print("Error al conectarse a la pagina")
        sys.exit()
    soup = BeautifulSoup(reqs.content, 'html.parser')
    enlaces = soup.find_all('a')

    # Verificar si el enlace buscado está presente en la página
    encontrado = False
    for enlace in enlaces:
        href = enlace.get('href')
        if href == URL2:
            print("Enlace pertenece a la pagina")
            print(URL2)
            encontrado = True
    if encontrado == False:
        print("Enlace No pertenece a la pagina")

            




def menu():

    if len(sys.argv) != 3:
        print("El formato para ejecutar el script es el siguiente:" )
        print("Crawling.py <nombre_medio> <Nombre_Categoria>")
        sys.exit(1)

    N_Medio = sys.argv[1]
    N_Categoria = sys.argv[2]


    #Comprobar que el medio existe en la base de datos
    query = " SELECT Nomprensa FROM mediosprensa WHERE Nomprensa = ? "
    params = (N_Medio,)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    for i in Seleccion:
        if not i[0]:
            print("Medio de prensa NO existe en la base de datos")


    #Comprobar que la categoria existe en la base de datos y en el medio de prensa
    query = " SELECT * FROM categorias WHERE NomCat = ? "
    params = (N_Categoria,)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    for i in Seleccion:
        if not i[1]:
            print("Categoria NO existe en la base de datos o en el Medio de prensa")
        URL = i[2]
        URL2 = i[3]

    # print("El link de la noticia de ejemplo de esta categoria es: ")
    # print(URL2)
    B_enlace_pagina(URL,URL2)

    

menu()
conn.close()