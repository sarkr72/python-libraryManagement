import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json

class SignupPage:
    def __init__(self, master, go_home):
        self.master = master
        self.go_home = go_home
        self.image = None
        self.create_signup_page()

    def create_signup_page(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(self.master, text="Sign Up").grid(row=0, column=1, pady=10)

        tk.Label(self.master, text="First Name").grid(row=1, column=0)
        self.first_name_entry = tk.Entry(self.master)
        self.first_name_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Last Name").grid(row=2, column=0)
        self.last_name_entry = tk.Entry(self.master)
        self.last_name_entry.grid(row=2, column=1)

        tk.Label(self.master, text="Address").grid(row=3, column=0)
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=3, column=1)

        tk.Label(self.master, text="Town").grid(row=5, column=0)
        self.town_entry = tk.Entry(self.master)
        self.town_entry.grid(row=5, column=1)

        tk.Label(self.master, text="ZIP Code").grid(row=6, column=0)
        self.zip_entry = tk.Entry(self.master)
        self.zip_entry.grid(row=6, column=1)

        tk.Label(self.master, text="Phone").grid(row=4, column=0)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=4, column=1)

        tk.Label(self.master, text="Username").grid(row=7, column=0)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=7, column=1)

        tk.Label(self.master, text="Password").grid(row=8, column=0)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=8, column=1)

        self.image_label = tk.Label(self.master, text="No Image")
        self.image_label.grid(row=9, column=1, pady=10)
        
        tk.Button(self.master, text="Add Image", command=self.add_image).grid(row=10, column=0, pady=5)
        tk.Button(self.master, text="Sign Up", command=self.apply_for_card).grid(row=10, column=1, pady=5)
        tk.Button(self.master, text="Back to Home", command=self.go_home).grid(row=11, column=1, pady=10)

    def add_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.image.thumbnail((150, 150))
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo, text="")



    def apply_for_card(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        town = self.town_entry.get()
        zip_code = self.zip_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not (first_name and last_name and address and phone and town and zip_code and username and password):
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        # Save the data to a file
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "phone": phone,
            "town": town,
            "zip_code": zip_code,
            "username": username,
            "password": password
        }
        
        try:
            with open("user_data.json", "a") as file:
                file.write(json.dumps(user_data) + "\n")
            messagebox.showinfo("Success", "Sign up successful!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")
            return

        # After successful sign-up, go back to home page
        self.go_home()


if __name__ == "__main__":
    root = tk.Tk()
    app = SignupPage(root, None)
    root.mainloop()
