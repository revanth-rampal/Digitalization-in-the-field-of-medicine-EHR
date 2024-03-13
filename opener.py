import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def open_main_file():
    subprocess.Popen(["python", "main.py"])

def open_drug_file():
    subprocess.Popen(["python", "drug.py"])

def open_app_file():
    subprocess.Popen(["python", "app.py"])

# Create the main window
root = tk.Tk()
root.title("Welcome to EHR")  # Set the title

# Headline Label
headline_label = tk.Label(root, text="Welcome to EHR", font=("Helvetica", 16, "bold"))
headline_label.pack(pady=10)

# Load and display the logo image
logo_image = Image.open("logo.png")  # Replace "logo.png" with the actual filename of your logo image
try:
    logo_image = logo_image.resize((150, 150), Image.ANTIALIAS)
except AttributeError:
    # For Pillow versions that don't have ANTIALIAS attribute
    logo_image = logo_image.resize((150, 150), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.NEAREST)

logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(root, image=logo_photo)
logo_label.image = logo_photo  # Keep a reference to the image to prevent garbage collection
logo_label.pack(pady=10)

# Create buttons
main_button = tk.Button(root, text="lab test", command=open_main_file)
main_button.pack(pady=5)

drug_button = tk.Button(root, text="drug details", command=open_drug_file)
drug_button.pack(pady=5)

app_button = tk.Button(root, text="patient details ", command=open_app_file)
app_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
