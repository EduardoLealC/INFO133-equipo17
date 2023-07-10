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

#Funciones a usar


def NuevoMedio():
    #Contar la cantidad de medios de prensa
    query = "SELECT COUNT(*) FROM MediosPrensa"
    cur.execute(query)
    count = cur.fetchone()[0]

    #Contar la cantidad de Ciudades
    query2 = "SELECT COUNT(*) FROM ubicaciones"
    cur.execute(query2)
    count2 = cur.fetchone()[0]

    while True:
        try:
            #ATRIBUTOS DE MediosPrensa
            print("<Atributos del Medio>",end='\n')
            IDMedio = count + 1
            NomPrensa = input("Nombre del nuevo medio de prensa: ")
            Cobertura =  int(input("Cobertura del medio 'Nacional(1)Regional(2)Internacional(3)': "))
            while Cobertura not in [1,2,3]:
                print("Porfavor, reingrese correctamente ")
                Cobertura =  int(input("Cobertura del medio 'Nacional(1)Regional(2)Internacional(3)': "))
            AFund = int(input("Año de fundación de este medio: "))
            SWeb = input("Sitio web del medio: ")
            print(end='\n')

            #ATRIBUTOS DE Ubicaciones
            print("<Ubicación>",end='\n')
            IDCiud = count2 + 1
            NomCiud = input("Nombre de la Ciudad donde se ubica el medio: ")
            Region = input("Región donde se ubica el medio: ")
            Pais = "Honduras"
            Continente = "América Central"
            print(end='\n')

            break
        except ValueError:
            print("Error al ingresar el medio")

    insert_query = '''
    INSERT INTO Ubicaciones (IDCiud, NomCiud, Region, Pais, Continente)
    VALUES (%s, %s, %s, %s, %s)'''
    cur.execute(insert_query, (IDCiud, NomCiud, Region, Pais, Continente))
    conn.commit()

    insert_query = '''
    INSERT INTO MediosPrensa (IDMedio, NomPrensa, Cobertura, AFund, SWeb, IDCiud)
    VALUES (%s, %s, %s, %s, %s, %s)'''
    cur.execute(insert_query, (IDMedio, NomPrensa, Cobertura, AFund, SWeb, IDCiud))
    conn.commit()

    #Fundadores(IDMedio)  # <------------------- no se para que es

def Categoria(idmedio):
    query = "SELECT COUNT(*) FROM Categorias"
    cur.execute(query)
    count = cur.fetchone()[0]

    while True:
        try:
            #ATRIBUTOS DE Categorias
            print("<Categoria>",end='\n')
            IDCat = count + 1
            NomCat = input("Nombre de la categoría: ")
            PrinURL =  input("URL principal de la Categoría: ")
            EjemURL = input("URL de una noticia de ejemplo: ")
            Xpath = input("Expresión XPath para obtener los enlaces: ")
            IDMedio = idmedio
            print(end='\n')
            
            break
        except ValueError:
            print("Error al ingresar la categoría")

    insert_query = '''
    INSERT INTO Categorias (IDCat, NomCat, PrinURL, EjemURL, Xpath, IDMedio)
    VALUES (%s, %s, %s, %s, %s, %s)'''
    cur.execute(insert_query, (IDCat, NomCat, PrinURL, EjemURL, Xpath, IDMedio))
    conn.commit()
    
def RedesSociales(idmedio):
    query = "SELECT COUNT(*) FROM RedesSociales"
    cur.execute(query)
    count = cur.fetchone()[0]

    while True:
        try:
            #ATRIBUTOS DE RedesSociales
            print("<Red Social>",end='\n')
            IDRS = count + 1
            Plataforma = input("Nombre de la red social: ")
            NomUsuario = input("Nombre de 'usuario' del medio en esta red: ")
            NumSeg = int(input("Número de seguidores del medio en esta red: "))
            Fecha = input("Fecha de la última vez que se actualizaron los seguidores(DD-MM-YYYY): ")
            ActualizaS = datetime.strptime(Fecha,"%d-%m-%Y")
            IDMedio = idmedio
            print(end='\n')

            break
        except ValueError:
            print("Error al ingresar la red social")

    insert_query = '''
    INSERT INTO RedesSociales (IDRS, Plataforma, NomUsuario, NumSeg, ActualizaS, IDMedio)
    VALUES (%s, %s, %s, %s, %s, %s)'''
    cur.execute(insert_query, (IDRS, Plataforma, NomUsuario, NumSeg, ActualizaS, IDMedio))
    conn.commit()

def NoticiaEj(idmedio):
    query = "SELECT COUNT(*) FROM NoticiaEj"
    cur.execute(query)
    count = cur.fetchone()[0]

    while True:
        try:
            #ATRIBUTOS DE NoticiaEj
            print("<Noticia>",end='\n')
            IDNoticia = count + 1
            URL = input("URL de la noticia de ejemplo: ")
            FechaXP = input("Expresión XPATH que permita leer la Fecha de la noticia: ")
            TituloXP = input("Expresión XPATH que permita leer el Titulo de la noticia: ")
            ContXP = input("Expresión XPATH que permita leer el Contenido de la noticia: ")
            IDMedio = idmedio
            print(end='\n')

            break
        except ValueError:
            print("Error al ingresar la noticia")

    insert_query = '''
    INSERT INTO NoticiaEj (IDNoticia, URL, FechaXP, TituloXP, ContXP, IDMedio)
    VALUES (%s, %s, %s, %s, %s, %s)'''
    cur.execute(insert_query, (IDNoticia, URL, FechaXP, TituloXP, ContXP, IDMedio))
    conn.commit()

def Fundadores(idmedio):
    cantidad = int(input("Cuántos fundadores tiene este medio?: "))
    for i in range(1,cantidad+1):
        while True:
            try:
                #ATRIBUTOS DE Fundadores
                print("<Fundador ", i, ">",end='\n')
                NomFund = input("Nombre del fundador del medio: ")
                Fecha = input("Fecha de nacimiento(DD-MM-YYYY): ")
                FNac = datetime.strptime(Fecha,"%d-%m-%Y")
                print(end='\n')
            
                break
            except ValueError:
                print("Error al ingresar un fundador")

        insert_query = '''
        INSERT INTO Fundadores (NomFund, FNac)
        VALUES (%s, %s)'''
        cur.execute(insert_query, (NomFund, FNac))
        conn.commit()
        CuentaCon(idmedio,NomFund)

def CuentaCon(IDMedio,NomFund):
    insert_query = '''
    INSERT INTO CuentaCon (IDMedio, NomFund)
    VALUES (%s, %s)'''
    cur.execute(insert_query, (IDMedio, NomFund))
    conn.commit()

def MedioExistente():
    query1 = "SELECT * FROM MediosPrensa"
    cur.execute(query1)
    medios_prensa = cur.fetchall()

    query2 = "SELECT COUNT(*) FROM MediosPrensa"
    cur.execute(query2)
    count = cur.fetchone()[0]
    # Imprimir los medios de prensa
    print("Medios de Prensa existentes:")
    print("---------------------------")
    for medio in medios_prensa:
        print(f"ID: {medio[0]}")
        print(f"Nombre del medio: {medio[1]}")
        print("---------------------------")

    idmedio = int(input("Indique el ID del medio existente: "))
    while idmedio > count:
        print("El medio de prensa no existe, intentelo denuevo:")
    Eleccion2 = input(
                        """¿Qué desea agregar al Medio?:
            1- Categorias
            2- Fundadores
            3- Redes Sociales
            4- Noticia de ejemplo
            5- Salir
            """
            )
    if Eleccion2 == "1":
        Categoria(idmedio)
    elif Eleccion2 == "2":
        Fundadores(idmedio)
    elif Eleccion2 == "3":
        RedesSociales(idmedio)
    elif Eleccion2 == "4":
        NoticiaEj(idmedio)
    else:
        conn.close()
        return


def menu():
    while True:
        print("¿Qué desea hacer?:")
        print("1- Agregar Medio de Prensa")
        print("2- Agregar informacion a un medio de prensa")
        print("otro numero -  Salir ")
        Eleccion = input("Eleccion: ")
        
        if Eleccion == "1":
            NuevoMedio()
        elif Eleccion == "2":
            MedioExistente()
        else:
            conn.close()
            break
menu()

