from io import BytesIO
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json
from myProfile import Profile
from getBags import GetBags
from profileBag import ProfileBag
from utilities import Utilities

class SignupPage:
    def __init__(self, master, go_home, get_bags_instance, menubar):
        self.master = master
        self.go_home = go_home
        self.image = None
        self.get_bags_instance = get_bags_instance
        self.create_signup_page()
        self.menubar = menubar
        self.master.config(menu=self.menubar)

    def create_signup_page(self):
        self.login_frame = tk.Frame(self.master)
        self.login_frame.grid(row=0, column=0)

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

        tk.Label(self.master, text="Town").grid(row=4, column=0)
        self.town_entry = tk.Entry(self.master)
        self.town_entry.grid(row=4, column=1)

        tk.Label(self.master, text="ZIP Code").grid(row=5, column=0)
        self.zip_entry = tk.Entry(self.master)
        self.zip_entry.grid(row=5, column=1)

        tk.Label(self.master, text="Username").grid(row=6, column=0)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=6, column=1)

        tk.Label(self.master, text="Password").grid(row=7, column=0)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=7, column=1)

        tk.Label(self.master, text="Phone").grid(row=8, column=0)
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=8, column=1)

        self.image_label = tk.Label(self.master, text="No Image")
        self.image_label.grid(row=9, column=1, pady=10)
        
        tk.Button(self.master, text="Add Image", command=self.add_image).grid(row=10, column=0, pady=5)
        tk.Button(self.master, text="Sign Up", command=self.apply_for_card).grid(row=10, column=1, pady=5)
        tk.Button(self.master, text="Back to Home", command=self.go_home).grid(row=11, column=1, pady=10)

    def add_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.convert("RGB")
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
        
        image_data = None
        if self.image:
            with BytesIO() as img_buffer:
                self.image.save(img_buffer, format="JPEG")
                image_data = img_buffer.getvalue()     

        borrowed_books = []
        profile = Profile(first_name, last_name, address, phone, town, zip_code, image_data, username, password, "Active", borrowed_books)

        profile_bag = self.get_bags_instance.get_profile_bag()
        profile_bag.add_profile(profile)
        print(f"First Name: {profile.first_name}, Last Name: {profile.last_name}, Username: {profile.user_name}, last: {profile.borrowed_history}.")

        messagebox.showinfo("Success", "Sign up successful!")
        self.clear_frame()
        self.go_home()

    def clear_frame(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Menu):
                continue
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SignupPage(root, None)
    root.mainloop()
