import tkinter as tk
from tkinter import messagebox

# Define entry_name, entry_email, entry_password in the global scope
entry_name = None
entry_email = None
entry_password = None

def open_registration_form():
    # Close the login window
    login_window.destroy()

    # Open the registration form window
    registration_form()

def authenticate_user():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password are correct
    if username == "user" and password == "password":
        messagebox.showinfo("Success", "Login successful!")
        open_registration_form()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def submit_registration_form():
    # Access the global entry_name, entry_email, entry_password
    global entry_name, entry_email, entry_password

    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()

    # You can perform validation and store data in a database here
    # For simplicity, just print a message
    print(f"Name: {name}\nEmail: {email}\nPassword: {password}")
    messagebox.showinfo("Success", "Registration successful!")

def registration_form():
    global entry_name, entry_email, entry_password

    # Create the registration window
    registration_window = tk.Tk()
    registration_window.title("Registration Form")

    # Create and place widgets in the registration window
    label_name = tk.Label(registration_window, text="Name:")
    label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entry_name = tk.Entry(registration_window)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    label_email = tk.Label(registration_window, text="Email:")
    label_email.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    entry_email = tk.Entry(registration_window)
    entry_email.grid(row=1, column=1, padx=10, pady=10)

    label_password = tk.Label(registration_window, text="Password:")
    label_password.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    entry_password = tk.Entry(registration_window, show="*")  # show="*" to hide the password
    entry_password.grid(row=2, column=1, padx=10, pady=10)

    submit_button = tk.Button(registration_window, text="Submit", command=submit_registration_form)
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Run the Tkinter event loop for the registration window
    registration_window.mainloop()

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

login_button = tk.Button(login_window, text="Login", command=authenticate_user)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop for the login window
login_window.mainloop()
