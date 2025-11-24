# db_utils.py
import sqlite3
from typing import List

DB_PATH = "data.db"

# Initialize the database and create the table if it doesn't exist
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

# Clear all locations from the database
def clear_locations(db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM paikkakunnat")
    conn.commit()
    conn.close()

# Add a new location to the database
def add_location(name: str, db_path: str = DB_PATH):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO paikkakunnat(name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

# Retrieve all locations from the database
def get_locations(db_path: str = DB_PATH) -> List[str]:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name FROM paikkakunnat ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]
