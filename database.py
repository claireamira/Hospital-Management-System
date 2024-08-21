import sqlite3

def create_db():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    
    # Create tables if they don't exist
    c.execute('''CREATE TABLE IF NOT EXISTS patients (
                   patient_id INTEGER PRIMARY KEY,
                   name TEXT,
                   date_of_birth TEXT,
                   contact_info TEXT,
                   medical_history TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS doctors (
                   doctor_id INTEGER PRIMARY KEY,
                   name TEXT,
                   specialization TEXT,
                   contact_info TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS appointments (
                   appointment_id INTEGER PRIMARY KEY,
                   patient_id INTEGER,
                   doctor_id INTEGER,
                   date TEXT,
                   time TEXT,
                   status TEXT,
                   FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
                   FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id))''')

    c.execute('''CREATE TABLE IF NOT EXISTS staff (
                   staff_id INTEGER PRIMARY KEY,
                   name TEXT,
                   role TEXT,
                   contact_info TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS billing (
                   bill_id INTEGER PRIMARY KEY,
                   patient_id INTEGER,
                   amount REAL,
                   date TEXT,
                   status TEXT,
                   FOREIGN KEY(patient_id) REFERENCES patients(patient_id))''')

    conn.commit()
    conn.close()
