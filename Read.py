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
7)AHORA puede ejecutar este CÓDIGO python
-----------------------------------------------------------------------------------------------------------"""
import mariadb
import sys
from datetime import datetime

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

#Funciones a Usar

def EsDigito(Numero1,Numero2,frase):
    Comprueba = False
    while Comprueba == False:
        if Numero1.isdigit() == True:
            if int(Numero1) > Numero2:
                Numero1 = input("Error! digite " + frase + " existente: ")
            else:
                Comprueba = True
                return Numero1
        else:
            Numero1 = input("Error! digite "+frase +" numerico: ")

def RS(ID):
    query = " SELECT * FROM RedesSociales WHERE IDMedio = ? "
    params = (int(ID),)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    print("---------------------------")
    for Posicion in Seleccion:
        print("ID de la red social:", Posicion[0])
        print("Plataforma: " + Posicion[1])
        print("Nombre de Usuario: " + Posicion[2])
        print("N°Seguidores:", Posicion[3])
        print("Ultima Actualizacion:", Posicion[4])
        print("IDMedio:", Posicion[5])
        print("---------------------------")
    return

def CS(ID):
    query = " SELECT * FROM Categorias WHERE IDMedio = ? "
    params = (int(ID),)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    print("---------------------------")
    for Posicion in Seleccion:
        print("ID de la categoría:", Posicion[0])
        print("Nombre Categoria: " + Posicion[1])
        print("URL Principal: " + Posicion[2])
        print("Ejemplo de Noticia: " + Posicion[3])
        print("XPath: " + Posicion[4])
        print("IDmedio:", Posicion[5])
        print("---------------------------")
    return

def N_ejem(ID):
    query = " SELECT * FROM NoticiaEj WHERE IDMedio = ? "
    params = (int(ID),)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    print("---------------------------")
    for Posicion in Seleccion:
        print("ID de la noticia de ejemplo:", Posicion[0])
        print("URL: " + Posicion[1])
        print("Xpath Fecha: " + Posicion[2])
        print("Xpath Titulo: " + Posicion[3])
        print("Xpath Contenido: " + Posicion[4])
        print("IDMedio:", Posicion[5])
        print("---------------------------")
    return

def Fun(ID):
    query = " SELECT Nomfund FROM CuentaCon WHERE IDMedio = ? "
    params = (int(ID),)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    print("---------------------------")
    for Posicion in Seleccion:
        print(Posicion[0])
        print("---------------------------") 
    return

def Ubi(ID):

    query = " SELECT IDCiud FROM MediosPrensa WHERE IDMedio = ? "
    params1 = (int(ID),)
    cur.execute(query, params1)
    Seleccion = cur.fetchone()
    a = int(Seleccion[0])
    
    query2 = " SELECT * FROM Ubicaciones WHERE IDciud = ? "
    params2 = (a,)
    cur.execute(query2, params2)
    Seleccion2 = cur.fetchall()

    print("---------------------------")
    for Posicion in Seleccion2:
        print("ID de la Ubicación:", Posicion[0])
        print("Nombre Ciudad: " + Posicion[1])
        print("Region: " + Posicion[2])
        print("Pais: " + Posicion[3])
        print("Continente: " + Posicion[4])
        print("---------------------------")
    return
    

def menu():
    query = "SELECT * FROM MediosPrensa"
    cur.execute(query)
    medios_prensa = cur.fetchall()

    query2 = "SELECT COUNT(*) FROM MediosPrensa"
    cur.execute(query2)
    count = cur.fetchone()[0]


    print("---------------------------")
    for medio in medios_prensa:
        print(f"ID: {medio[0]}")
        print(f"Nombre de prensa: {medio[1]}")
        if medio[2] == 1:
            print(f"Cobertura: Local")
        elif medio[2] == 2:
            print(f"Cobertura: Nacional")
        elif medio[2] == 3:
            print(f"Cobertura: Internacional")
        print(f"Año de fundación: {medio[3]}")
        print(f"Sitio web: {medio[4]}")
        print(f"ID de ciudad: {medio[5]}")
        print("---------------------------")
    print("¿De cuál medio de prensa quieres obtener información?")
    Id = input("Digite el ID: ")
    Id = EsDigito(Id,count,"un ID")
    seguir = True
    while seguir:
        print(
                """¿Que desea ver de este medio de prensa?:
                1- Categorias
                2- Fundadores
                3- Redes Sociales
                4- Noticia de ejemplo
                5- Ubicacion
                6- Salir
                """
                )
        Eleccion = input("Digite su eleccion: ")
        EsDigito(Eleccion,6,"una Opcion")
    
        if int(Eleccion) == 1: CS(Id)
        elif int(Eleccion) == 2: Fun(Id)
        elif int(Eleccion) == 3: RS(Id)
        elif int(Eleccion) == 4: N_ejem(Id)
        elif int(Eleccion) == 5: Ubi(Id)
        elif int(Eleccion) == 6: seguir = False
        

menu()