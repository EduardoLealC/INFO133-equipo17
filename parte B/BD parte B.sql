CREATE DATABASE IF NOT EXISTS ParteB;

USE ParteB;

CREATE TABLE IF NOT EXISTS Pais (
    NomPais VARCHAR(30) PRIMARY KEY,
    Poblacion VARCHAR(30),
    Superficie VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS Region (
    NumRegion INT1 PRIMARY KEY,
    NomRegion VARCHAR(30),

    NomPais VARCHAR(30),
    FOREIGN KEY (NomPais) REFERENCES Pais(NomPais)
);

CREATE TABLE IF NOT EXISTS Comuna (
    CUT INT1 PRIMARY KEY,
    Habitantes INT,
    NomComuna VARCHAR(30),
    Superficie INT,

    NumRegion INT1,
    FOREIGN KEY (NumRegion) REFERENCES Region(NumRegion)
);

CREATE TABLE IF NOT EXISTS Trabajo (
    IDTrabajo INT PRIMARY KEY,
    Genero BOOL,
    Ocupadas INT,
    Desocupadas INT,

    CUT INT1,
    FOREIGN KEY (CUT) REFERENCES Comuna(CUT)
);

CREATE TABLE IF NOT EXISTS Salud (
    IDSalud INT PRIMARY KEY,
    CantEstab INT,
    TipoEstSal INT1,

    CUT INT1,
    FOREIGN KEY (CUT) REFERENCES Comuna(CUT)
);

CREATE TABLE IF NOT EXISTS Educacion (
    IDEd INT PRIMARY KEY,
    TipoEstEd VARCHAR(60),
    CantEstab INT,

    CUT INT1,
    FOREIGN KEY (CUT) REFERENCES Comuna(CUT)
);

CREATE TABLE IF NOT EXISTS Entretencion (
    IDEnt INT,
    NomArea VARCHAR(60),
    Promulgacion DATE,
    Tipo VARCHAR(50),

    CUT INT1,
    FOREIGN KEY (CUT) REFERENCES Comuna(CUT)
);


