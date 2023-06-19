CREATE DATABASE IF NOT EXISTS Medios_Prensa;

USE Medios_Prensa;


CREATE TABLE IF NOT EXISTS Ubicaciones (
    Ciudad VARCHAR(30) PRIMARY KEY,
    Region VARCHAR(30),
    Pais VARCHAR(30),
    Continente VARCHAR(30)
);medios_prensamedios_prensamedios_prensa

CREATE TABLE IF NOT EXISTS MediosPrensa (
    NomPrensa VARCHAR(80) PRIMARY KEY,
    Cobertura VARCHAR(80),
    AFund YEAR,
    SWeb VARCHAR(500),medios_prensa

    Ciudad VARCHAR(30),
    FOREIGN KEY (Ciudad) REFERENCES Ubicaciones(Ciudad)
);

CREATE TABLE IF NOT EXISTS Categorias (
    Nomcat VARCHAR(30) PRIMARY KEY,
    PrinURL VARCHAR(500),
    EjemURL VARCHAR(500),
    Xpath VARCHAR(100),

    NomPrensa VARCHAR(80),
    FOREIGN KEY (NomPrensa) REFERENCES MediosPrensa(NomPrensa)
);

CREATE TABLE IF NOT EXISTS Fundadores (
    NomFund VARCHAR(50) PRIMARY KEY,
    FNac DATE
);

CREATE TABLE IF NOT EXISTS RedesSociales (
    IDRS INT1 PRIMARY KEY,
    Plataforma VARCHAR(30),
    NomUsuario VARCHAR(50),
    Numseg INT,
    ActualizaS DATE,

    NomPrensa VARCHAR(80),
    FOREIGN KEY (NomPrensa) REFERENCES MediosPrensa(NomPrensa)
);

CREATE TABLE IF NOT EXISTS Noticias (
    URL VARCHAR(500) PRIMARY KEY,
    FechaXP VARCHAR(100),
    TituloXP VARCHAR(100),
    ContXP VARCHAR(100),

    NomPrensa VARCHAR(80),
    FOREIGN KEY (NomPrensa) REFERENCES MediosPrensa(NomPrensa)
);

CREATE TABLE IF NOT EXISTS CuentaCon (
    NomPrensa VARCHAR(80),
    NomFund VARCHAR(50),
    PRIMARY KEY (NomPrensa, NomFund),
    FOREIGN KEY (NomPrensa) REFERENCES MediosPrensa(NomPrensa),
    FOREIGN KEY (NomFund) REFERENCES Fundadores(NomFund)
);


