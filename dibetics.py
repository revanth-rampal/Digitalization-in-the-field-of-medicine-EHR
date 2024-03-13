import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

class PatientRecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Record Management")

        # Initialize Firebase
        cred = credentials.Certificate("key/diabetes-f2cdc-firebase-adminsdk-tgd8n-6e46735b22.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        # Creating variables to store input values
        self.patient_id_var = tk.IntVar()  # Changed to IntVar for patient_id
        self.blood_sugar_var = tk.DoubleVar()

        # Creating labels and entry widgets
        ttk.Label(root, text="Patient ID:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Entry(root, textvariable=self.patient_id_var).grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        ttk.Label(root, text="Blood Sugar Level:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        ttk.Entry(root, textvariable=self.blood_sugar_var).grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Creating "Add Record" button
        ttk.Button(root, text="Add Record", command=self.add_record).grid(row=2, column=0, columnspan=2, pady=10)

    def add_record(self):
        # Get values from entry widgets
        patient_id = self.patient_id_var.get()
        blood_sugar_level = self.blood_sugar_var.get()

        # Validate input
        if not (patient_id and blood_sugar_level):
            messagebox.showwarning("Error", "Please fill in required fields.")
            return

        # Get current date and time as timestamp
        test_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Add record to Firebase
        self.db.collection('RBSTEST').add({
            'patient_id': patient_id,
            'blood_sugar_level': blood_sugar_level,
            'test_date': test_date
        })

        # Display submission message
        messagebox.showinfo("Submission", "Record submitted successfully.")

        # Clear input fields
        self.patient_id_var.set("")
        self.blood_sugar_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientRecordApp(root)
    root.mainloop()
