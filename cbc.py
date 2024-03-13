import tkinter as tk

def submit_data():
    # Get values from the entry widgets
    id_value = entry_widgets[0].get()
    wbc_value = entry_widgets[1].get()
    rbc_value = entry_widgets[2].get()
    hb_value = entry_widgets[3].get()
    hct_value = entry_widgets[4].get()
    platelet_value = entry_widgets[5].get()
    mcv_value = entry_widgets[6].get()
    mch_value = entry_widgets[7].get()
    mchc_value = entry_widgets[8].get()
    rdw_value = entry_widgets[9].get()
    mpv_value = entry_widgets[10].get()

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

# Function to open the CBC Test window
def open_cbc_test_window():
    # Close the dashboard window
    dashboard_window.destroy()

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
    submit_button = tk.Button(cbc_test_window, text="Submit", command=submit_data)
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    # Run the Tkinter event loop for the CBC Test window
    cbc_test_window.mainloop()

# Create the main dashboard window
dashboard_window = tk.Tk()
dashboard_window.title("Dashboard")

# Create buttons for different tests
button_cbc_test = tk.Button(dashboard_window, text="CBC TEST", command=open_cbc_test_window)
button_cbc_test.pack(pady=20)

button_diabetics_test = tk.Button(dashboard_window, text="DIABETICS TEST")
button_diabetics_test.pack(pady=20)

# Run the Tkinter event loop for the dashboard window
dashboard_window.mainloop()
