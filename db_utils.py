# db_utils.py
import sqlite3
from typing import List

DB_PATH = "data.db"

def init_db(db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS paikkakunnat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def clear_locations(db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM paikkakunnat")
    conn.commit()
    conn.close()

def add_location(name: str, db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO paikkakunnat(name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_locations(db_path: str = DB_PATH) -> List[str]:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM paikkakunnat ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]