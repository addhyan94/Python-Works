# app.py
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = "replace_with_a_strong_secret_key"  # change for production

DB = "edunova.db"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# ----------------- Database helpers -----------------
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    # users: both admin (teacher) and student
    c.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL, -- 'admin' or 'student'
        name TEXT,
        email TEXT UNIQUE,
        roll TEXT UNIQUE,
        password_hash TEXT,
        security_key TEXT,
        created_at TEXT
    )''')
    # students details & marks stored separately (student users + student_info)
    c.execute('''CREATE TABLE IF NOT EXISTS student_info(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        class TEXT,
        subjects TEXT, -- comma separated subject_codes
        attendance_count INTEGER DEFAULT 0,
        total_classes INTEGER DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    # subjects
    c.execute('''CREATE TABLE IF NOT EXISTS subjects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE,
        name TEXT
    )''')
    # marks table: stores sessional type ('S1' or 'S2') and marks as integer
    c.execute('''CREATE TABLE IF NOT EXISTS marks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_user_id INTEGER,
        subject_id INTEGER,
        sessional TEXT, -- 'S1' or 'S2'
        marks INTEGER,
        FOREIGN KEY(student_user_id) REFERENCES users(id),
        FOREIGN KEY(subject_id) REFERENCES subjects(id)
    )''')
    # attendance log: stores each attendance event per student with timestamp
    c.execute('''CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_user_id INTEGER,
        timestamp TEXT,
        present INTEGER DEFAULT 1,
        FOREIGN KEY(student_user_id) REFERENCES users(id)
    )''')
    conn.commit()
    conn.close()

def db_get(query, args=(), one=False):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

def db_execute(query, args=()):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    lastrowid = cur.lastrowid
    conn.close()
    return lastrowid

# ----------------- Flask-Login User -----------------
class User(UserMixin):
    def __init__(self, db_row):
        self.id = db_row["id"]
        self.name = db_row["name"]
        self.email = db_row["email"]
        self.role = db_row["role"]
        self.roll = db_row["roll"]

@login_manager.user_loader
def load_user(user_id):
    user_row = db_get("SELECT * FROM users WHERE id=?",(user_id,), one=True)
    if user_row:
        return User(user_row)
    return None

# ----------------- Seed admin -----------------
def seed_admin():
    admin = db_get("SELECT * FROM users WHERE role='admin' AND email=?",("admin@edunova.local",), one=True)
    if not admin:
        password_hash = generate_password_hash("admin123")
        db_execute("INSERT INTO users(role,name,email,roll,password_hash,security_key,created_at) VALUES(?,?,?,?,?,?,?)",
                   ("admin", "EduNova Admin", "admin@edunova.local", "ADMIN", password_hash, "edunova", datetime.utcnow().isoformat()))
seed_admin()

# ----------------- Routes -----------------
@app.route("/")
def welcome():
    # Loading animation controlled by frontend, ensure server responds quickly
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        role = request.form.get("role")
        email = request.form.get("email").strip()
        password = request.form.get("password")
        user = db_get("SELECT * FROM users WHERE email=? AND role=?", (email, role), one=True)
        if user and check_password_hash(user["password_hash"], password):
            user_obj = User(user)
            login_user(user_obj)
            flash("Logged in successfully", "success")
            if role=="admin":
                return redirect(url_for("admin_dashboard"))
            else:
                return redirect(url_for("student_dashboard"))
        flash("Invalid credentials", "danger")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("welcome"))

@app.route("/register_student", methods=["GET","POST"])
def register_student():
    # teachers can add students via admin panel normally; keep a public page too
    if request.method=="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        roll = request.form.get("roll")
        pwd = request.form.get("password")
        sec = request.form.get("security_key")
        role = "student"
        if not (name and email and roll and pwd and sec):
            flash("Fill all fields", "warning")
            return redirect(url_for("register_student"))
        ph = generate_password_hash(pwd)
        try:
            uid = db_execute("INSERT INTO users(role,name,email,roll,password_hash,security_key,created_at) VALUES(?,?,?,?,?,?,?)",
                             (role,name,email,roll,ph,sec,datetime.utcnow().isoformat()))
            db_execute("INSERT INTO student_info(user_id,class,subjects) VALUES(?,?,?)",(uid,"", ""))
            flash("Student registered", "success")
            return redirect(url_for("login"))
        except Exception as e:
            flash("Error or duplicate email/roll", "danger")
    return render_template("register_student.html")

@app.route("/forgot_password", methods=["GET
