CREATE DATABASE gestor_contrasena;
USE gestor_contrasena;

CREATE TABLE baul (
 id_baul int NOT NULL AUTO_INCREMENT,
 Plataforma varchar(80) NOT NULL,
 usuario varchar(80) NOT NULL,
 clave varchar(80) NOT NULL,
 PRIMARY KEY (id_baul),
 UNIQUE KEY Plataforma (Plataforma,usuario)
) ;

INSERT INTO baul (Plataforma, usuario, clave) VALUES
('facebook', 'angelo', '0412'),
('X', 'heliod', '6464'),
('youtube', 'josue', '2020'),
('twitter', 'sleed', '3647'),
