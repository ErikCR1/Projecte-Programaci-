USE choose_your_story;

-- 1. LIMPIEZA TOTAL
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE decisio_partida;
TRUNCATE TABLE partida;
TRUNCATE TABLE opcio;
TRUNCATE TABLE pas;
TRUNCATE TABLE aventura;
SET FOREIGN_KEY_CHECKS = 1;

-- 2. DEFINICIÓN DE LA AVENTURA
INSERT INTO aventura (id_aventura, nom, descripcio) 
VALUES (1, 'Rescate Crítico: Infiltración', 'Misión de rescate que escala hasta el corazón de la organización criminal.');

-- 3. TODOS LOS PASOS (Escenas de tu historia)
INSERT INTO pas (id_pas, id_aventura, descripcio_text, es_final) VALUES 
(1, 1, 'Situación: Tienes que salvar al rehén. El criminal lo tiene encañonado. ¿Qué haces?', FALSE),
(2, 1, 'Sacas el arma. El criminal se pone muy nervioso. ¿Disparar o Amenazar?', FALSE),
(3, 1, 'Decides intentar razonar. ¿Hablas de forma calmada o agresiva?', FALSE),
(4, 1, 'Disparas, el criminal muere, el rehén está a salvo. ¿Qué haces ahora?', FALSE),
(5, 1, 'Misión Fallida: Fuiste lento y el criminal disparó primero. Has muerto.', TRUE),
(6, 1, 'El criminal se entrega. Lo tienes esposado. ¿Cómo procedes?', FALSE),
(7, 1, 'Misión Fallida: El criminal se asusta y se tira con el rehén. Mueren ambos.', TRUE),

-- RAMA DEL REHÉN (Viene del paso 4)
(8, 1, 'Interrogas al rehén. Tras presionarlo, confiesa: Es parte de la organización, te lleva a su base. ¿Cómo entras?', FALSE),
(9, 1, 'Intentas entrar en sigilo, pero una mina oculta explota. Has muerto.', TRUE),
(10, 1, 'Entras en asalto total. Estás en el centro de la base enemiga. ¡Misión cumplida!', TRUE),

-- RAMA DEL CRIMINAL (Viene del paso 6)
(11, 1, 'Interrogas al criminal. ¿Cómo le hablas, con suavidad o amenazante?', FALSE),
(12, 1, 'Le hablas con suavidad. El criminal se ríe de ti y no dice nada. Se acaba el tiempo.', TRUE),
(13, 1, 'Eres muy amenazante. El criminal, aterrado, te da la ubicación del Cuartel General.', FALSE),

-- ENFRENTAMIENTO FINAL CONTRA EL JEFE (Viene del paso 13)
(14, 1, 'Estás frente al Jefe. Tiene un detonador en la mano. ¿Disparas a la mano o intentas placarlo?', FALSE),
(15, 1, 'Fallo: El Jefe es más rápido y activa la bomba. Todo explota. Has muerto.', TRUE),
(16, 1, '¡ÉXITO TOTAL! Has neutralizado al Jefe y desarticulado la organización. Eres un héroe.', TRUE);

-- 4. TODAS LAS OPCIONES (Conexiones)
INSERT INTO opcio (id_pas_actual, id_pas_seguent, text_resposta) VALUES 
-- Inicio
(1, 2, 'Usar la fuerza'),
(1, 3, 'Intentar hablar'),

-- Rama Fuerza
(2, 4, 'Disparar al criminal'),
(2, 5, 'Amenazar (Mueres)'),

-- Rama Hablar
(3, 6, 'Hablar calmado (Éxito)'),
(3, 7, 'Hablar agresivo (Mueren)'),

-- Conexión al interrogatorio del Rehén (Desde paso 4)
(4, 8, 'Interrogar al rehén de forma correcta'),

-- Decisiones en la Base (Sigilo o Asalto)
(8, 9, 'Entrar en Sigilo (Mueres por mina)'),
(8, 10, 'Entrar en Asalto (Victoria)'),

-- Conexión al interrogatorio del Criminal (Desde paso 6)
(6, 11, 'Iniciar interrogatorio al criminal'),

-- El interrogatorio debe ser amenazante (Desde paso 11)
(11, 12, 'Ser amable (Fallo)'),
(11, 13, 'Ser amenazante (Te da la ubicación)'),

-- Enfrentamiento contra el Jefe (Desde paso 13)
(13, 14, 'Ir al Cuartel General a por el Jefe'),

-- Decisión final (Desde paso 14)
(14, 15, 'Placarlo (Mueres)'),
(14, 16, 'Disparar a la mano (Victoria Final)');

-- 5. PERSONAJE
INSERT INTO personatge (id_personatge, nom, descripcio) 
VALUES (1, 'Agente Eustakio. Especialidad: Investigador', 'Agente Manuel. Especialidad: Soldado');
