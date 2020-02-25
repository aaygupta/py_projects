-------------------------------

-- CREATE TABLE plays (
--   id INTEGER NOT NULL,
--   title VARCHAR(40) NOT NULL,
--   writer VARCHAR(40) NOT NULL,
--   UNIQUE(id)
-- );

-- CREATE TABLE reservations (
--   id INTEGER NOT NULL,
--   play_id INTEGER NOT NULL,
--   number_of_tickets INTEGER NOT NULL,
--   theater VARCHAR(40) NOT NULL,
--   UNIQUE(id)
-- );

-------------------------------

-- INSERT INTO plays VALUES (109, "Queens and Kings of Madagascar", "Paul Sat");
-- INSERT INTO plays VALUES (123, "Merlin", "Lee Roy");
-- INSERT INTO plays VALUES (142, "Key of the tea", "Max Rogers");
-- INSERT INTO plays VALUES (144, "ROMEance Comedy", "Bohring Ashell");
-- INSERT INTO plays VALUES (145, "Nameless.", "Note Nul");

-- INSERT INTO reservations VALUES (13, 109, 12, "Mc Rayleigh Theater");
-- INSERT INTO reservations VALUES (24, 109, 34, "Mc Rayleigh Theater");
-- INSERT INTO reservations VALUES (37, 145, 84, "Mc Rayleigh Theater");
-- INSERT INTO reservations VALUES (49, 145, 45, "Mc Rayleigh Theater");
-- INSERT INTO reservations VALUES (51, 145, 41, "Mc Rayleigh Theater");
-- INSERT INTO reservations VALUES (68, 123, 3, "Mc Rayleigh Theater");
-- INSERT INTO reservations VALUES (83, 142, 46, "Mc Rayleigh Theater");

-------------------------------

SELECT p.id, p.title, SUM(r.number_of_tickets) AS reserved_tickets
FROM reservations r JOIN plays p
ON r.play_id = p.id
GROUP BY p.id ORDER BY reserved_tickets DESC, p.id ASC