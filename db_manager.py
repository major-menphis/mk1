import sqlite3
import os

def create_database():
    if not os.path.exists("database.db"):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT)")
        conn.close()

def save_username(username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username) VALUES (?)", (username,))
    conn.commit()
    conn.close()

def get_username():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT username FROM users")
    username = c.fetchone()[0]
    conn.close()
    return username