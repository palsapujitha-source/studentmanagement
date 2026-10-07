import sqlite3

class StudentService:
    def __init__(self, db):
        self.db = db

    def add_student(self, sid, name, age, course):
        if not name or str(name).strip() == "":
            raise ValueError("Name cannot be empty")
        if int(age) < 18:
            raise ValueError("Age must be 18+")
        
        conn = self.db.get_connection()
        try:
            conn.execute("INSERT INTO students VALUES (?,?,?,?)", (sid, name.strip(), age, course))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            raise Exception("Duplicate ID")
        finally:
            conn.close()

    def get_student(self, sid):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE id=?", (sid,))
        row = cur.fetchone()
        conn.close()
        return row

    def get_all_students(self):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        conn.close()
        return rows

    def update_student(self, sid, name, age, course):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", (name, age, course, sid))
        conn.commit()
        count = cur.rowcount
        conn.close()
        return count > 0

    def delete_student(self, sid):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE id=?", (sid,))
        conn.commit()
        count = cur.rowcount
        conn.close()
        return count > 0
     