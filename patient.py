import tkinter as tk
from tkinter import messagebox
import sqlite3

def register_patient():
    def submit():
        name = entry_name.get()
        dob = entry_dob.get()
        contact = entry_contact.get()
        history = entry_history.get()
        
        if not name or not dob or not contact:
            messagebox.showwarning("Input Error", "All fields are required!")
            return
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute('''INSERT INTO patients (name, date_of_birth, contact_info, medical_history)
                     VALUES (?, ?, ?, ?)''', (name, dob, contact, history))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Patient Registered Successfully")
        register_window.destroy()

    register_window = tk.Toplevel()
    register_window.title("Register Patient")
    register_window.geometry("400x300")
    register_window.configure(bg="#e0f7fa")

    # Create registration form
    tk.Label(register_window, text="Name:", bg="#e0f7fa").grid(row=0, column=0, padx=10, pady=5)
    entry_name = tk.Entry(register_window)
    entry_name.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(register_window, text="Date of Birth:", bg="#e0f7fa").grid(row=1, column=0, padx=10, pady=5)
    entry_dob = tk.Entry(register_window)
    entry_dob.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(register_window, text="Contact Info:", bg="#e0f7fa").grid(row=2, column=0, padx=10, pady=5)
    entry_contact = tk.Entry(register_window)
    entry_contact.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(register_window, text="Medical History:", bg="#e0f7fa").grid(row=3, column=0, padx=10, pady=5)
    entry_history = tk.Entry(register_window)
    entry_history.grid(row=3, column=1, padx=10, pady=5)
    
    tk.Button(register_window, text="Submit", command=submit, bg="#007acc", fg="white").grid(row=4, column=1, padx=10, pady=10)
