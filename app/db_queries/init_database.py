command = """
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS mailing;
DROP TABLE IF EXISTS workers;

CREATE TABLE IF NOT EXISTS workers (
    id SERIAL PRIMARY KEY,
    email TEXT,
    password TEXT,
    role INT
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email TEXT,
    groups TEXT
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
    marketolog INT,

    FOREIGN KEY (analyst) REFERENCES workers (id),
    FOREIGN KEY (product) REFERENCES workers (id),
    FOREIGN KEY (editor) REFERENCES workers (id),
    FOREIGN KEY (main_editor) REFERENCES workers (id),
    FOREIGN KEY (marketolog) REFERENCES workers (id)
);

"""
