USE choose_your_story;

-- Informe de Respuesta más usada
SELECT 
    CONCAT(a.id_aventura, ' - ', a.nom) AS "ID AVENTURA - NOMBRE", -- Concat para concatenar lo que habra en el interior de la tabla y as para poner el titulo de la columna
    a.nom AS "NOMBRE",
    CONCAT(p.id_pas, ' - ', SUBSTRING(p.descripcio_text, 1, 30), '...') AS "ID PASO - DESCRIPCION",
    p.descripcio_text AS "DESCRIPCION",
    CONCAT(o.id_opcio, ' - ', SUBSTRING(o.text_resposta, 1, 30), '...') AS "ID RESPUESTA - DESCRIPCION",
    o.text_resposta AS "DESCRIPCION RESPUESTA",
    COUNT(dp.id_opcio_triada) AS "NUMERO VECES SELECCIONADA" -- count para contar cuantos id de opcio triada hay que es  = a cuantas veces ha sido selecionada
FROM aventura a
JOIN pas p ON a.id_aventura = p.id_aventura
JOIN opcio o ON p.id_pas = o.id_pas_actual
LEFT JOIN decisio_partida dp ON o.id_opcio = dp.id_opcio_triada
GROUP BY a.id_aventura, p.id_pas, o.id_opcio
ORDER BY a.id_aventura ASC, p.id_pas ASC;

-- Informe de usuario que mas partidas ha jugado
SELECT 
    u.username AS "NOMBRE USUARIO",
    COUNT(pa.id_partida) AS "PARTIDAS JUGADAS"
FROM usuari u
JOIN partida pa ON u.id_usuari = pa.id_usuari
GROUP BY u.id_usuari, u.username
ORDER BY `PARTIDAS JUGADAS` DESC, u.id_usuari ASC
LIMIT 1;

-- Informe de historial de aventuras por usuario
SELECT 
    a.id_aventura AS "idadventure",
    a.nom AS "Name",
    p.data_inici AS "date"
FROM partida p
JOIN aventura a ON p.id_aventura = a.id_aventura
JOIN usuari u ON p.id_usuari = u.id_usuari
WHERE u.username = 'erik'
ORDER BY p.data_inici DESC;