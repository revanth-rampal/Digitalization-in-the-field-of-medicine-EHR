import tkinter as tk
from tkinter import messagebox
import requests

def get_drug_info():
    drug_name = entry.get()
    
    # Define the API endpoint
    api_url = "https://rxnav.nlm.nih.gov/REST/drugs.json"

    # Set up the parameters
    params = {"name": drug_name}

    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract and display relevant information
        display_info(data)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")

def display_info(data):
    # Extract relevant information from the API response and display it
    drug_group = data.get("drugGroup", {})
    concept_groups = drug_group.get("conceptGroup", [])

    if not concept_groups:
        messagebox.showinfo("Result", "No information found for the specified drug.")
        return

    result_text = "Results:\n\n"

    for concept_group in concept_groups:
        tty = concept_group.get("tty")
        concept_properties = concept_group.get("conceptProperties", [])

        result_text += f"Term Type: {tty}\n"

        for concept in concept_properties:
            rxcui = concept.get("rxcui")
            name = concept.get("name")
            synonym = concept.get("synonym")

            result_text += f"  - RxNorm ID: {rxcui}\n"
            result_text += f"  - Concept Name: {name}\n"
            result_text += f"  - Synonym: {synonym}\n\n"

    # Display the information in a new window
    result_window = tk.Toplevel(app)
    result_window.title("Drug Information")
    
    result_label = tk.Label(result_window, text=result_text)
    result_label.pack(padx=10, pady=10)

# Create the main application window
app = tk.Tk()
app.title("Drug Information Lookup")

# Create GUI components
label = tk.Label(app, text="Enter Drug Name:")
entry = tk.Entry(app)
button = tk.Button(app, text="Get Information", command=get_drug_info)

# Place components in the window
label.pack(pady=10)
entry.pack(pady=10)
button.pack(pady=10)

# Start the application
app.mainloop()
