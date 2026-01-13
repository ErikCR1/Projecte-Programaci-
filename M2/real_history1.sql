USE choose_your_story;

-- 1. LIMPIEZA TOTAL (Para que no se mezclen historias)
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE decisio_partida;
TRUNCATE TABLE partida;
TRUNCATE TABLE opcio;
TRUNCATE TABLE pas;
TRUNCATE TABLE aventura;
SET FOREIGN_KEY_CHECKS = 1;

-- 2. TU AVENTURA
INSERT INTO aventura (id_aventura, nom, descripcio) 
VALUES (1, 'Rescate Crítico', 'Misión de alto riesgo para salvar a un rehén.');

-- 3. TODOS LOS PASOS (Los 7 cuadros de tu esquema)
INSERT INTO pas (id_pas, id_aventura, descripcio_text, es_final) VALUES 
(1, 1, 'Situación: Tienes que salvar al rehén. ¿Fuerza o Hablar?', FALSE),
(2, 1, 'Sacas tu arma. El criminal se pone nervioso. ¿Disparar o Amenazar?', FALSE),
(3, 1, 'Decides guardar el arma. ¿Hablas de forma calmada o agresiva?', FALSE),
(4, 1, '¡Misión Cumplida! El criminal ha sido asesinado y el rehén está a salvo.', TRUE),
(5, 1, '¡Misión Fallida! Te has demorado amenazando y el criminal te ha matado.', TRUE),
(6, 1, '¡Misión Cumplida! El criminal acepta tus términos y se entrega.', TRUE),
(7, 1, '¡Misión Fallida! El criminal se asusta por tu agresividad y se tira con el rehén.', TRUE);

-- 4. TODAS LAS OPCIONES (Las flechas que conectan todo)
INSERT INTO opcio (id_pas_actual, id_pas_seguent, text_resposta) VALUES 
-- De la situación inicial
(1, 2, 'Fuerza'),
(1, 3, 'Hablar'),
-- Desde "Sacas un arma"
(2, 4, 'Disparar'),
(2, 5, 'Amenazar'),
-- Desde "Hablas con el criminal"
(3, 6, 'Hablar calmado'),
(3, 7, 'Hablar agresivo');

-- 5. PERSONAJE (Para poder jugar)
INSERT INTO personatge (id_personatge, nom, descripcio) 
VALUES (1, 'Agente Especial', 'Experto en tácticas de rescate.');
