import tkinter as tk
from tkinter import messagebox
import sqlite3

def manage_billing():
    def submit():
        patient_id = entry_patient_id.get()
        amount = entry_amount.get()
        date = entry_date.get()
        status = entry_status.get()
        
        if not patient_id or not amount or not date or not status:
            messagebox.showwarning("Input Error", "All fields are required!")
            return
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute('''INSERT INTO billing (patient_id, amount, date, status)
                     VALUES (?, ?, ?, ?)''', (patient_id, amount, date, status))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Billing Info Added Successfully")
        billing_window.destroy()

    billing_window = tk.Toplevel()
    billing_window.title("Manage Billing")
    billing_window.geometry("400x300")
    billing_window.configure(bg="#e0f7fa")

    # Create billing form
    tk.Label(billing_window, text="Patient ID:", bg="#e0f7fa").grid(row=0, column=0, padx=10, pady=5)
    entry_patient_id = tk.Entry(billing_window)
    entry_patient_id.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(billing_window, text="Amount:", bg="#e0f7fa").grid(row=1, column=0, padx=10, pady=5)
    entry_amount = tk.Entry(billing_window)
    entry_amount.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(billing_window, text="Date (YYYY-MM-DD):", bg="#e0f7fa").grid(row=2, column=0, padx=10, pady=5)
    entry_date = tk.Entry(billing_window)
    entry_date.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(billing_window, text="Status:", bg="#e0f7fa").grid(row=3, column=0, padx=10, pady=5)
    entry_status = tk.Entry(billing_window)
    entry_status.grid(row=3, column=1, padx=10, pady=5)
    
    tk.Button(billing_window, text="Submit", command=submit, bg="#007acc", fg="white").grid(row=4, column=1, padx=10, pady=10)
