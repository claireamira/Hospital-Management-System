import tkinter as tk
from tkinter import messagebox
import sqlite3

def manage_staff():
    def add_staff():
        name = entry_name.get()
        role = entry_role.get()
        contact = entry_contact.get()
        
        if not name or not role or not contact:
            messagebox.showwarning("Input Error", "All fields are required!")
            return
        
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute('''INSERT INTO staff (name, role, contact_info)
                     VALUES (?, ?, ?)''', (name, role, contact))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Staff Added Successfully")
        staff_window.destroy()

    staff_window = tk.Toplevel()
    staff_window.title("Manage Staff")
    staff_window.geometry("400x300")
    staff_window.configure(bg="#e0f7fa")

    # Create staff form
    tk.Label(staff_window, text="Name:", bg="#e0f7fa").grid(row=0, column=0, padx=10, pady=5)
    entry_name = tk.Entry(staff_window)
    entry_name.grid(row=0, column=1, padx=10, pady=5)
    
    tk.Label(staff_window, text="Role:", bg="#e0f7fa").grid(row=1, column=0, padx=10, pady=5)
    entry_role = tk.Entry(staff_window)
    entry_role.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(staff_window, text="Contact Info:", bg="#e0f7fa").grid(row=2, column=0, padx=10, pady=5)
    entry_contact = tk.Entry(staff_window)
    entry_contact.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Button(staff_window, text="Submit", command=add_staff, bg="#007acc", fg="white").grid(row=3, column=1, padx=10, pady=10)
