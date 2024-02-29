CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    height FLOAT,
    position VARCHAR,
    tier INT
);

INSERT INTO players
    (id, first_name, last_name, height, position, tier)
VALUES
    (DEFAULT, 'Michael', 'Zhang', 5.9, 'Small Forward', 2),
    (DEFAULT, 'Stanley', 'Lin', 5.11, 'Power Forward', 1),
    (DEFAULT, 'Eric', 'Ngai', 5.9, 'Power Forward', 1),
    (DEFAULT, 'Will', 'Ho', 5.9, 'Forward', 2),
    (DEFAULT, 'Brian', 'Cen', 5.5, 'Point Guard', 2);
