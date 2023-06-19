import mysql.connector

conexion = mysql.connector.connect(
        host='.....',
        user='....',
        password='.....',
        database='Medios_Prensa'
    )
cursor = conexion.cursor()

medio = input("Ingrese el nombre del Medio de Prensa: ")
url_noticia = input("Ingrese la URL de la noticia: ")



# Obtener el nombre de la prensa según el nombre del medio
cursor.execute("SELECT NomPrensa FROM MediosPrensa WHERE NomPrensa = %s", (medio,))
resultado_medio = cursor.fetchone()

if resultado_medio:
    cursor.execute("SELECT TituloXP, FechaXP FROM Noticias WHERE NomPrensa = %s AND URL = %s", (medio, url_noticia))
    resultado_noticia = cursor.fetchone()
    if resultado_noticia:
        titulo_xp = resultado_noticia[0]
        fecha_xp = resultado_noticia[1]
    else:
        print("La noticia no existe en el Medio de Prensa.")
else:
    print("El Medio de prensa no existe.")

print("El Titulo es:", titulo_xp)
print("La fecha es:", fecha_xp)

cursor.close()
conexion.close()    