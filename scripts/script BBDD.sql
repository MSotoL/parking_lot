/*
***********************************************************
       SCRIPT SQL (MYSQL) PARA LA CREACIÓN DE LA
       BASE DE DATOS Y TABLAS DE LA APLICACIÓN

        Desarrollado por: MIGUEL SOTO LOMBRIS

                    TFG - UNIR

***********************************************************
*/

/* **********  CREACIÓN DE LA BASE DE DATOS  *********** */
DROP DATABASE IF EXISTS PARKING_LOT_LAYOUT;
CREATE DATABASE IF NOT EXISTS PARKING_LOT_LAYOUT;

USE PARKING_LOT_LAYOUT;
/* ***************************************************** */

/* ELIMINACIÓN DE TABLAS POR SI YA EXISTIERAN PREVIAMENTE */
DROP TABLE PLAZAS;
DROP TABLE TIPOS_PLAZA;
DROP TABLE ZONAS;
DROP TABLE PLANTAS;
DROP TABLE EDIFICIOS;
DROP TABLE PARKINGS;
/* ***************************************************** */

/* ************  CREACIÓN DE TABLAS  ******************* */
CREATE TABLE PARKINGS (
    id_parking int NOT NULL AUTO_INCREMENT,
    ubicacion varchar(50),
    descripcion varchar(50),
    cubierto varchar(1) CHECK (cubierto = 's' OR cubierto = 'N'),
    num_plazas_grandes INT,
    num_plazas_peq INT,
    num_plazas_discap INT,
    CONSTRAINT parking_pk PRIMARY KEY (id_parking)
);

CREATE TABLE EDIFICIOS (
    id_edificio int NOT NULL AUTO_INCREMENT,
    id_parking int NOT NULL,
    descripcion varchar(50),
    num_plantas INT,
    completo varchar(1) CHECK (completo = 's' OR completo = 'N'),
    CONSTRAINT edificio_pk PRIMARY KEY (id_edificio),
    CONSTRAINT parking_fk FOREIGN KEY (id_parking) REFERENCES PARKINGS(id_parking)
);

CREATE TABLE PLANTAS (
    id_planta int NOT NULL AUTO_INCREMENT,
    id_edificio int NOT NULL,
    descripcion varchar(30),
    num_plazas_grandes INT,
    num_plazas_peq INT,
    num_plazas_discap INT,
    max_plazas INT,
    planta_completa varchar(1) CHECK (planta_completa = 's' OR planta_completa = 'n'),
    CONSTRAINT planta_pk PRIMARY KEY (id_planta),
    CONSTRAINT edificio_fk FOREIGN KEY (id_edificio) REFERENCES EDIFICIOS(id_edificio)
);

CREATE TABLE ZONAS (
    id_zona int NOT NULL AUTO_INCREMENT,
    id_planta int NOT NULL,
    descripcion varchar(30),
    CONSTRAINT zona_pk PRIMARY KEY (id_zona),
    CONSTRAINT planta_fk FOREIGN KEY (id_planta) REFERENCES PLANTAS(id_planta)
);

CREATE TABLE TIPOS_PLAZA (
    id_tipo_plaza int NOT NULL AUTO_INCREMENT,
    descripcion varchar(30),
    ancho decimal(3,2),
    largo decimal(3,2),
    CONSTRAINT tipo_plaza_pk PRIMARY KEY (id_tipo_plaza)
);

CREATE TABLE PLAZAS (
    id_plaza int NOT NULL AUTO_INCREMENT,
    id_zona int NOT NULL,
    id_tipo_plaza int NOT NULL,
    observaciones varchar(50),
    CONSTRAINT plaza_pk PRIMARY KEY (id_plaza),
    CONSTRAINT zona_fk FOREIGN KEY (id_zona) REFERENCES ZONAS(id_zona),
    CONSTRAINT tipo_plaza_fk FOREIGN KEY (id_tipo_plaza) REFERENCES TIPOS_PLAZA(id_tipo_plaza)
);
/* ***************************************************** */