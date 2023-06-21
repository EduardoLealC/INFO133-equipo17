#Instalar "mariadb" ejecutando en la terminal lo siguiente:
#pip install mariadb
"""
Para ejecutar este script de python: CREAREMOS EL USUARIO 'parteA':
1)Estando en la terminal, fuera de mariadb, conectarse como ADMIN: "sudo mariadb" o "mysql -u root" 
2)Para ver los usuarios: SELECT user, host FROM mysql.user;
3)Para crear un usuario: CREATE USER 'parteA'@'localhost' IDENTIFIED BY 'parteA';
4)Otorgaremos todos los privilegios: GRANT ALL PRIVILEGES ON * . * TO 'parteA'@'localhost';
5)Guarda los cambios ejecutando el siguiente comando: FLUSH PRIVILEGES;
-----------------------------------------------------------------------------------------------------------"""
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="parteA",
        password="parteA",
        host="localhost",
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# Crea la base de datos si esque NO existe:
cur.execute("CREATE DATABASE IF NOT EXISTS Medios_Prensa")

# Entramos a la base de datos:
cur.execute("USE Medios_Prensa")

# Creamos las tablas si esque NO existen: 
cur.execute("""CREATE TABLE IF NOT EXISTS Ubicaciones (
    IDCiud INT PRIMARY KEY,
    NomCiud VARCHAR(60),
    Region VARCHAR(60),
    Pais VARCHAR(60),
    Continente VARCHAR(30)
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS MediosPrensa (
    IDMedio INT AUTO_INCREMENT PRIMARY KEY,
    NomPrensa VARCHAR(80),
    Cobertura INT1,
    AFund YEAR,
    SWeb VARCHAR(500),

    IDCiud INT,
    FOREIGN KEY (IDCiud) REFERENCES Ubicaciones(IDCiud)
)""")
  
cur.execute("""CREATE TABLE IF NOT EXISTS Categorias (
    IDCat INT KEY,
    Nomcat VARCHAR(30),
    PrinURL VARCHAR(500),
    EjemURL VARCHAR(500),
    Xpath VARCHAR(100),

    IDMedio INT AUTO_INCREMENT,
    FOREIGN KEY (IDMedio) REFERENCES MediosPrensa(IDMedio)
)""")
    
cur.execute("""CREATE TABLE IF NOT EXISTS Fundadores (
    NomFund VARCHAR(50) PRIMARY KEY,
    FNac DATE
)""")
    
cur.execute("""CREATE TABLE IF NOT EXISTS RedesSociales (
    IDRS INT PRIMARY KEY,
    Plataforma VARCHAR(30),
    NomUsuario VARCHAR(60),
    NumSeg INT,
    ActualizaS DATE,

    IDMedio INT AUTO_INCREMENT,
    FOREIGN KEY (IDMedio) REFERENCES MediosPrensa(IDMedio)
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS Noticias (
    IDNoticia INT PRIMARY KEY,
    URL VARCHAR(500),
    FechaXP VARCHAR(100),
    TituloXP VARCHAR(100),
    ContXP VARCHAR(100),

    IDMedio INT AUTO_INCREMENT,
    FOREIGN KEY (IDMedio) REFERENCES MediosPrensa(IDMedio)
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS CuentaCon (
    IDMedio INT AUTO_INCREMENT,
    NomFund VARCHAR(50),
    PRIMARY KEY (IDMedio, NomFund),
    FOREIGN KEY (IDMedio) REFERENCES MediosPrensa(IDMedio),
    FOREIGN KEY (NomFund) REFERENCES Fundadores(NomFund)
)""")
            
#cur.execute("INSERT INTO news (url, title) VALUES (?,?)", ("a","b"))

conn.commit() 
conn.close()