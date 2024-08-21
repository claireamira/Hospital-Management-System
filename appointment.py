import tkinter as tk
from tkinter import messagebox
import sqlite3

def schedule_appointment():
    def submit():
        patient_id = entry_patient_id.get()
        doctor_id = entry_doctor_id.get()
        date = entry_date.get()
        time = entry_time.get()
        status = entry_status.get()
        
        if not patient_id or not doctor_id or not date or not time:
            messagebox.showwarning("Input Error", "All fields are required!")
            return
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute('''INSERT INTO appointments (patient_id, doctor_id, date, time, status)
                     VALUES (?, ?, ?, ?, ?)''', (patient_id, doctor_id, date, time, status))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Appointment Scheduled Successfully")
        appointment_window.destroy()

    appointment_window = tk.Toplevel()
    appointment_window.title("Schedule Appointment")
    appointment_window.geometry("400x300")
    appointment_window.configure(bg="#e0f7fa")

    # Create appointment form
    tk.Label(appointment_window, text="Patient ID:", bg="#e0f7fa").grid(row=0, column=0, padx=10, pady=5)
    entry_patient_id = tk.Entry(appointment_window)
    entry_patient_id.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(appointment_window, text="Doctor ID:", bg="#e0f7fa").grid(row=1, column=0, padx=10, pady=5)
    entry_doctor_id = tk.Entry(appointment_window)
    entry_doctor_id.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(appointment_window, text="Date (YYYY-MM-DD):", bg="#e0f7fa").grid(row=2, column=0, padx=10, pady=5)
    entry_date = tk.Entry(appointment_window)
    entry_date.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(appointment_window, text="Time (HH:MM):", bg="#e0f7fa").grid(row=3, column=0, padx=10, pady=5)
    entry_time = tk.Entry(appointment_window)
    entry_time.grid(row=3, column=1, padx=10, pady=5)
    
    tk.Label(appointment_window, text="Status:", bg="#e0f7fa").grid(row=4, column=0, padx=10, pady=5)
    entry_status = tk.Entry(appointment_window)
    entry_status.grid(row=4, column=1, padx=10, pady=5)
    
    tk.Button(appointment_window, text="Submit", command=submit, bg="#007acc", fg="white").grid(row=5, column=1, padx=10, pady=10)
