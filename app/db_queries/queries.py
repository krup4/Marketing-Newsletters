import os
import psycopg2
from psycopg2 import extras
from db_queries.init_database import command

user = os.environ['POSTGRES_USERNAME']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
database = os.environ['POSTGRES_DATABASE']
connection = psycopg2.connect(user=user,
                              password=password,
                              host=host,
                              port=port,
                              database=database)


def init_db():
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(command)
            connection.commit()


def add_worker(data):
    query = f"INSERT INTO workers ("
    for key, _ in data.items():
        query += f"{key}, "
    query = query[:-2] + ") VALUES ("

    for _, value in data.items():
        if type(value) == int:
            query += f"{value}, "
        else:
            query += f"'{value}', "

    query = query[:-2] + ")"

    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            connection.commit()

def worker_list():
    query = "SELECT * FROM WORKERS"

    data = []
    with connection:
        with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()

    return data