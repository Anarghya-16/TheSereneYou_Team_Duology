# app.py
from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3

app = Flask(__name__)

# --------- DATABASE SETUP ---------
conn = sqlite3.connect("app.db", check_same_thread=False)
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS diary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    created_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS meditation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_name TEXT,
    duration INTEGER,
    date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS journal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    content TEXT,
    created_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ai_companion (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    ai_response TEXT,
    created_at TEXT
)
""")
conn.commit()

# --------- ROUTES ---------

# --- Diary ---
@app.route("/diary", methods=["POST"])
def create_diary():
    data = request.json
    title = data.get("title")
    content = data.get("content")
    created_at = datetime.now().isoformat()
    cursor.execute("INSERT INTO diary (title, content, created_at) VALUES (?, ?, ?)",
                   (title, content, created_at))
    conn.commit()
    return jsonify({"message": "Diary entry created."})

@app.route("/diary", methods=["GET"])
def get_diary():
    cursor.execute("SELECT title, content FROM diary")
    rows = cursor.fetchall()
    result = [{"title": r[0], "content": r[1]} for r in rows]
    return jsonify(result)

# --- Meditation ---
@app.route("/meditation", methods=["POST"])
def add_meditation():
    data = request.json
    session_name = data.get("session_name")
    duration = data.get("duration")
    date = datetime.now().date().isoformat()
    cursor.execute("INSERT INTO meditation (session_name, duration, date) VALUES (?, ?, ?)",
                   (session_name, duration, date))
    conn.commit()
    return jsonify({"message": "Meditation session logged."})

@app.route("/meditation", methods=["GET"])
def get_meditation():
    cursor.execute("SELECT session_name, duration, date FROM meditation")
    rows = cursor.fetchall()
    result = [{"session_name": r[0], "duration": r[1], "date": r[2]} for r in rows]
    return jsonify(result)

# --- Journal ---
@app.route("/journal", methods=["POST"])
def add_journal():
    data = request.json
    topic = data.get("topic")
    content = data.get("content")
    created_at = datetime.now().isoformat()
    cursor.execute("INSERT INTO journal (topic, content, created_at) VALUES (?, ?, ?)",
                   (topic, content, created_at))
    conn.commit()
    return jsonify({"message": "Journal entry created."})

@app.route("/journal", methods=["GET"])
def get_journal():
    cursor.execute("SELECT topic, content FROM journal")
    rows = cursor.fetchall()
    result = [{"topic": r[0], "content": r[1]} for r in rows]
    return jsonify(result)

# --- AI Companion ---
@app.route("/ai", methods=["POST"])
def ai_chat():
    data = request.json
    user_message = data.get("user_message")
    # Simple echo AI for prototype. Replace with real AI integration if needed.
    ai_response = f"AI says: I hear you said '{user_message}'. How can I help further?"
    created_at = datetime.now().isoformat()
    cursor.execute("INSERT INTO ai_companion (user_message, ai_response, created_at) VALUES (?, ?, ?)",
                   (user_message, ai_response, created_at))
    conn.commit()
    return jsonify({"ai_response": ai_response})

@app.route("/ai", methods=["GET"])
def get_ai_history():
    cursor.execute("SELECT user_message, ai_response FROM ai_companion")
    rows = cursor.fetchall()
    result = [{"user_message": r[0], "ai_response": r[1]} for r in rows]
    return jsonify(result)

# --------- RUN APP ---------
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000',debug=True)
