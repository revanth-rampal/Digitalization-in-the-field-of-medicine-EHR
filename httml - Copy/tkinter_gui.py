import tkinter as tk
from tkinter import filedialog
import requests

def update_profile():
    # Get values from entry widgets
    name_value = name_entry.get()
    age_value = age_entry.get()
    email_value = email_entry.get()
    phone_value = phone_entry.get()
    address_value = address_entry.get()
    dob_value = dob_entry.get()
    insurance_status_value = insurance_status_entry.get()

    # Upload the image to the Flask server
    files = {'file': open(image_path, 'rb')}
    image_response = requests.post('http://127.0.0.1:5000/upload_image', files=files)

    # Create a payload with other details
    payload = {
        'name': name_value,
        'age': age_value,
        'email': email_value,
        'phone': phone_value,
        'address': address_value,
        'dob': dob_value,
        'insurance_status': insurance_status_value
    }

    # Send the payload to the Flask server
    response = requests.post('http://127.0.0.1:5000/update_profile', data=payload)
    print(response.text)

# Function to handle image upload
def upload_image():
    global image_path
    image_path = filedialog.askopenfilename()

# Create the main window
app = tk.Tk()
app.title("Profile Details")

# Create entry widgets
name_entry = tk.Entry(app)
age_entry = tk.Entry(app)
email_entry = tk.Entry(app)
phone_entry = tk.Entry(app)
address_entry = tk.Entry(app)
dob_entry = tk.Entry(app)
insurance_status_entry = tk.Entry(app)

# Create a button to update profile
update_button = tk.Button(app, text="Update Profile", command=update_profile)

# Create a button to upload image
upload_button = tk.Button(app, text="Upload Image", command=upload_image)

# Arrange widgets using the grid layout
name_entry.grid(row=0, column=1)
age_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
phone_entry.grid(row=3, column=1)
address_entry.grid(row=4, column=1)
dob_entry.grid(row=5, column=1)
insurance_status_entry.grid(row=6, column=1)

update_button.grid(row=7, column=1)
upload_button.grid(row=7, column=2)

# Start the Tkinter event loop
app.mainloop()
