USE choose_your_story;

-- 1. LIMPIEZA TOTAL
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE decisio_partida;
TRUNCATE TABLE partida;
TRUNCATE TABLE opcio;
TRUNCATE TABLE pas;
TRUNCATE TABLE aventura;
TRUNCATE TABLE personatge;
SET FOREIGN_KEY_CHECKS = 1;

-- ======================================================
-- AVENTURA 1: RESCATE CRÍTICO
-- ======================================================
INSERT INTO aventura (id_aventura, nom, descripcio) 
VALUES (1, 'Rescate Crítico: Infiltración', 'Misión de rescate contra una organización criminal.');

INSERT INTO pas (id_pas, id_aventura, descripcio_text, es_final) VALUES 
(1, 1, 'Situación: El criminal tiene al rehén encañonado. ¿Qué haces?', FALSE),
(2, 1, 'Sacas el arma. El criminal se pone nervioso. ¿Disparar o Amenazar?', FALSE),
(3, 1, 'Decides razonar. ¿Hablas de forma calmada o agresiva?', FALSE),
(4, 1, 'Disparas, el criminal muere, el rehén se salva. ¿Qué haces ahora?', FALSE),
(5, 1, 'Misión Fallida: El criminal disparó primero. Has muerto.', TRUE),
(6, 1, 'El criminal se entrega. Lo tienes esposado. ¿Cómo procedes?', FALSE),
(7, 1, 'Misión Fallida: El criminal se asusta y salta con el rehén. Mueren ambos.', TRUE),
(8, 1, 'Interrogas al rehén. Confiesa ser un traidor. ¿Cómo entras a la base?', FALSE),
(9, 1, 'Misión Fallida: Una mina oculta explota en la entrada.', TRUE),
(10, 1, '¡Misión cumplida! Has tomado el control de la base.', TRUE),
(11, 1, 'Interrogas al criminal. ¿Cómo le hablas?', FALSE),
(12, 1, 'Misión Fallida: Se ríe de ti y el tiempo se agota.', TRUE),
(13, 1, 'Te da la ubicación del Jefe tras ser amenazado.', FALSE),
(14, 1, 'Frente al Jefe. Tiene un detonador. ¿Disparas o lo placas?', FALSE),
(15, 1, 'Misión Fallida: Todo explota.', TRUE),
(16, 1, '¡ÉXITO TOTAL! Eres un héroe nacional.', TRUE);

INSERT INTO opcio (id_pas_actual, id_pas_seguent, text_resposta) VALUES 
(1, 2, 'Usar la fuerza'), (1, 3, 'Intentar hablar'),
(2, 4, 'Disparar'), (2, 5, 'Amenazar'),
(3, 6, 'Calmado'), (3, 7, 'Agresivo'),
(4, 8, 'Interrogar al rehén'),
(8, 9, 'Sigilo'), (8, 10, 'Asalto'),
(6, 11, 'Interrogar criminal'),
(11, 12, 'Ser amable'), (11, 13, 'Ser amenazante'),
(13, 14, 'Ir a por el Jefe'),
(14, 15, 'Placarlo'), (14, 16, 'Disparar a la mano');

-- ======================================================
-- AVENTURA 2: EL MISTERIO DE LA MANSIÓN (DETECTIVE)
-- ======================================================
INSERT INTO aventura (id_aventura, nom, descripcio) 
VALUES (2, 'Muerte en la casa de los Gemelos', 'Un gemelo ha sido asesinado. Debes encontrar al culpable antes de que escape.');

INSERT INTO pas (id_pas, id_aventura, descripcio_text, es_final) VALUES 
(20, 2, 'Llegas a la escena. El cuerpo está en el estudio. ¿Revisas el cadáver o interrogas al mayordomo?', FALSE),
(21, 2, 'Encuentras un pétalo de orquídea en la mano de la víctima. ¿Buscas en el jardín o en la cocina?', FALSE),
(22, 2, 'El mayordomo parece nervioso. ¿Le presionas agresivamente o usas la psicología?', FALSE),
(23, 2, 'En el jardín, alguien te golpea por la espalda. Has muerto.', TRUE),
(24, 2, 'En la cocina encuentras veneno oculto en un frasco de té. ¿A quién confrontas?', FALSE),
(25, 2, 'El mayordomo confiesa que el gemelo estaba en el jardín. Vas a buscarlo.', FALSE),
(26, 2, 'Intentas arrestar al gemelo, pero el te dispara. Has muerto.', TRUE),
(27, 2, 'Con las pruebas del veneno y la orquídea, reúnes a todos en el salón. ¿Quién es el asesino?', FALSE),
(28, 2, 'Acusas al mayordomo sin pruebas suficientes. Te demandan y pierdes tu placa. Fallo.', TRUE),
(29, 2, '¡ÉXITO! Pruebas que el gemelo y el jardinero eran cómplices. Caso cerrado, detective.', TRUE);

INSERT INTO opcio (id_pas_actual, id_pas_seguent, text_resposta) VALUES 
(20, 21, 'Revisar el cadáver'), (20, 22, 'Hablar con el mayordomo'),
(21, 23, 'Ir al jardín solo'), (21, 24, 'Investigar la cocina'),
(22, 25, 'Usar psicología'), (22, 23, 'Presionar agresivamente'),
(24, 27, 'Reunir a los sospechosos'),
(25, 27, 'Ir al salón principal'),
(27, 28, 'Acusar al mayordomo'), (27, 29, 'Acusar al gemelo');

-- ======================================================
-- PERSONAJES (Solo los dos originales)
-- ======================================================
INSERT INTO personatge (id_personatge, nom, descripcio) VALUES 
(1, 'Agente Eustakio', 'Especialidad: Investigador con gran ojo para los detalles.'),
(2, 'Agente Manuel', 'Especialidad: Soldado experto en tácticas de asalto.');
