"""
Para instalar "mariadb", ejecutar en la terminal lo siguiente:
    pip install mariadb

Para ejecutar este script de python debes crear el usuario: "parteA":
1)Iniciar el server de mariadb en una terminal:
    sudo /etc/init.d/mariadb start
2)Estando en la terminal (fuera de mariadb), conectarse como ADMIN:
    "sudo mariadb" o "mysql -u root" 
3)Para ver los usuarios:
    SELECT user, host FROM mysql.user;
4)Para crear un usuario:
    CREATE USER 'parteA'@'localhost' IDENTIFIED BY 'parteA'; (INCLUIR LAS COMILLAS SIMPLES)
5)Le otorgaremos todos los privilegios al usuario creado:
    GRANT ALL PRIVILEGES ON * . * TO 'parteA'@'localhost'; (INCLUIR LAS COMILLAS SIMPLES)
6)Guarda los cambios ejecutando el siguiente comando:
    FLUSH PRIVILEGES;
7)AHORA puede ejecutar este CÓDIGO python PERO desde una terminal, y con los parámetros requeridos
-----------------------------------------------------------------------------------------------------------"""
#crawling.py: este script recibe el nombre de un medio y el nombre de una categoría y devuelve los enlaces de una de las páginas de esta categoría.

import sys
import requests
from bs4 import BeautifulSoup
import mariadb

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="parteA",
        password="parteA",
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
        print("El formato para ejecutar el script desde una terminal es el siguiente:" )
        print("python Crawling.py <nombre_medio> <Nombre_Categoria>")
        sys.exit(1)

    N_Medio = sys.argv[1]
    N_Categoria = sys.argv[2]


    #Comprobar que el medio existe en la base de datos
    query = " SELECT NomPrensa FROM MediosPrensa WHERE NomPrensa = ? "
    params = (N_Medio,)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    for i in Seleccion:
        if not i[0]:
            print("Medio de prensa NO existe en la base de datos")


    #Comprobar que la categoria existe en la base de datos y en el medio de prensa
    query = " SELECT * FROM Categorias WHERE NomCat = ? "
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