import mysql.connector

def Funcion(nombre_medio, nombre_categoria):
    # Conexión a la base de datos
    conexion = mysql.connector.connect(
        host='....',
        user='....',
        password='....',
        database='Medios_Prensa'
    )

    # Crear cursor
    cursor = conexion.cursor()

    try:
        # Verifica
        cursor.execute("SELECT NomPrensa FROM MediosPrensa WHERE NomPrensa = %s", (nombre_medio,))
        resultado_medio = cursor.fetchone()

        if resultado_medio:
            # Verifica categoría 
            cursor.execute("SELECT PrinURL, EjemURL FROM Categorias WHERE NomPrensa = %s AND Nomcat = %s", (nombre_medio, nombre_categoria))
            resultado_categoria = cursor.fetchone()

            if resultado_categoria:
                prin_url = resultado_categoria[0]
                ejem_url = resultado_categoria[1]
                return prin_url, ejem_url
            else:
                print("La categoría especificada no existe para el medio.")
        else:
            print("El medio especificado no existe.")
    except mysql.connector.Error as error:
        print("Error al acceder a la base de datos:", error)
    finally:
        cursor.close()
        conexion.close()

# Ejemplo de uso
medio = input("Ingrese el nombre del medio: ")
categoria = input("Ingrese el nombre de la categoría: ")

enlaces = Funcion(medio, categoria)
if enlaces:
    prin_url, ejem_url = enlaces
    print("Enlaces encontrados:")
    print("Página principal:", prin_url)
    print("Ejemplo de página:", ejem_url)