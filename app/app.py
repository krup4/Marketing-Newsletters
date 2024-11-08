from flask import Flask, request, jsonify

import os
import psycopg2

app = Flask(__name__)

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



@app.route('/api/ping', methods=['GET'])
def send():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run()