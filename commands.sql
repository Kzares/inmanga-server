CREATE TABLE mangas( 
    id UUID NOT NULL PRIMARY KEY, 
    title VARCHAR(150) NOT NULL, 
    released DATE NOT NULL, 
    author VARCHAR(150) NOT NULL, 
    sinopsis VARCHAR(1000) NOT NULL, 
    review VARCHAR(1000) NOT NULL, 
    likes INT NOT NULL, 
    score FLOAT NOT NULL, 
    points INT NOT NULL,
    categories json 
);
CREATE TABLE users( id UUID NOT NULL PRIMARY KEY, username VARCHAR(150) NOT NULL, password VARCHAR(150) NOT NULL, saved json,hidden json,liked json);
CREATE TABLE admins( 
    id UUID NOT NULL PRIMARY KEY, 
    username VARCHAR(150) NOT NULL, 
    password VARCHAR(150) NOT NULL
);
INSERT INTO admins (id,username,password) VALUES ('a455f7cc-45dc-44a7-9b9e-d3c3bccb501b', 'admin', 'password') ;

INSERT INTO users (id,username,password,saved,hidden, liked) VALUES ('a455f7cc-45dc-44a7-9b9e-d3c3bccb501b', 'username', 'password', '["a455f7cc-45dc-44a7-9b9e-d3c3bccb501a"]'::jsonb , '["a455f7cc-45dc-44a7-9b9e-d3c3bccb501a"]'::jsonb , '["a455f7cc-45dc-44a7-9b9e-d3c3bccb501a"]'::jsonb  );

ALTER TABLE mangas ALTER COLUMN categories TYPE jsonb USING categories::jsonb
ALTER TABLE users ALTER COLUMN saved TYPE jsonb USING saved::jsonb;
ALTER TABLE users ALTER COLUMN hidden TYPE jsonb USING hidden::jsonb;
ALTER TABLE users ALTER COLUMN liked TYPE jsonb USING liked::jsonb;

\c inmanga


INSERT INTO mangas(id, title, released, author, sinopsis, review, likes, score, points, categories)
VALUES 
    ('a455f7cc-45dc-44a7-9b9e-d3c3bccb501a', 'vagabond', '1998-01-01', 'takehiko inoue', 'La historia de Miyamoto Musashi, quien se convierte en uno de los espadachines más legendarios de Japón. A lo largo del camino, se involucra en varias aventuras y enfrenta a numerosos oponentes', 'Una historia impresionante y muy bien dibujada. Los personajes son geniales y el estilo de lucha de la espada es muy realista. Realmente te sumerge en el mundo del espadachín', 418, 8.9, 846, '["shounen", "accion", "drama"]'::jsonb ),

    ('f328f7cc-45dc-44a7-9b9e-d3c3bccb501a', 'berserk', '1991-03-10', 'kentaro miura', 'Guts, el guerrero negro, busca venganza contra su ex compañero Griffith, quien le traicionó y sacrificó a sus amigos. En su camino se encuentra con varios nuevos aliados y enemigos, mientras lucha contra demonios y otros seres sobrenaturales', 'Una historia épica y emocionante que te mantiene al borde de tu asiento. Los personajes son geniales y el arte es impresionante. Altamente recomendado', 712, 9.7, 1221, '["shounen", "accion", "drama"]'::jsonb),

    ('f94af7cc-45dc-44a7-9b9e-d3c3bccb501a', 'uzumaki', '1998-01-01', 'junji ito', 'La historia de una pequeña ciudad llamada Kurozu-cho, que se ve afectada por una maldición relacionada con la forma de una espiral. A medida que la maldición se propaga, los habitantes de la ciudad se ven obligados a enfrentar situaciones cada vez más extrañas y grotescas', 'Muy buen horror cósmico japonés. La historia y los personajes son muy interesantes y el horror se muestra a través de la locura y las obsesiones de los personajes', 294, 8.3, 679, '["shounen","horror","accion", "drama"]'::jsonb);

INSERT INTO mangas (id, title, released, author, sinopsis, review, likes, score, points, categories)
VALUES ('a5a29b5c-c6a3-4171-994e-92db6b43601a', 'kimetsu no yaiba', '2016-02-15', 'koyoharu gotouge',
'A young boy becomes a demon hunter after his family is slaughtered by demons, and sets out on a quest to find a cure for his demonized sister.', 'Kimetsu no Yaiba is a beautifully drawn manga with a compelling story that will tug at your heartstrings. The characters are well-written and the action scenes are breathtaking. Highly recommended!', 3500, 9.2, 300, '["shounen", "accion", "drama"]'::jsonb);

INSERT INTO mangas (id, title, released, author, sinopsis, review, likes, score, points, categories)
VALUES ('ebaadfd4-4da4-4a67-ba08-38e19479e283', 'chainsaw man', '2018-12-03', 'tatsuki fujimoto', 
'A chainsaw-wielding demon hunter fights to protect humanity from the monsters that inhabit the world.', 'Chainsaw Man is an extremely fun and adrenaline-packed manga that will keep you hooked from start to finish. The characters are memorable and the story is full of twists and turns that will leave you on the edge of your seat', 1500, 9.5, 500, '["shounen", "accion", "drama"]'::jsonb);

INSERT INTO mangas (id, title, released, author, sinopsis, review, likes, score, points, categories) VALUES ('d31809f2-d7ab-4e5d-b7f9-9d9cdfc4f4ad', 'tokyo ghoul', '2011-09-08', 'sui ishida', 'A young man becomes a ghoul after being attacked by one, and must navigate being half-human, half-monster in a world that hates and fears his kind.', 'Tokyo Ghoul is a dark and thrilling manga that will leave you wanting more. The character development is excellent and the story is full of unexpected twists and turns. Highly recommended!', 2500, 8.7, 200, '["shounen","horror", "accion", "drama"]'::jsonb)

INSERT INTO mangas(id, title, released, author, sinopsis, review, likes, score, points, categories) 
VALUES 
    ('87b0f9d9-7a98-40e2-af36-b1d86f7c647d', 'one piece', '1997-07-22', 'eiichiro oda', 'Monkey D Luffy y su tripulación de piratas buscan el tesoro oculto conocido como "One Piece", mientras se enfrentan a desafíos y oponentes poderosos', 'Una historia emocionante y divertida que es perfecta para los fanáticos del género de aventuras. Los personajes son divertidos y la historia es muy imaginativa', 10251, 9.8, 2142, '["shounen", "aventuras", "accion", "comedia"]'::jsonb), 

    ('a2257c33-3d04-499e-b911-e817fda0d1b8', 'naruto', '1999-09-21', 'masashi kishimoto', 'Naruto Uzumaki es un joven ninja con el sueño de convertirse en el líder de su aldea y ser reconocido como el mejor ninja de todos. A lo largo del camino, se enfrenta a numerosos retos y enemigos', 'Una historia emocionante y absorbente que es perfecta para los fanáticos del género "shounen". Los personajes son muy interesantes y la historia es muy bien escrita', 8124, 9.6, 1921, '["shounen", "aventuras", "accion", "comedia"]'::jsonb),

    ('f44eb3dc-0577-4c9b-a1ad-d8cb50b70c4f', 'hunter x hunter', '1998-03-04', 'yoshihiro togashi', 'Gon Freecss, un joven que busca convertirse en un cazador, abandona su casa y se dirige a la torre de examen donde se deben superar una serie de duras pruebas para acceder al título de cazador', 'Una historia emocionante y llena de acción que es adictiva desde el principio hasta el final. Los personajes están bien desarrollados y la trama es muy intrigante', 5063, 9.3, 1367, '["shounen", "aventuras", "accion", "fantasia"]'::jsonb),

    ('bfb4f4c4-4b2b-4e6b-9e27-9deaac9d010c', 'jujutsu kaisen', '2018-03-05', 'gege akutami', 'Yuji Itadori, un joven con habilidades sobrenaturales, se une al mundo de los jujutsu, una forma de combatir a los demonios y maldiciones que amenazan al mundo humano', 'Una historia muy interesante y emocionante que es perfecta para los fanáticos del género "shounen". Los personajes son muy atractivos y la trama es muy bien desarrollada', 2230, 9.5, 620, '["shounen", "fantasia", "horror", "accion"]'::jsonb),

    ('c0405fb1-5f5a-4dbb-b832-2033e3973ecc', 'attack on titan', '2009-09-09', 'hajime isayama', 'La humanidad vive en ciudades rodeadas de altos muros para protegerse de los titanes, unos seres gigantes que intentan devorar a los humanos. Eren Yeager, Mikasa Ackerman y Armin Arlert se unen al ejército para luchar contra los titanes', 'Una historia emocionante y llena de acción que es perfecta para los fanáticos del género "shounen". Los personajes son muy interesantes y la trama es muy bien desarrollada', 10212, 9.7, 2401, '["shounen", "horror", "accion", "drama"]'::jsonb),

    ('8b3185d5-d23a-4125-8523-3abd26d3dbdf', 'death note', '2003-12-01', 'tsugumi ohba', 'Un estudiante de secundaria llamado Light Yagami encuentra un misterioso cuaderno que le da el poder de matar a cualquier persona cuyo nombre escriba en el cuaderno. Light comienza a utilizar el cuaderno para eliminar a los criminales y convertirse en un justiciero', 'Una historia emocionante y llena de intriga que es perfecta para los fanáticos del género "thriller". Los personajes son muy interesantes y el concepto de la historia es muy original', 9153, 9.4, 1873, '["thriller", "misterio", "psicologico"]'::jsonb),

    ('a1ed717a-bbdd-4cee-b9fc-2937e33517af', 'aullmetal alchemist', '2001-07-12', 'hiromu arakawa', 'Dos hermanos, Edward y Alphonse Elric, intentan recuperar sus cuerpos después de haberlos perdido en un intento fallido de resucitar a su madre utilizando la alquimia. Juntos se embarcan en una búsqueda para encontrar la Piedra Filosofal, que se dice que puede conceder cualquier deseo', 'Una historia emocionante y llena de acción que es perfecta para los fanáticos dela fantasía y la aventura. Los personajes son muy interesantes y la trama es muy bien desarrollada', 8790, 9.5, 2137, '["shounen", "aventuras", "fantasia", "drama"]'::jsonb);

    ('2192e281-0c0d-4a7a-b290-e008f0c515ba', 'My Hero Academia', '2014-07-07', 'Kohei Horikoshi', 'Izuku Midoriya, un joven sin superpoderes en un mundo donde la mayoría de la gente los tiene, sueña con ser un héroe como su ídolo All Might. Cuando All Might lo elige como su sucesor, Izuku comienza su entrenamiento para convertirse en un héroe', 'Una historia emocionante y llena de acción que es perfecta para los fanáticos del género "shounen". Los personajes son muy atractivos y la trama es muy bien desarrollada', 6895, 9.2, 1960, '"shounen", "accion", "fantasia", "comedia"'::jsonb), 

    ('2058d42c-3f2e-4b4e-8a62-98112c4e2f57', 'Demon Slayer', '2016-02-15', 'Koyoharu Gotouge', 'Tanjiro Kamado se convierte en un cazador de demonios para vengar la muerte de su familia y curar a su hermana, quien se convirtió en un demonio tras el ataque. A lo largo del camino, enfrenta muchos desafíos y conoce a aliados y enemigos poderosos', 'Una historia emocionante y bien escrita que es perfecta para los fanáticos del género "shounen". Los personajes son geniales y la trama es muy intrigante', 4670, 9.3, 1353, '"shounen", "accion", "drama"'::jsonb);

