DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userName TEXT NOT NULL,
    phoneNumber TEXT NOT NULL,
    colors TEXT NOT NULL
);

INSERT INTO users (userName, phoneNumber, colors) VALUES ('colin', '+15864573219', 'Green, Blue');

SELECT * FROM users;

INSERT INTO users (userName, phoneNumber, colors) VALUES ('John', '+15864573219', 'Black, Red');

SELECT * FROM users;
