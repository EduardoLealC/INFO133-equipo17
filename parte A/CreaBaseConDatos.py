"""
Instalar "mariadb" ejecutando en la terminal lo siguiente:
    pip install mariadb

Para ejecutar este script de python: CREAREMOS EL USUARIO 'parteA':
1)Estando en la terminal, fuera de mariadb, conectarse como ADMIN:
    "sudo mariadb" o "mysql -u root" 
2)Para ver los usuarios:
    SELECT user, host FROM mysql.user;
3)Para crear un usuario:
    CREATE USER 'parteA'@'localhost' IDENTIFIED BY 'parteA'; (INCLUIR LAS COMILLAS SIMPLES)
4)Otorgaremos todos los privilegios:
    GRANT ALL PRIVILEGES ON * . * TO 'parteA'@'localhost'; (INCLUIR LAS COMILLAS SIMPLES)
5)Guarda los cambios ejecutando el siguiente comando:
    FLUSH PRIVILEGES;
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
    IDMedio INT PRIMARY KEY,
    NomPrensa VARCHAR(80),
    Cobertura INT1,
    AFund SMALLINT,
    SWeb VARCHAR(500),

    IDCiud INT,
    FOREIGN KEY (IDCiud) REFERENCES Ubicaciones(IDCiud)
)""")
  
cur.execute("""CREATE TABLE IF NOT EXISTS Categorias (
    IDCat INT PRIMARY KEY,
    NomCat VARCHAR(40),
    PrinURL VARCHAR(500),
    EjemURL VARCHAR(500),
    Xpath VARCHAR(100),

    IDMedio INT,
    FOREIGN KEY (IDMedio) REFERENCES MediosPrensa(IDMedio)
)""")
    
cur.execute("""CREATE TABLE IF NOT EXISTS Fundadores (
    NomFund VARCHAR(100) PRIMARY KEY,
    FNac DATE
)""")
    
cur.execute("""CREATE TABLE IF NOT EXISTS RedesSociales (
    IDRS INT PRIMARY KEY,
    Plataforma VARCHAR(30),
    NomUsuario VARCHAR(60),
    NumSeg INT,
    ActualizaS DATE,

    IDMedio INT,
    FOREIGN KEY (IDMedio) REFERENCES MediosPrensa(IDMedio)
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS NoticiaEj (
    IDNoticia INT PRIMARY KEY,
    URL VARCHAR(500),
    FechaXP VARCHAR(100),
    TituloXP VARCHAR(100),
    ContXP VARCHAR(100),

    IDMedio INT,
    FOREIGN KEY (IDMedio) REFERENCES MediosPrensa(IDMedio)
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS CuentaCon (
    IDMedio INT,
    NomFund VARCHAR(50),
    PRIMARY KEY (IDMedio, NomFund),
    FOREIGN KEY (IDMedio) REFERENCES MediosPrensa(IDMedio),
    FOREIGN KEY (NomFund) REFERENCES Fundadores(NomFund)
)""")

#INSERTA LOS DATOS A LA BASE ------------------------------------------------------------------------------------

#(Honduras se divide en departamentos, no en regiones)
cur.execute("""INSERT INTO Ubicaciones (IDCiud, NomCiud, Region, Pais, Continente) VALUES
(1, 'Tegucigalpa', 'Francisco Morazán', 'Honduras', 'América Central'),
(2, 'San Pedro Sula', 'Cortés', 'Honduras', 'América Central'),
(3, 'El Progreso', 'Yoro', 'Honduras', 'América Central'),
(4, 'La Ceiba', 'Atlántida', 'Honduras', 'América Central'),
(5, 'Desconocida', 'Desconocida', 'Honduras', 'América Central')
""")
conn.commit()

cur.execute("""INSERT INTO MediosPrensa (IDMedio, NomPrensa, Cobertura, AFund, SWeb, IDCiud) VALUES
(1, 'Diario La Prensa', 2, 1964, 'https://www.laprensa.hn/', 2),
(2, 'Diario El Heraldo', 1, 1979, 'https://www.elheraldo.hn/', 1),
(3, 'Diario Tiempo', 1, 1970, 'https://tiempo.hn/', 2),
(4, 'Diario El País', 1, 2017, 'https://www.elpais.hn/', 2),
(5, 'Diario El Mundo', 2, 2018, 'https://elmundo.hn/', 1),
(6, 'Proceso Digital', 1, 2005, 'https://proceso.hn/', 1),
(7, 'Diario La Tribuna', 1, 2005, 'https://www.latribuna.hn/', 1),
(8, 'El Libertador', 2, 2003, 'https://ellibertador.hn/', 1),
(9, 'El Pulso', 2, 0000, 'https://elpulso.hn/', 5),
(10, 'La Noticia', 2, 0000, 'https://lanoticia.hn/', 5),
(11, 'Diario Deportivo Diez', 2, 2006, 'https://www.diez.hn/', 2),
(12, 'Diario El Articulista', 1, 2013, 'https://www.elarticulista.net/', 1),
(13, 'Diario Contexto', 2, 0000, 'https://contextohn.com/', 5),
(14, 'Diario EL ONCE HN', 1, 2008, 'https://eloncehn.com/', 2),
(15, 'Diario Deportivo GOLAZO', 2, 0000, 'https://diariogolazo.hn/', 1),
(16, 'ENTER504', 2, 2020, 'https://enter504.com/', 2),
(17, 'Radio HRN', 1, 1933, 'https://www.radiohrn.hn/', 1),
(18, 'Radio Globo', 1, 1999, 'https://www.radioglobohonduras.com/', 1),
(19, 'RDS Radio', 1, 0000, 'https://rdsradio.hn/', 1),
(20, 'Radio America', 2, 1948, 'https://www.radioamerica.hn/', 1),
(21, 'Radio Progreso', 1, 1980, 'https://www.radioprogresohn.net/', 3),
(22, 'Radio Cadena Voces', 1, 2006, 'https://www.rcv.hn/', 1),
(23, 'Televicentro', 2, 1987, 'https://www.televicentro.com/', 1),
(24, 'HCH', 1, 2010, 'https://hch.tv/', 1),
(25, 'Canal 6', 1, 1982, 'https://canal6.com.hn/', 2),
(26, 'Globo TV', 1, 2010, 'https://www.globotvhonduras.com/', 1),
(27, 'Canal 11', 2, 1996, 'https://canal11.hn/', 2),
(28, 'MAYA TV', 1, 2004, 'https://mayatv.hn/', 1)
""")
conn.commit()

cur.execute("""INSERT INTO Fundadores (NomFund, FNac) VALUES
('Jorge Canahuati', '1956-04-21'),
('Jaime Rosenthal', '1936-05-05'),
('Oscar Flores', '1912-07-04'),
('Jhonny Lagos', NULL),
('José Mejía', '1978-03-22'),
('Kenet Orellana', NULL),
('Eddy Sarmiento', NULL),
('Rafael Ferrari', '1934-02-10'),
('Alejandro Villatoro', NULL),
('Sergio Castellón', NULL),
('Ismael Moreno', '1960-01-22'),
('Fernando Lardizábal', NULL),
('Manuel Villeda', '1968-07-30'),
('Eduardo Maldonado', '1960-12-06'),
('Joaquin Nodarse', NULL),
('Mario Flores', NULL),
('Desconocido', NULL)
""")
conn.commit()

cur.execute("""INSERT INTO CuentaCon (IDMedio,NomFund) VALUES
(1, 'Jorge Canahuati'),
(2, 'Jorge Canahuati'),
(3, 'Jaime Rosenthal'),
(4, 'Desconocido'),
(5, 'Desconocido'),
(6, 'Desconocido'),
(7, 'Oscar Flores'),
(8, 'Jhonny Lagos'),
(9, 'Desconocido'),
(10, 'Desconocido'),
(11, 'Jorge Canahuati'),
(12, 'José Mejía'),
(13, 'Desconocido'),
(14, 'Desconocido'),
(15, 'Kenet Orellana'),
(16, 'Eddy Sarmiento'),
(17, 'Rafael Ferrari'),
(18, 'Alejandro Villatoro'),
(19, 'Desconocido'),
(20, 'Sergio Castellón'),
(21, 'Ismael Moreno'),
(22, 'Desconocido'),
(23, 'Rafael Ferrari'),
(24, 'Eduardo Maldonado'),
(25, 'Joaquin Nodarse'),
(26, 'Alejandro Villatoro'),
(27, 'Jaime Rosenthal'),
(28, 'Mario Flores')
""")
conn.commit()
            
cur.execute("""INSERT INTO RedesSociales (IDRS, Plataforma, NomUsuario, NumSeg, ActualizaS, IDMedio) VALUES
(1, 'Instagram', 'diariolaprensa', 300000, '2023-07-07', 1),
(2, 'Facebook', 'Diario La Prensa', 2300000, '2023-07-07', 1),
(3, 'Twitter', 'DiarioLaPrensa', 551800, '2023-07-07', 1),
(4, 'Youtube', 'diariolaprensahn', 58100, '2023-07-07', 1),
(5, 'Instagram', 'diarioelheraldo', 198000, '2023-07-07', 2),
(6, 'Facebook', 'DIARIO EL HERALDO', 1600000, '2023-07-07', 2),
(7, 'Twitter', 'diarioelheraldo', 441900, '2023-07-07', 2),
(8, 'Youtube', 'DiarioElHeraldoHonduras', 33100, '2023-07-07', 2),
(9, 'Instagram', 'diariotiempo', 19900, '2023-07-07', 3),
(10, 'Facebook', 'Diario Tiempo', 504000, '2023-07-07', 3),
(11, 'Twitter', 'DiarioTiempo', 309400, '2023-07-07', 3),
(12, 'Instagram', 'elpaishn', 3763, '2023-07-07', 4),
(13, 'Facebook', 'Honduras El País', 47000, '2023-07-07', 4),
(14, 'Twitter', 'elpaishn', 53900, '2023-07-07', 4),
(15, 'Instagram', 'elmundohn', 249, '2023-07-07', 5),
(16, 'Twitter', 'elmundohn', 1979, '2023-07-07', 5),
(17, 'Youtube', 'diarioelmundohn7885', 57, '2023-07-07', 5),
(18, 'Instagram', 'procesohn', 1866, '2023-07-07', 6),
(19, 'Facebook', 'Proceso Hn', 29000, '2023-07-07', 6),
(20, 'Twitter', 'ProcesoDigital', 50800, '2023-07-07', 6),
(21, 'Youtube', 'videosproceso', 5990, '2023-07-07', 6),
(22, 'Instagram', 'latribuna', 438000, '2023-07-07', 7),
(23, 'Facebook', 'La Tribuna', 55000, '2023-07-07', 7),
(24, 'Twitter', 'LaTribunahn', 312700, '2023-07-07', 7),
(25, 'Youtube', 'latribunatvhn', 66400, '2023-07-07', 7),
(26, 'Instagram', 'ellibertadorhn', 2165, '2023-07-07', 8),
(27, 'Facebook', 'Periodico EL LIBERTADOR', 52000, '2023-07-07', 8),
(28, 'Twitter', 'hnellibertador', 30300, '2023-07-07', 8),
(29, 'Youtube', 'ellibertadoroficialhn', 912, '2023-07-07', 8),
(30, 'Instagram', 'elpulsohn', 2964, '2023-07-07', 9),
(31, 'Facebook', 'El Pulso', 80000, '2023-07-07', 9),
(32, 'Twitter', 'elpulsohn', 20900, '2023-07-07', 9),
(33, 'Youtube', 'ElPulsoHN', 4790, '2023-07-07', 9),
(34, 'Instagram', 'lanoticiahn', 146, '2023-07-07', 10),
(35, 'Facebook', 'Lanoticia.hn', 115000, '2023-07-07', 10),
(36, 'Twitter', 'lanoticiahn', 1351, '2023-07-07', 10),
(37, 'Instagram', 'diariodiez', 264000, '2023-07-07', 11),
(38, 'Facebook', 'Diario Deportivo Diez', 1500000, '2023-07-07', 11),
(39, 'Twitter', 'DiarioDiezHn', 93200, '2023-07-07', 11),
(40, 'Youtube', 'DiarioDiez', 111000, '2023-07-07', 11),
(41, 'Facebook', 'Diario El Articulista', 3300, '2023-07-07', 12),
(42, 'Twitter', 'EL_ARTICULISTA', 2549, '2023-07-07', 12),
(43, 'Youtube', 'ESCRITORJOSE', 9970, '2023-07-07', 12),
(44, 'Instagram', 'contextohn', 1105, '2023-07-07', 13),
(45, 'Facebook', 'Contexto', 392, '2023-07-07', 13),
(46, 'Twitter', 'contextohn', 454, '2023-07-07', 13),
(47, 'Youtube', 'contextohonduras4869', 232, '2023-07-07', 13),
(48, 'Instagram', 'ddeloncehn', 1586, '2023-07-07', 14),
(49, 'Facebook', 'Diario Deportivo El ONCE HN', 182000, '2023-07-07', 14),
(50, 'Twitter', 'eloncehn1', 384, '2023-07-07', 14),
(51, 'Youtube', 'eloncehn', 322, '2023-07-07', 14),
(52, 'Instagram', 'diariogolazohn', 296, '2023-07-07', 15),
(53, 'Facebook', 'Diario Deportivo GOLAZO', 8300, '2023-07-07', 15),
(54, 'Twitter', 'DiarioGOLAZO', 1977, '2023-07-07', 15),
(55, 'Youtube', 'DiarioGOLAZO', 4320, '2023-07-07', 15),
(56, 'Instagram', 'enter504', 6623, '2023-07-07', 16),
(57, 'Facebook', 'Enter504 Periodico Digital', 16000, '2023-07-07', 16),
(58, 'Twitter', 'enter504', 701, '2023-07-07', 16),
(59, 'Youtube', 'enter504', 253, '2023-07-07', 16),
(60, 'Instagram', 'radiohrn', 35300, '2023-07-07', 17),
(61, 'Facebook', 'RadioHRN', 349000, '2023-07-07', 17),
(62, 'Twitter', 'radiohrn', 272800, '2023-07-07', 17),
(63, 'Youtube', 'HRNemisorasunidas', 8390, '2023-07-07', 17),
(64, 'Instagram', 'globohonduras', 513, '2023-07-07', 18),
(65, 'Facebook', 'Radio Globo Honduras', 146000, '2023-07-07', 18),
(66, 'Twitter', 'GloboHonduras', 5228, '2023-07-07', 18),
(67, 'Instagram', 'rdsradiohn', 3785, '2023-07-07', 19),
(68, 'Facebook', 'RDS Radio 88.9 FM', 153000, '2023-07-07', 19),
(69, 'Twitter', 'RDSRadioHn', 381, '2023-07-07', 19),
(70, 'Instagram', 'radioamericahn', 53700, '2023-07-07', 20),
(71, 'Facebook', 'Radio América', 668000, '2023-07-07', 20),
(72, 'Twitter', 'radioamericahn', 155400, '2023-07-07', 20),
(73, 'Youtube', 'Radioamericahn', 29900, '2023-07-07', 20),
(74, 'Instagram', 'radioprogresohn', 2565, '2023-07-07', 21),
(75, 'Facebook', 'Radio Progreso | Pagina Oficial', 268200, '2023-07-07', 21),
(76, 'Twitter', 'RadioProgresoHN', 21500, '2023-07-07', 21),
(77, 'Instagram', 'rcvhonduras', 19200, '2023-07-07', 22),
(78, 'Facebook', 'Radio Cadena Voces', 174000, '2023-07-07', 22),
(79, 'Twitter', 'RCVHonduras', 34500, '2023-07-07', 22),
(80, 'Instagram', 'televicentro_hn', 332000, '2023-07-07', 23),
(81, 'Facebook', 'Televicentro HN', 735000, '2023-07-07', 23),
(82, 'Twitter', 'televicentrohn', NULL, '2023-07-07', 23),
(83, 'Youtube', 'televicentroHN', NULL, '2023-07-07', 23),
(84, 'Instagram', 'hchtv', 481000, '2023-07-07', 24),
(85, 'Facebook', 'HCH Television Digital', 2900000, '2023-07-07', 24),
(86, 'Twitter', 'HCHTelevDigital', 470900, '2023-07-07', 24),
(87, 'Youtube', 'HCHTelevisionDigital', 1110000, '2023-07-07', 24),
(88, 'Instagram', 'canal6honduras', 60600, '2023-07-07', 25),
(89, 'Facebook', 'Canal 6 Honduras', 1100000, '2023-07-07', 25),
(90, 'Twitter', 'Canal6Honduras', 76700, '2023-07-07', 25),
(91, 'Youtube', 'CanalSeisHonduras', 3470, '2023-07-07', 25),
(92, 'Facebook', 'Globo TV Honduras', 326000, '2023-07-07', 26),
(93, 'Twitter', 'Globotvhonduras', 39, '2023-07-07', 26),
(94, 'Youtube', 'globotvhonduras325', 6260, '2023-07-07', 26),
(95, 'Instagram', 'canal11hn', 133000, '2023-07-07', 27),
(96, 'Facebook', 'Canal 11', 492000, '2023-07-07', 27),
(97, 'Twitter', 'canal11hn', 203600, '2023-07-07', 27),
(98, 'Youtube', 'canal11honduras', 79600, '2023-07-07', 27),
(99, 'Instagram', 'mayatv.hn', 7853, '2023-07-07', 28),
(100, 'Facebook', 'MAYA TV', 5300, '2023-07-07', 28),
(101, 'Twitter', 'mayatvnoticias', 11, '2023-07-07', 28),
(102, 'Youtube', 'mayatvhonduras1774', 651, '2023-07-07', 28)
""")
conn.commit()

cur.execute("""INSERT INTO Categorias (IDCat, NomCat, PrinURL, EjemURL, Xpath, IDMedio) VALUES
(1, 'Sucesos', 'https://www.laprensa.hn/sucesos', 'https://www.laprensa.hn/sucesos/honduras-desarman-linchan-presunto-asaltante-arenal-yoro-HO14293554', '/html/head/link[@rel="canonical"]/@href' ,1),
(2, 'Internacional', 'https://www.laprensa.hn/mundo', 'https://www.laprensa.hn/mundo/como-funciona-threads-aplicacion-meta-compite-twitter-FA14277417', '/html/head/link[@rel="canonical"]/@href' ,1),
(3, 'Deporte','https://www.laprensa.hn/deportes', 'https://www.laprensa.hn/deportes/mercado-cristian-sacaza-deja-el-vida-y-es-nuevo-fichaje-del-marathon-torneo-apertura-2023-honduras-AG14308239', '/html/head/link[@rel="canonical"]/@href', 1),
(4, 'Entretenimiento', 'https://www.laprensa.hn/espectaculos', 'https://www.laprensa.hn/espectaculos/farandula-actriz-mexicana-salma-hayek-impacta-bikinazo-56-anos-FG14305918', '/html/head/link[@rel="canonical"]/@href', 1),
(5, 'Sucesos', 'https://www.elheraldo.hn/sucesos', 'https://www.elheraldo.hn/sucesos/detenidos-dos-menores-miembros-pandilla-18-armas-droga-colonia-hato-de-enmedio-tegucigalpa-GG14308428', '/html/head/link[@rel="canonical"]/@href', 2),
(6, 'Deporte', 'https://www.elheraldo.hn/deportes', 'https://www.elheraldo.hn/deportes/copa-oro/luis-suarez-explica-la-posibilidad-de-dirigir-a-la-seleccion-de-honduras-CG14307647', '/html/head/link[@rel="canonical"]/@href', 2),
(7, 'Internacional', 'https://www.elheraldo.hn/mundo', 'https://www.elheraldo.hn/mundo/autoridades-guatemala-piden-respetar-resultados-elecciones-impugnadas-JG14308346', '/html/head/link[@rel="canonical"]/@href', 2),
(8, 'Entretenimiento', 'https://www.elheraldo.hn/entretenimiento', 'https://www.elheraldo.hn/fotogalerias/entretenimiento/celebridades-famosas-sufrieron-violencia-domestica-como-lo-superaron-GG14307919', '/html/head/link[@rel="canonical"]/@href', 2),
(9, 'Sucesos', 'https://www.elpais.hn/', 'https://www.elpais.hn/aparatoso-accidente-de-transito-deja-un-herido-en-bulevar-de-tegucigalpa/', '//a[div[@class="tdb-menu-item-text"] = "Sucesos"]/@href', 4),
(10, 'Deporte', 'https://www.elpais.hn/', 'https://www.elpais.hn/diego-vazquez-deja-de-ser-tecnico-de-honduras-tras-eliminacion-en-la-copa-oro/', '//a[div[@class="tdb-menu-item-text"] = "Deportes"]/@href', 4),
(11, 'Internacional','https://www.elpais.hn/', 'https://www.elpais.hn/condenado-a-90-cadenas-perpetuas-al-autor-de-matanza-en-walmart-de-2019/', '//a[div[@class="tdb-menu-item-text"] = "Internacionales"]/@href', 4),
(12, 'Sucesos', 'https://elmundo.hn/', 'https://elmundo.hn/tragico-hallazgo-de-una-menor-de-13-anos-sin-vida-en-una-quebrada-en-honduras/', '//*[@id="menu-main-navigation-2"]/li[5]/a/@href' , 5),
(13, 'Deporte', 'https://elmundo.hn/', 'https://elmundo.hn/las-11-estrellas-del-futbol-que-tambien-triunfan-en-el-mundo-de-la-moda/', '//*[@id="menu-main-navigation-2"]/li[7]/a/@href', 5),
(14, 'Entretenimiento', 'https://elmundo.hn/', 'https://elmundo.hn/daniel-radcliffe-aseguro-que-no-esta-interesado-en-ser-parte-de-la-nueva-serie-de-harry-potter/', '//*[@id="menu-main-navigation-2"]/li[9]/a/@href', 5),
(15, 'Internacional', 'https://proceso.hn/', 'https://proceso.hn/eeuu-da-por-finalizada-la-destruccion-de-sus-reservas-de-armas-quimicas/', '//a[contains(@href, ''/category/secciones/internacionales/'')]/@href',6),
(16, 'Deporte', 'https://proceso.hn/', 'https://proceso.hn/messi-sera-presentado-con-el-inter-miami-el-16-de-julio/', '//*[@id="menu-td-demo-header-menu-3"]/li[8]/a/@href', 6),
(17, 'Internacional', 'https://elpulso.hn/', 'https://elpulso.hn/2023/07/07/el-presidente-xi-jinping-insta-al-ejercito-chino-a-reforzar-los-planes-de-guerra/', '//*[@id="menu-item-53076"]/a/@href', 9),
(18, 'Internacional', 'https://lanoticia.hn/', 'https://lanoticia.hn/nicaragua-cancela-nombramiento-de-embajador-nicaraguense-en-honduras/', '//*[@id="menu-item-101344"]/a/@href', 10),
(19, 'Deporte', 'https://lanoticia.hn/category/', 'https://lanoticia.hn/astros-vence-a-rockies-dubon-con-dos-hits-e-impulsada/', '//*[@id="menu-item-101344"]/a/@href', 10),
(20, 'Deporte', 'https://www.diez.hn/', 'https://www.diez.hn/internacionales/ronaldo-nazario-vini-real-madrid-no-sabia-controlar-con-la-zurda-solo-ahora-es-el-jugador-mas-decisivo-y-determinante-del-mundo-NG14306685', '//*[@id="menu_2911572534"]/div/ul/li[2]/div/a/@href', 11), 
(21, 'Internacional', 'https://www.elarticulista.net/search/label/Internacionales?&max-results=6', 'https://www.elarticulista.net/2022/08/murio-los-91-anos-mijail-gorbachov-el.html', '/html/head/link[@rel=''canonical'']/@href', 12),
(22, 'Deporte', 'https://www.elarticulista.net/search/label/Deportes?&max-results=6', 'https://www.elarticulista.net/2022/08/jugadores-de-la-nfl-eligen-tom-brady.html', '/html/head/link[@rel=''canonical'']/@href', 12),
(23, 'Sucesos', 'https://www.elarticulista.net/search/label/Sucesos?&max-results=6', 'https://www.elarticulista.net/2022/08/celulares-y-videos-vinculan-gringo-con.html', '/html/head/link[@rel=''canonical'']/@href', 12),
(24, 'Internacional', 'https://contextohn.com/', 'https://contextohn.com/internacionales/biden-teme-que-taiwan-siga-a-ucrania-y-acelera-sus-planes-para-contener-a-china/', '//*[@id="menu-item-46"]/a/@href', 13),
(25, 'Nacional', 'https://contextohn.com/', 'https://contextohn.com/nacional/inversion-de-palmerola-international-airport-es-de-mas-de-135-millones-en-el-aeropuerto/', '//*[@id="menu-item-577"]/a', 13),
(26, 'Entretencion', 'https://contextohn.com/', 'https://contextohn.com/farandula/no-da-tregua-contenciosa-batalla-legal-entre-kevin-costner-y-su-ex/', '//*[@id="menu-item-47"]/a/@href', 13),
(27, 'Deporte', 'https://eloncehn.com/', 'https://eloncehn.com/index.php/2023/07/07/olimpia-habria-tomado-determinacion-con-jack-jean-baptiste/', '//*[@id="menu-item-9"]/a/@href', 14 ),
(28, 'Deporte', 'https://eloncehn.com/', 'https://eloncehn.com/index.php/2022/12/30/posicion-2-real-madrid-en-lo-mas-alto-de-toda-europa/', '//*[@id="menu-item-7"]/a/@href', 14),
(29, 'Deporte', 'https://diariogolazo.hn/', 'https://diariogolazo.hn/otros-deportes/de-seve-a-jon-la-gloria-del-heredero-y-la-historia-de-amor-entre-espana-y-augusta/28/', '//*[@id="menu-item-7"]/a/@href', 15),
(30, 'Internacional', 'https://enter504.com/', 'https://enter504.com/ee-uu-abre-el-nuevo-proceso-de-reunificacion-familiar-para-ciudadanos-de-4-paises-latinos/', '//*[@id="menu-item-575"]/a/@href', 16),
(31, 'Nacional', 'https://enter504.com/', 'https://enter504.com/inversion-de-palmerola-international-airport-es-de-mas-de-135-millones-en-el-aeropuerto/', '//*[@id="menu-item-576"]/a/@href', 16),
(32, 'Deporte', 'https://enter504.com/', 'https://enter504.com/de-companero-a-rival-de-messi-neymar-interesa-a-un-campeon-de-la-mls/', '//*[@id="menu-item-573"]/a/@href', 16),
(33, 'Entretenimiento', 'https://enter504.com/', 'https://enter504.com/rauw-alejandro-lanza-playa-saturno-disco-que-le-rinde-homenaje-al-reggaeton-clasico/', '//*[@id="menu-item-577"]/a/@href', 16),
(34, 'Deporte', 'https://www.radiohrn.hn/', 'https://www.radiohrn.hn/lionel-messi-inter-miamo-fc-anuncia-cuando-presentara-oficialmente-2023-07-07', '//*[@id="sticky-navbar"]/div/div/div/ul/li[6]/a/@href', 17),
(35, 'Nacional', 'https://www.radiohrn.hn/', 'https://www.radiohrn.hn/diputados-cn-anterior-repartian-dinero-uno-dieron-l-113-millones-ong-senala-bartolo-fuentes-2023-07-07', '//*[@id="sticky-navbar"]/div/div/div/ul/li[3]/a/@href', 17),
(36, 'Internacional', 'https://www.radiohrn.hn/', 'https://www.radiohrn.hn/derrumbe-edificio-hombre-pedrada-turquia-video-2023-07-07', '//*[@id="sticky-navbar"]/div/div/div/ul/li[5]/a/@href', 17),
(37, 'Programacion', 'https://www.radiohrn.hn/', 'https://www.radiohrn.hn/programacion', '//*[@id="sticky-navbar"]/div/div/div/ul/li[7]/a/@href', 17),
(38, 'Deporte', 'https://rdsradio.hn/', 'https://rdsradio.hn/deportes-2/hondureno-mauricio-dubon-rompe-record-de-50-anos-en-los-astros-de-houston/', '//*[@id="menu-1-a842338"]/li[3]/a/@href', 19),
(39, 'Entretenimiento', 'https://rdsradio.hn/', 'https://rdsradio.hn/entretenimiento/rurouni-kenshin-2023-cuantos-capitulos-tiene-y-que-se-sabe-del-esperado-regreso-de-este-anime/', '//*[@id="menu-1-a842338"]/li[5]/a/@href', 19),
(40, 'Nacional', 'https://rdsradio.hn/', 'https://rdsradio.hn/noticias/no-hay-fecha-de-emision-para-nuevas-licencias-de-conducir/', '//*[@id="menu-1-4e0b7f4"]/li[1]/a/@href', 19),
(41, 'Internacional', 'https://rdsradio.hn/', 'https://rdsradio.hn/noticias/preven-un-aumento-de-huracanes-en-el-atlantico-debido-a-las-altas-temperaturas-del-mar/', '//*[@id="menu-1-4e0b7f4"]/li[2]/a/@href', 19),
(42, 'Nacional', 'https://www.radioamerica.hn/', 'https://www.radioamerica.hn/economista-pide-al-gobierno-tener-mucha-capacidad-en-negociacion-del-tratado-de-libre-comercio-con-china/', '//*[@id="nav-menu-item-494871"]/a/@href', 20),
(43, 'Internacional', 'https://www.radioamerica.hn/', 'https://www.radioamerica.hn/ee-uu-da-por-finalizada-la-destruccion-de-sus-reservas-de-armas-quimicas/', '//*[@id="nav-menu-item-494872"]/a/@href', 20),
(44, 'Deporte', 'https://www.radioamerica.hn/', 'https://www.radioamerica.hn/mexico-y-costa-rica-se-enfrentan-por-el-boleto-las-semifinales-de-la-copa-oro/', '//*[@id="nav-menu-item-494874"]/a/@href', 20),
(45, 'Entretenimiento', 'https://www.radioamerica.hn/', 'https://www.radioamerica.hn/romeo-santos-anade-22-conciertos-en-estados-unidos-y-canada-la-gira-formula-vol-3/', '//*[@id="nav-menu-item-494875"]/a/@href', 20),
(46, 'Nacional', 'https://www.radioprogresohn.net/', 'https://www.radioprogresohn.net/noticias-nacionales/nueve-conflictos-debidamente-vinculados-y-vinculantes/', '//*[@id="menu-item-30144"]/a/@href', 21),
(47, 'Internacional', 'https://www.radioprogresohn.net/', 'https://www.radioprogresohn.net/instante/papa-francisco-alienta-la-union-civil-para-parejas-homosexuales/', '//*[@id="menu-item-15104"]/a/@href', 21),
(48, 'Nacional', 'https://www.rcv.hn/', 'https://www.rcv.hn/2023/07/07/la-sub-23-de-honduras-gana-el-bronce-en-los-juegos-centroamericanos/', '//*[@id="menu-item-14"]/a/@href', 22),
(49, 'Sucesos', 'https://www.rcv.hn/', 'https://www.rcv.hn/2023/06/21/al-descubierto-12-sospechosas-responsables-de-la-tragedia-en-pnfas/', '//*[@id="menu-item-3908"]/a/@href', 22),
(50, 'Internacional', 'https://www.rcv.hn/', 'https://www.rcv.hn/2023/07/07/se-intensifica-temporada-de-huracanes-en-el-atlantico/', '//*[@id="menu-item-13"]/a/@href', 22),
(51, 'Deporte', 'https://www.rcv.hn/', 'https://www.rcv.hn/2023/07/07/se-anuncia-el-calendario-de-honduras-para-la-liga-de-naciones-2023-2024/', '//*[@id="menu-item-11"]/a/@href', 22),
(52, 'Deporte', 'https://www.televicentro.com/', 'https://www.deportestvc.com/la-h/jorge-luis-pinto-renuncia-a-su-club-en-colombia-y-se-convierte-en-opcion-para-honduras-2023-07-08', '//*[@id="deportes"]/a/@href', 23),
(53, 'Noticias', 'https://www.televicentro.com/', 'https://www.tunota.com/mundo/articulo/dos-muertos-y-un-desaparecido-tras-explosion-en-una-plataforma-petrolera-de-mexico', '//*[@id="barsNavigations"]/div/div/div[6]/a/@href', 23),
(54, 'Deporte', 'https://www.televicentro.com/', 'https://www.deportestvc.com/liga-nacional/marathon-confirma-fichaje-de-lujo-para-la-delantera-a-peticion-de-salomon-nazar', '//*[@id="deportes"]/a/@href', 23),
(55, 'Noticias', 'https://www.televicentro.com/', 'https://www.tunota.com/mundo/articulo/90-cadenas-perpetuas-patrick-crusius-asesino-23-personas-elpaso-texas-2023-07-07', '//*[@id="deportes"]/a/@href', 23),
(56, 'Entretenimiento', 'https://hch.tv//', 'https://entretenimiento.hch.tv/title/que-viva-la-vida-viernes-30-de-junio-del-2023/', '//*[@id="menu-item-1089939"]/a/@href', 24),
(57, 'Nacional', 'https://hch.tv/', 'https://hch.tv/2023/07/07/arranca-la-decima-edicion-del-festival-de-arte-y-cultura-gracias-convoca-2023/', '//*[@id="menu-item-936935"]/a/@href', 24),
(58, 'Deporte', 'https://canal6.com.hn/', 'https://canal6.com.hn/karim-benzema-recibio-su-primer-trofeo-pichichi.html', '//*[@id="tdi_209"]/@href', 25),
(59, 'Sucesos', 'https://canal6.com.hn/','https://canal6.com.hn/resultados-operacionales-de-requisa-en-el-centro-penitenciario-el-porvenir-atlantida-2.html', '//*[@id="tdi_217"]/@href',  25),
(60, 'Noticias', 'https://canal11.hn/', 'https://www.oncenoticias.hn/honduras-estado-tiempo/', '//*[@id="content"]/div/section[3]/div/div[2]/div/div[1]/div/figure/a/@href', 27),
(61, 'Deportes', 'https://canal11.hn/', 'https://canal11.hn/video/ya-se-armo-25-9-22/', '//*[@id="content"]/div/section[3]/div/div[4]/div/div/div/figure/a/@href', 27)
""")
conn.commit()

cur.execute("""INSERT INTO NoticiaEj (IDNoticia, URL, FechaXP, TituloXP, contXP, IDMedio) VALUES 
(1, 'https://www.laprensa.hn/premium/indice-ia-honduras-esta-grupo-rezagados-NO14291729', 'fecha', 'titulo', 'contenido', 1),
(2, 'https://www.elheraldo.hn/honduras/mateo-yibrin-negativa-construir-prosperidad-asegurar-elecciones-libres-2025-AH14311661', 'fecha', 'titulo', 'contenido', 2),
(3, 'https://tiempo.hn/carmen-y-gloria-las-gemelas-hondurenas/', 'fecha', 'titulo', 'contenido', 3),
(4, 'https://www.elpais.hn/sobrevivio-al-covid-y-a-eta-e-iota-vendiendo-agua-en-bolsa-en-las-calles/', 'fecha', 'titulo', 'contenido', 4),
(5, 'https://elmundo.hn/tlc-con-china-podria-afectar-exportaciones-de-camaron-hondureno/', 'fecha', 'titulo', 'contenido', 5),
(6, 'https://proceso.hn/dengue-sigue-en-aumento-con-6365-casos-a-nivel-nacional/', 'fecha', 'titulo', 'contenido', 6),
(7, 'https://www.latribuna.hn/2023/07/08/mueren-seis-personas-al-estrellarse-un-avion-privado-en-california/', 'fecha', 'titulo', 'contenido', 7),
(8, 'https://ellibertador.hn/2023/07/08/muda-queda-diputada-nacionalista-cuando-le-exhiben-su-familion-y-corrupcion/', 'fecha', 'titulo', 'contenido', 8),
(9, 'https://elpulso.hn/2023/07/07/el-presidente-xi-jinping-insta-al-ejercito-chino-a-reforzar-los-planes-de-guerra/', 'fecha', 'titulo', 'contenido', 9),
(10, 'https://lanoticia.hn/fijan-nuevo-precio-para-quintal-de-arroz-a-l500/', 'fecha', 'titulo', 'contenido', 10),
(11, 'https://www.diez.hn/internacionales/messi-ayudo-seleccion-argentina-rodrigo-de-paul-di-maria-aguero-campeon-mundial-qatar-GH14313885', 'fecha', 'titulo', 'contenido', 11),
(12, 'https://www.elarticulista.net/2022/08/murio-los-91-anos-mijail-gorbachov-el.html', 'fecha', 'titulo', 'contenido', 12),
(13, 'https://contextohn.com/nacional/personal-de-el-torax-se-esta-contagiando-de-coronavirus/', 'fecha', 'titulo', 'contenido', 13),
(14, 'https://eloncehn.com/index.php/2023/07/08/real-espana-cerca-de-quedarse-con-portero-centroamericano/', 'fecha', 'titulo', 'contenido', 14),
(15, 'https://diariogolazo.hn/otros-deportes/badosa-no-puede-con-rybakina-y-se-despide-de-indian-wells-en-segunda-ronda/19/', 'fecha', 'titulo', 'contenido', 15),
(16, 'https://enter504.com/se-filtra-el-iconico-traje-que-usara-wolverine-en-deadpool-3/', 'fecha', 'titulo', 'contenido', 16),
(17, 'https://www.radiohrn.hn/video-fallecen-seis-personas-al-estrellarse-avion-privado-en-california-2023-07-08', 'fecha', 'titulo', 'contenido', 17),
(18, 'https://rdsradio.hn/tecno/meta-adelanta-el-lanzamiento-de-threads-su-chat-para-competir-con-twitter/', 'fecha', 'titulo', 'contenido', 19),
(19, 'https://www.radioamerica.hn/encargados-de-movilizar-pandilleros-armas-y-drogas-desde-sps-tegucigalpa-son-capturados-por-la-dipampco/', 'fecha', 'titulo', 'contenido', 20),
(20, 'https://www.radioprogresohn.net/noticias-nacionales/nueve-conflictos-debidamente-vinculados-y-vinculantes/', 'fecha', 'titulo', 'contenido', 21),
(21, 'https://www.rcv.hn/2023/07/08/enfrentan-3-2-millones-de-personas-necesidades-alerta-onu-de-crisis-humanitaria-en-honduras/', 'fecha', 'titulo', 'contenido', 22),
(22, 'https://www.televicentro.com/juanchi-sufrio-maltrato-fisico-pareja-yailin-anuel-aa-2023-07-07', 'fecha', 'titulo', 'contenido', 23),
(23, 'https://hch.tv/2023/07/08/piden-al-cn-aprobar-con-urgencia-la-ley-transitoria-del-agonizante-ihss/', 'fecha', 'titulo', 'contenido', 24),
(24, 'https://canal6.com.hn/mas-de-600-hondurenos-fueron-deportados-en-los-primeros-ocho-dias-de-enero.html', 'fecha', 'titulo', 'contenido', 25),
(25, 'https://www.oncenoticias.hn/eeh-corte-energia/', 'fecha', 'titulo', 'contenido', 27),
(26, 'https://mayatv.hn/2023/07/que-sabemos-de-los-mamiferos-que-vivieron-entre-dinosaurios/', 'fecha', 'titulo', 'contenido', 28)
""")
conn.commit()

conn.close()