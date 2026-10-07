import sqlite3
import os

# Windows error fix kosam wrapper
class ClosingConnection(sqlite3.Connection):
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.commit()
            else:
                self.rollback()
        finally:
            self.close()
        return False

class Database:
    def __init__(self, path="students.db"):
        self.path = path
        dir_name = os.path.dirname(self.path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)
        
        conn = sqlite3.connect(self.path)
        conn.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, course TEXT NOT NULL)")
        conn.commit()
        conn.close()

    def connect(self):
        # ee connection with lo nundi bayataki vachaka auto close avthundi
        return sqlite3.connect(self.path, factory=ClosingConnection)

    def get_connection(self):
        return sqlite3.connect(self.path, factory=ClosingConnection)