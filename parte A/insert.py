import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
    host='....',
    user='....',
    password='....',
    database='Medios_Prensa'
)

def Opcion1():
    while True:
        try:
            Continente = input("Indica el Continente: ")
            Pais = input("Indica el Pais: ")
            Region = input("Indica la Region: ")
            Ciudad = input("Indica la Ciudad: ")
            Nombre = input("Indica el Nombre del nuevo medio de prensa: ")
            Cobertura =  int(input("Indica la Cobertura en numeros(1-Nacional,2-Regional,3-Internacional): "))
            AFund = int(input("Indica el Año de Fundacion: "))
            Sweb = input("Indica el sitio web del medio: ")
            break
        except ValueError:
            print("Ha ocurrido un error al ingresar los datos, reintentelo nuevamente")

    # Ubicacion 
    insert_ubicacion_query = '''
        INSERT INTO Ubicaciones (Continente,Pais, Region, Ciudad)
        VALUES (%s, %s, %s, %s)
    '''
    cursor.execute(insert_ubicacion_query, (Continente, Pais, Region, Ciudad ))
    conn.commit()

    # Medio de Prensa 
    insert_medio_query = '''
        INSERT INTO MediosPrensa (Ciudad, NomPrensa, Cobertura, AFund,  SWeb)
        VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_medio_query, (Ciudad, Nombre, Cobertura, AFund, Sweb))
    conn.commit()

def Opcion2():
    while True:
        try:
            Nombre = input("Indica el Nombre de la categoria: ")
            URL =  input("Indica el URL de la Categoria: ")
            EJemURL = input("Indica un URL que lleve a una noticia de ejemplo: ")
            XPath = input("Path para obtener los enlaces: ")
            NombrePrensa = input("Indica el nombre del medio de prensa que posee la categoria: ")
            break
        except ValueError:
            print("Ha ocurrido un error al ingresar los datos, reintentelo nuevamente")

    # Categoria
    insert_Categoria_query = '''
        INSERT INTO Categorias (Nomcat,PrinURL, EjemURL, Xpath, NomPrensa)
        VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_Categoria_query, (Nombre, URL, EJemURL, XPath, NombrePrensa ))
    conn.commit()
    
def Opcion3():
    while True:
        try:
            URL = input("Indica el URL de la Noticia: ")
            FechaXP =  input("Indica La Expresion Xpath para leer la fecha: ")
            TituloXP = input("Indica La Expresion Xpath para leer el titulo: ")
            ContXP = input("Indica La Expresion Xpath para leer el contenido: ")
            NombrePrensa = input("Indica el nombre del medio de prensa que posee la Noticia: ")
            break
        except ValueError:
            print("Ha ocurrido un error al ingresar los datos, reintentelo nuevamente")

    # Noticia
    insert_Noticia_query = '''
        INSERT INTO Noticias (URL,FechaXP, TituloXP, ContXP, NomPrensa)
        VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_Noticia_query, (URL, FechaXP, TituloXP, ContXP, NombrePrensa ))
    conn.commit()

def Opcion4():
    while True:
        try:
            IDRS = int(input("Indica un id para la RS: "))
            Plataforma =  input("Indica La plataforma: ")
            NomUsuario = input("Indica el Nombre del Medio de Prensa en la Red Social: ")
            Numseg = int(input("Indica el N°Seguidores: "))
            ActualizaS = input("Indica la ultima fecha de actualizacion de seguidores (DD/MM/YY): ")
            NombrePrensa = input("Indica el nombre del medio de prensa: ")
            break
        except ValueError:
            print("Ha ocurrido un error al ingresar los datos, reintentelo nuevamente")

    # RS
    insert_RedesSociales_query = '''
        INSERT INTO RedesSociales (IDRS,Plataforma, NomUsuario, Numseg, ActualizaS, NomPrensa)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_RedesSociales_query, (IDRS, Plataforma, NomUsuario, Numseg, ActualizaS, NombrePrensa ))
    conn.commit()
    
#Preguntar que desea:

while True:
    Eleccion = input(
        """Elija lo que quiere hacer: 
        1- Agregar Nuevo Medio de Prensa
        2- Agregar Nueva Categoria a Medio de Prensa Existente
        3- Agregar Noticia a Medio de Prensa Existente
        4- Agregar Redes Sociales a Medio de Prensa Existente
        5- Terminar Sesion
        """
    )
    cursor = conn.cursor()
    if Eleccion == "1":
        Opcion1()
    elif Eleccion == "2":
        Opcion2()
    elif Eleccion == "3":
        Opcion3()
    elif Eleccion == "4":
        Opcion4()
    elif Eleccion == "5":
        conn.close()
        break
        
  