DROP DATABASE IF EXISTS choose_your_story;
CREATE DATABASE choose_your_story;
USE choose_your_story;

-- Fase 2: Identidad
CREATE TABLE usuari (
    id_usuari INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE personatge (
    id_personatge INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL UNIQUE,
    descripcio TEXT
);

-- Fase 3: Aventuras y Pasos
CREATE TABLE aventura (
    id_aventura INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    descripcio TEXT
);

CREATE TABLE pas (
    id_pas INT AUTO_INCREMENT PRIMARY KEY,
    id_aventura INT NOT NULL,
    descripcio_text TEXT NOT NULL,
    es_final BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_aventura) REFERENCES aventura(id_aventura) ON DELETE CASCADE
);

-- Fase 4: Opciones
CREATE TABLE opcio (
    id_opcio INT AUTO_INCREMENT PRIMARY KEY,
    id_pas_actual INT NOT NULL,
    id_pas_seguent INT NOT NULL,
    text_resposta TEXT NOT NULL,
    FOREIGN KEY (id_pas_actual) REFERENCES pas(id_pas),
    FOREIGN KEY (id_pas_seguent) REFERENCES pas(id_pas)
);

-- 5. Tabla de Partidas
-- Aquí registramos qué USUARIO juega con qué PERSONAJE y en qué AVENTURA.
CREATE TABLE partida (
    id_partida INT AUTO_INCREMENT PRIMARY KEY,
    id_usuari INT NOT NULL,
    id_personatge INT NOT NULL,
    id_aventura INT NOT NULL,
    data_inici DATETIME NOT NULL, -- Para guardar la fecha y hora exacta
    FOREIGN KEY (id_usuari) REFERENCES usuari(id_usuari),
    FOREIGN KEY (id_personatge) REFERENCES personatge(id_personatge),
    FOREIGN KEY (id_aventura) REFERENCES aventura(id_aventura)
);

-- 6. Registro de decisiones tomadas en cada paso
CREATE TABLE decisio_partida (
    id_partida INT NOT NULL,
    id_pas INT NOT NULL,
    id_opcio_triada INT NOT NULL,
    PRIMARY KEY (id_partida, id_pas), -- Un registro por paso en cada partida
    FOREIGN KEY (id_partida) REFERENCES partida(id_partida),
    FOREIGN KEY (id_pas) REFERENCES pas(id_pas),
    FOREIGN KEY (id_opcio_triada) REFERENCES opcio(id_opcio)
);
