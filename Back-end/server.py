from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

def connect_db():
    return sqlite3.connect("database.db")

# Criar tabela
conn = connect_db()
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    message TEXT,
    created_at TEXT
)
""")
conn.commit()
conn.close()

# Enviar mensagem
@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    username = data["username"]
    message = data["message"]

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (username, message, created_at) VALUES (?, ?, ?)",
        (username, message, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )

    conn.commit()
    conn.close()

    return jsonify({"status": "ok"})

# Buscar mensagens
@app.route("/messages", methods=["GET"])
def get_messages():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT username, message, created_at FROM messages ORDER BY id ASC")
    messages = cursor.fetchall()

    conn.close()

    return jsonify([
        {"username": m[0], "message": m[1], "time": m[2]}
        for m in messages
    ])

if __name__ == "__main__":
    app.run(debug=True)