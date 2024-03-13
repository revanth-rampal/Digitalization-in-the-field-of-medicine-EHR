import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("key/diabetes-f2cdc-firebase-adminsdk-tgd8n-6e46735b22.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Global variable to store the username
current_user = ""

def submit_data(entry_widgets):
    try:
        # Get values from the entry widgets
        id_value = int(entry_widgets[0].get())
        wbc_value = int(entry_widgets[1].get())
        rbc_value = float(entry_widgets[2].get())
        hb_value = int(entry_widgets[3].get())
        hct_value = int(entry_widgets[4].get())
        platelet_value = int(entry_widgets[5].get())
        mcv_value = int(entry_widgets[6].get())
        mch_value = int(entry_widgets[7].get())
        mchc_value = int(entry_widgets[8].get())
        rdw_value = int(entry_widgets[9].get())
        mpv_value = int(entry_widgets[10].get())

        # Print or use the values as needed
        print("ID:", id_value)
        print("White Blood Cell Count (WBC):", wbc_value)
        print("Red Blood Cell Count (RBC):", rbc_value)
        print("Hemoglobin (Hb):", hb_value)
        print("Hematocrit (Hct):", hct_value)
        print("Platelet Count:", platelet_value)
        print("Mean Corpuscular Volume (MCV):", mcv_value)
        print("Mean Corpuscular Hemoglobin (MCH):", mch_value)
        print("Mean Corpuscular Hemoglobin Concentration (MCHC):", mchc_value)
        print("Red Cell Distribution Width (RDW):", rdw_value)
        print("Mean Platelet Volume (MPV):", mpv_value)

        # Upload data to Firebase
        submit_data_to_firebase({
            'ID': id_value,
            'WBC': wbc_value,
            'RBC': rbc_value,
            'Hb': hb_value,
            'Hct': hct_value,
            'Platelet': platelet_value,
            'MCV': mcv_value,
            'MCH': mch_value,
            'MCHC': mchc_value,
            'RDW': rdw_value,
            'MPV': mpv_value,
        })

        # Show submitted message
        messagebox.showinfo("Submitted", "Data submitted successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

def submit_data_to_firebase(data):
    # Add a new document with auto-generated ID to the "CBCDATA" collection
    doc_ref, doc_id = db.collection('CBCDATA').add(data)
    print(f'Data submitted to Firebase with ID: {doc_id}')

# Function to open the CBC Test window
def open_cbc_test_window(login_window):
    # Close the login window
    login_window.destroy()

    # Create the CBC Test window
    cbc_test_window = tk.Tk()
    cbc_test_window.title("CBC Test")

    # Create labels and entry widgets for each parameter
    labels = ["ID", "White Blood Cell Count (WBC)", "Red Blood Cell Count (RBC)",
              "Hemoglobin (Hb)", "Hematocrit (Hct)", "Platelet Count",
              "Mean Corpuscular Volume (MCV)", "Mean Corpuscular Hemoglobin (MCH)",
              "Mean Corpuscular Hemoglobin Concentration (MCHC)",
              "Red Cell Distribution Width (RDW)", "Mean Platelet Volume (MPV)"]

    # Create a list to store entry widgets
    entry_widgets = []

    for i, label_text in enumerate(labels):
        label = tk.Label(cbc_test_window, text=label_text)
        label.grid(row=i, column=0, sticky="e", pady=5, padx=10)

        entry = tk.Entry(cbc_test_window)
        entry.grid(row=i, column=1, pady=5, padx=10)

        # Append the entry widget to the list
        entry_widgets.append(entry)

    # Create the submit button
    submit_button = tk.Button(cbc_test_window, text="Submit", command=lambda: submit_data(entry_widgets))
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    # Run the Tkinter event loop for the CBC Test window
    cbc_test_window.mainloop()

def authenticate_user(entry_username, entry_password, login_window):
    global current_user
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password are correct
    if username == "user" and password == "password":
        messagebox.showinfo("Success", "Login successful!")
        current_user = username
        open_dashboard(login_window)
    else:
        messagebox.showerror("Error", "Invalid username or password")

def open_dashboard(login_window):
    # Close the login window
    login_window.destroy()

    # Create the main dashboard window
    dashboard_window = tk.Tk()
    dashboard_window.title("Dashboard")

    # Create buttons for different tests
    button_cbc_test = tk.Button(dashboard_window, text="CBC TEST", command=lambda: open_cbc_test_window(dashboard_window))
    button_cbc_test.pack(pady=20)

    button_diabetics_test = tk.Button(dashboard_window, text="DIABETICS TEST", command=lambda: open_cbc_test_window(dashboard_window))
    button_diabetics_test.pack(pady=20)

    # Run the Tkinter event loop for the dashboard window
    dashboard_window.mainloop()

# Create the main login window
login_window = tk.Tk()
login_window.title("Login")

# Create and place widgets in the login window
label_username = tk.Label(login_window, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_username = tk.Entry(login_window)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(login_window, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_password = tk.Entry(login_window, show="*")  # show="*" to hide the password
entry_password.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(login_window, text="Login", command=lambda: authenticate_user(entry_username, entry_password, login_window))
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop for the login window
login_window.mainloop()
