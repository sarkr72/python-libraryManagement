import tkinter as tk
from tkinter import ttk

class ProfileApp:
    def __init__(self, master, profile, back_callback):
        self.master = master
        self.profile = profile
        self.back_callback = back_callback
        self.master.title("Profile")

        self.main_frame = ttk.Frame(master)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.add_label_and_text("First Name:", self.profile.first_name, row=0)
        self.add_label_and_text("Last Name:", self.profile.last_name, row=1)
        self.add_label_and_text("Username:", self.profile.user_name, row=2)
        self.add_label_and_text("Password:", self.profile.password, row=3)
        self.add_label_and_text("Address:", self.profile.address, row=4)
        self.add_label_and_text("Phone number:", self.profile.phone, row=5)

        self.back_button = ttk.Button(self.main_frame, text="Back", command=self.back)
        self.back_button.grid(row=6, column=0, pady=10)

    def add_label_and_text(self, label_text, text, row):
        label = ttk.Label(self.main_frame, text=label_text)
        label.grid(row=row, column=0, padx=5, pady=5, sticky="e")
        text_field = ttk.Label(self.main_frame, text=text, wraplength=400)
        text_field.grid(row=row, column=1, padx=5, pady=5, sticky="w")

    def back(self):
        self.main_frame.grid_remove()

        if self.back_callback:
            self.back_callback()

    def clear_frame(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Menu):
                continue
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    profile_app = ProfileApp(root)
    root.mainloop()
