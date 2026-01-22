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
(20, 2, 'Llegas a la escena. La víctima sostiene un sobre de té y tiene los zapatos llenos de barro. ¿Qué investigas?', FALSE),
(21, 2, 'El cadáver huele a almendras amargas (cianuro) y tiene barro rojo en las botas. ¿Dónde buscas el origen?', FALSE),
(22, 2, 'El mayordomo dice: "Él nunca tomaba té en el estudio". Ves barro rojo en la alfombra. ¿Cómo sigues?', FALSE),
(23, 2, 'Entras al jardín. El jardinero está cavando un hoyo sospechoso. ¿Le ayudas o le registras?', FALSE),
(24, 2, 'En la cocina encuentras el frasco de té. Tiene huellas de alguien que usa guantes de seda. ¿Qué haces?', FALSE),
(25, 2, 'Usas la psicología: "El barro te delata". El mayordomo confiesa: "Vi al jardinero hablando con el gemelo".', FALSE),
(26, 2, 'El jardinero se asusta y te golpea con la pala. Te entierra vivo. Has muerto.', TRUE),
(27, 2, 'Tienes las pruebas: barro rojo, guantes de seda y el veneno. Reúnes a todos. ¿A quién confrontas?', FALSE),
(28, 2, 'Acusas al mayordomo. Él ríe y muestra sus manos limpias. El verdadero asesino escapa. Fallo.', TRUE),
(29, 2, '¡ÉXITO! El gemelo usó los guantes y el jardinero puso el veneno. El barro rojo del jardín los delata.', TRUE),
(30, 2, 'Acusas solo al jardinero. Él confiesa, pero el gemelo (el cerebro) queda libre y te mata después. Fallo.', TRUE);

INSERT INTO opcio (id_pas_actual, id_pas_seguent, text_resposta) VALUES 
(20, 21, 'Analizar pistas en el cuerpo'),
(20, 22, 'Interrogar al mayordomo'),
(21, 23, 'Ir al jardín (por el barro)'),
(21, 24, 'Ir a la cocina (por el té)'),
(22, 25, 'Analizar la alfombra con barro'),
(22, 24, 'Ir a la cocina a por el té'),
(23, 26, 'Ayudar al jardinero'),
(23, 27, 'Registrar su cobertizo'),
(24, 27, 'Ir al salón con el frasco'),
(25, 27, 'Llamar a todos al salón'),
(27, 28, 'Confrontar al Mayordomo'),
(27, 29, 'Confrontar al Gemelo y al Jardinero'),
(27, 30, 'Confrontar solo al Jardinero');

-- ======================================================
-- PERSONAJES (Solo los dos originales)
-- ======================================================
INSERT INTO personatge (id_personatge, nom, descripcio) VALUES 
(1, 'Agente Eustakio', 'Especialidad: Investigador con gran ojo para los detalles.'),
(2, 'Agente Manuel', 'Especialidad: Soldado experto en tácticas de asalto.');
