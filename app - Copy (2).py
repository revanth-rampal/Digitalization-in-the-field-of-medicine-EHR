import tkinter as tk
from tkinter import filedialog
import cv2
import face_recognition
from PIL import Image, ImageTk, ImageDraw
import os
import pickle

class FaceRecognitionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Face Recognition and Registration System")

        self.register_btn = tk.Button(master, text="Register Face", command=self.register_face_gui)
        self.register_btn.pack(pady=10)

        self.upload_btn = tk.Button(master, text="Recognize from File", command=self.recognize_face_from_file)
        self.upload_btn.pack(pady=10)

        self.capture_btn = tk.Button(master, text="Recognize from Webcam", command=self.recognize_face_from_webcam)
        self.capture_btn.pack(pady=10)

        # Initialize dictionaries to store registered faces and their details
        self.registered_faces = {}  # Key: face encoding, Value: details

        # Create a label to show the live webcam image
        self.live_image_label = tk.Label(master)
        self.live_image_label.pack()

        # Initialize the webcam capture
        self.cap = cv2.VideoCapture(0)
        self.update_webcam()

        # Load registered faces from file
        self.load_registered_faces()

    def register_face_gui(self):
        register_window = tk.Toplevel(self.master)
        register_window.title("Register Face")

        # Entry widgets for basic details
        name_label = tk.Label(register_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(register_window)
        name_entry.pack()

        age_label = tk.Label(register_window, text="Age:")
        age_label.pack()
        age_entry = tk.Entry(register_window)
        age_entry.pack()

        gender_label = tk.Label(register_window, text="Gender:")
        gender_label.pack()
        gender_entry = tk.Entry(register_window)
        gender_entry.pack()

        browse_btn = tk.Button(register_window, text="Select Image", command=lambda: self.register_face(register_window, name_entry.get(), age_entry.get(), gender_entry.get()))
        browse_btn.pack()

    def register_face(self, register_window, name, age, gender):
        file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            image = face_recognition.load_image_file(file_path)
            face_encoding = face_recognition.face_encodings(image)

            if face_encoding:
                # Add face encoding and details to the dictionary
                details = {'name': name, 'age': age, 'gender': gender, 'image_path': None}

                # Save the image to the "register" folder
                image_filename = f"{name}_{age}_{gender}.png"
                image_path = os.path.join("register", image_filename)
                cv2.imwrite(image_path, cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

                details['image_path'] = image_path
                self.registered_faces[tuple(face_encoding[0])] = details

                print("Face registered successfully!")
                register_window.destroy()  # Close the registration window

                # Save registered faces to file
                self.save_registered_faces()
            else:
                print("No face found in the selected image.")

    def recognize_face_from_file(self):
        file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg;*.png")])
        if file_path:
            image = face_recognition.load_image_file(file_path)
            self.recognize_face(image)

    def recognize_face_from_webcam(self):
        ret, frame = self.cap.read()

        if ret:
            self.recognize_face(frame)

    def recognize_face(self, image):
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        if not face_encodings:
            print("No face found in the selected image.")
            return

        recognized_details = []

        for unknown_face_encoding in face_encodings:
            # Compare the unknown face encoding with registered face encodings
            for registered_encoding, details in self.registered_faces.items():
                match = face_recognition.compare_faces([registered_encoding], unknown_face_encoding)[0]

                if match:
                    recognized_details.append(details)
                    break

        self.display_recognized_details(recognized_details)

    def display_recognized_details(self, details_list):
        details_window = tk.Toplevel(self.master)
        details_window.title("Recognized Details")

        # Clear the existing details frame
        for widget in details_window.winfo_children():
            widget.destroy()

        # Display recognized details in a tabular form
        if details_list:
            for details in details_list:
                details_label = tk.Label(details_window, text=f"Name: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}")
                details_label.pack()

                # Display the circular image in the details window
                self.display_circular_image(details_window, details['image_path'])

        else:
            no_details_label = tk.Label(details_window, text="No faces recognized.")
            no_details_label.pack()

    def display_circular_image(self, window, image_path):
        try:
            # Convert the image to PIL format
            pil_image = Image.open(image_path)

            # Resize the image to a smaller size
            pil_image = pil_image.resize((100, 100))

            # Create a circular mask
            mask = Image.new('L', pil_image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, pil_image.width, pil_image.height), fill=255)

            # Apply the circular mask
            circular_image = Image.new('RGB', pil_image.size)
            circular_image.paste(pil_image, mask=mask)

            # Convert the PIL image to PhotoImage format
            tk_image = ImageTk.PhotoImage(image=circular_image)

            # Display the circular image in a Label widget
            circular_label = tk.Label(window, image=tk_image)
            circular_label.image = tk_image  # Keep a reference to prevent garbage collection
            circular_label.pack()

        except Exception as e:
            print(f"Error displaying circular image: {e}")

    def update_webcam(self):
        try:
            ret, frame = self.cap.read()

            if ret:
                # Display the live webcam image
                self.display_live_image(frame)

            # Update the live image after 10 milliseconds
            self.master.after(10, self.update_webcam)

        except Exception as e:
            print(f"Error updating webcam: {e}")

    def display_live_image(self, frame):
        try:
            # Convert the OpenCV image to PIL format
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Resize the image to fit the label
            pil_image = pil_image.resize((400, 300))

            # Convert the PIL image to PhotoImage format
            tk_image = ImageTk.PhotoImage(image=pil_image)

            # Update the live image label with the latest frame
            self.live_image_label.config(image=tk_image)
            self.live_image_label.image = tk_image  # Keep a reference to prevent garbage collection

        except Exception as e:
            print(f"Error displaying webcam image: {e}")

    def save_registered_faces(self):
        try:
            with open('registered_faces.pkl', 'wb') as file:
                pickle.dump(self.registered_faces, file)
        except Exception as e:
            print(f"Error saving registered faces: {e}")

    def load_registered_faces(self):
        try:
            with open('registered_faces.pkl', 'rb') as file:
                self.registered_faces = pickle.load(file)
        except FileNotFoundError:
            print("No registered faces file found.")
        except Exception as e:
            print(f"Error loading registered faces: {e}")

def main():
    # Create the "register" folder if it doesn't exist
    register_folder = "register"
    if not os.path.exists(register_folder):
        os.makedirs(register_folder)

    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
