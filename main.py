import tkinter as tk
from patient import register_patient
from appointment import schedule_appointment
from staff import manage_staff
from billing import manage_billing
from database import create_db

root = tk.Tk()
root.title("Hospital Management System")
root.geometry("800x600") 
root.configure(bg="#e0f7fa")  

tk.Label(root, text="Hospital Management System", font=("Arial", 20, "bold"), bg="#e0f7fa", fg="#007acc").pack(pady=20)

tk.Button(root, text="Register Patient", command=register_patient, bg="#007acc", fg="white", font=("Arial", 14), width=30).pack(pady=10)
tk.Button(root, text="Schedule Appointment", command=schedule_appointment, bg="#007acc", fg="white", font=("Arial", 14), width=30).pack(pady=10)
tk.Button(root, text="Manage Staff", command=manage_staff, bg="#007acc", fg="white", font=("Arial", 14), width=30).pack(pady=10)
tk.Button(root, text="Manage Billing", command=manage_billing, bg="#007acc", fg="white", font=("Arial", 14), width=30).pack(pady=10)

create_db()

root.mainloop()
