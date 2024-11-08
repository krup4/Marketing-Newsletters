command = """
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS workers (
    id SERIAL PRIMARY KEY,
    email TEXT,
    password TEXT,
    role INT
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email TEXT,
);

CREATE TABLE IF NOT EXISTS mailing (
    id SERIAL PRIMARY KEY,
    theme TEXT,
    target TEXT,
    community TEXT,
    template TEXT,
    status INT,
    analyst INT,
    product INT,
    editor INT,
    main_editor INT,
    marketolog INT
);

"""
