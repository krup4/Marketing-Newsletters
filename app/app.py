from flask import Flask, request, jsonify
from db_queries.queries import init_db, add_worker, worker_list
from argon2 import PasswordHasher
from handle_jwt import encode_jwt

app = Flask(__name__)
hasher = PasswordHasher()
init_db()


@app.route('/api/ping', methods=['GET'])
def send():
    return jsonify({"status": "ok"}), 200


@app.route('/worker/reg', methods=['POST'])
def reg_worker():
    data = request.json
    data["password"] = encode_jwt(data.get("password"))
    add_worker(data)
    return jsonify({"status": "ok"})


@app.route('/worker/list', methods=['GET'])
def get_workers():
    return jsonify(worker_list()), 200


if __name__ == "__main__":
    app.run()
