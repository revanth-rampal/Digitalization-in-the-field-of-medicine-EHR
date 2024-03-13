import tkinter as tk

class HostelManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Hostel Management System")

        self.create_building_layout()

    def create_building_layout(self):
        for floor in range(1, 5):
            for room in range(1, 113):
                room_key = f"{floor}_{room}"
                color = self.get_room_color(room_key)
                room_button = tk.Button(self.master, text=room_key, bg=color, width=5, height=2,
                                        command=lambda key=room_key: self.show_registration_page(key))
                row = (room - 1) // 16 * 2 + (floor - 1) * 4
                col = (room - 1) % 16
                if floor % 2 == 0:
                    col += 8  # Adding a gap in the middle for even floors
                room_button.grid(row=row, column=col)

    def show_registration_page(self, room_key):
        # Implementation for registration page goes here
        print(f"Registration for {room_key}")

    def get_room_color(self, room_key):
        # Implementation for determining room color goes here
        return "green"

if __name__ == "__main__":
    root = tk.Tk()
    app = HostelManagementSystem(root)
    root.mainloop()
