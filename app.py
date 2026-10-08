from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from datetime import datetime, date

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "attendance.db")

app = Flask(__name__)
app.secret_key = "student_attendance_management_secret"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT NOT NULL UNIQUE,
            department TEXT NOT NULL,
            year TEXT NOT NULL,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            attendance_date TEXT NOT NULL,
            status TEXT NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(student_id, attendance_date),
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
        """
    )
    conn.commit()
    conn.close()


@app.route("/")
def index():
    today = date.today().strftime("%Y-%m-%d")
    conn = get_db_connection()
    total_students = conn.execute("SELECT COUNT(*) AS total FROM students").fetchone()["total"]
    present_today = conn.execute(
        "SELECT COUNT(*) AS total FROM attendance WHERE attendance_date = ? AND status = 'Present'",
        (today,),
    ).fetchone()["total"]
    absent_today = conn.execute(
        "SELECT COUNT(*) AS total FROM attendance WHERE attendance_date = ? AND status = 'Absent'",
        (today,),
    ).fetchone()["total"]
    late_today = conn.execute(
        "SELECT COUNT(*) AS total FROM attendance WHERE attendance_date = ? AND status = 'Late'",
        (today,),
    ).fetchone()["total"]
    recent_entries = conn.execute(
        """
        SELECT a.attendance_date, a.status, s.name, s.roll_no
        FROM attendance a
        JOIN students s ON s.id = a.student_id
        ORDER BY a.created_at DESC
        LIMIT 5
        """
    ).fetchall()
    conn.close()
    return render_template(
        "index.html",
        total_students=total_students,
        present_today=present_today,
        absent_today=absent_today,
        late_today=late_today,
        recent_entries=recent_entries,
    )


@app.route("/students", methods=["GET", "POST"])
def students():
    if request.method == "POST":
        name = request.form["name"].strip()
        roll_no = request.form["roll_no"].strip()
        department = request.form["department"].strip()
        year = request.form["year"].strip()
        phone = request.form.get("phone", "").strip()

        if not all([name, roll_no, department, year]):
            flash("Please fill in all required fields.", "danger")
            return redirect(url_for("students"))

        conn = get_db_connection()
        try:
            conn.execute(
                "INSERT INTO students (name, roll_no, department, year, phone) VALUES (?, ?, ?, ?, ?)",
                (name, roll_no, department, year, phone),
            )
            conn.commit()
            flash("Student added successfully.", "success")
        except sqlite3.IntegrityError:
            flash("A student with this roll number already exists.", "danger")
        finally:
            conn.close()

        return redirect(url_for("students"))

    conn = get_db_connection()
    student_list = conn.execute(
        "SELECT * FROM students ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return render_template("students.html", students=student_list)


@app.route("/attendance", methods=["GET", "POST"])
def attendance():
    selected_date = request.args.get("date") or date.today().strftime("%Y-%m-%d")

    if request.method == "POST":
        selected_date = request.form["attendance_date"]
        conn = get_db_connection()
        students = conn.execute("SELECT * FROM students ORDER BY name").fetchall()

        for student in students:
            status = request.form.get(f"status_{student['id']}", "Absent")
            notes = request.form.get(f"notes_{student['id']}", "")
            conn.execute(
                """
                INSERT INTO attendance (student_id, attendance_date, status, notes)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(student_id, attendance_date)
                DO UPDATE SET status = excluded.status, notes = excluded.notes
                """,
                (student["id"], selected_date, status, notes),
            )
        conn.commit()
        conn.close()
        flash("Attendance saved successfully.", "success")
        return redirect(url_for("attendance", date=selected_date))

    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students ORDER BY name").fetchall()
    saved_records = conn.execute(
        """
        SELECT a.student_id, a.status, a.notes
        FROM attendance a
        WHERE a.attendance_date = ?
        """,
        (selected_date,),
    ).fetchall()
    status_map = {record["student_id"]: record["status"] for record in saved_records}
    notes_map = {record["student_id"]: record["notes"] for record in saved_records}
    conn.close()

    return render_template(
        "attendance.html",
        students=students,
        selected_date=selected_date,
        status_map=status_map,
        notes_map=notes_map,
    )


@app.route("/reports")
def reports():
    conn = get_db_connection()
    report = conn.execute(
        """
        SELECT
            s.id,
            s.name,
            s.roll_no,
            s.department,
            s.year,
            COUNT(a.id) AS total_marked,
            SUM(CASE WHEN a.status = 'Present' THEN 1 ELSE 0 END) AS present_days,
            SUM(CASE WHEN a.status = 'Absent' THEN 1 ELSE 0 END) AS absent_days,
            SUM(CASE WHEN a.status = 'Late' THEN 1 ELSE 0 END) AS late_days
        FROM students s
        LEFT JOIN attendance a ON a.student_id = s.id
        GROUP BY s.id, s.name, s.roll_no, s.department, s.year
        ORDER BY s.name
        """
    ).fetchall()
    conn.close()
    return render_template("reports.html", report=report)


init_db()


if __name__ == "__main__":
    app.run(debug=True)
