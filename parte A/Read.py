import mariadb
import sys
from datetime import datetime

"""alta embellecer las respuestas con:
ciudad = ...
pais = ....
y comprobar todo, si todo funciona bien esta al 100 ya
"""

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
    query = " SELECT * FROM redessociales WHERE IDMedio = ? "
    params = (int(ID),)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    print("---------------------------")
    for Posicion in Seleccion:
        print(Posicion[0])
        print(Posicion[1])
        print(Posicion[2])
        print(Posicion[3])
        print(Posicion[4])
        print(Posicion[5])
        print("---------------------------")
    return

def CS(ID):
    query = " SELECT * FROM categorias WHERE IDMedio = ? "
    params = (int(ID),)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    print("---------------------------")
    for Posicion in Seleccion:
        print(Posicion[0])
        print(Posicion[1])
        print(Posicion[2])
        print(Posicion[3])
        print(Posicion[4])
        print(Posicion[5])
        print("---------------------------")
    return

def N_ejem(ID):
    query = " SELECT * FROM noticiaej WHERE IDMedio = ? "
    params = (int(ID),)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    print("---------------------------")
    for Posicion in Seleccion:
        print(Posicion[0])
        print(Posicion[1])
        print(Posicion[2])
        print(Posicion[3])
        print(Posicion[4])
        print(Posicion[5])
        print("---------------------------")
    return

def Fun(ID):
    query = " SELECT Nomfund FROM cuentacon WHERE IDMedio = ? "
    params = (int(ID),)
    cur.execute(query, params)
    Seleccion = cur.fetchall()
    print("---------------------------")
    for Posicion in Seleccion:
        print(Posicion[0])
        print("---------------------------") 
    return

def Ubi(ID):

    query = " SELECT IDCiud FROM mediosprensa WHERE IDMedio = ? "
    params1 = (int(ID),)
    cur.execute(query, params1)
    Seleccion = cur.fetchone()
    a = int(Seleccion[0])
    
    query2 = " SELECT * FROM ubicaciones WHERE IDciud = ? "
    params2 = (a,)
    cur.execute(query2, params2)
    Seleccion2 = cur.fetchall()

    print("---------------------------")
    for Posicion in Seleccion2:
        print(Posicion[0])
        print(Posicion[1])
        print(Posicion[2])
        print(Posicion[3])
        print(Posicion[4])
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
        print(f"Cobertura: {medio[2]}")
        print(f"Año de fundación: {medio[3]}")
        print(f"Sitio web: {medio[4]}")
        print(f"ID de ciudad: {medio[5]}")
        print("---------------------------")
    print("¿De cual medio de prensa quieres obtener informacion?")
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