import tkinter as tk
from tkinter import messagebox
from utilities import Utilities
from tkinter import PhotoImage
from signup import SignupPage
from getBags import GetBags
from login import LoginPage
import pickle
import os

class LibraryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("600x400")  # Set the initial size of the window
        self.utilities = Utilities()
        self.get_bags_instance = GetBags()
        self.get_bags_instance.start()
        self.create_menu()  # Create the menu bar
        self.frame = None
        self.show_home_page()

    def create_menu(self):
        self.menubar = tk.Menu(self.master)
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.exit_app)
        self.menubar.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=self.menubar)

    def show_home_page(self):
        self.clear_frame()

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        tk.Label(self.frame, text="Welcome to the Library Management System").pack()

        tk.Button(self.frame, text="Log In", command=self.show_login_page).pack()
        tk.Button(self.frame, text="Sign Up", command=self.show_signup_page).pack()

    def show_login_page(self):
        self.clear_frame()
        LoginPage(self.master, self.show_signup_page, self.get_bags_instance, self.menubar)

    def show_signup_page(self):
        self.clear_frame()
        SignupPage(self.master, self.show_login_page, self.get_bags_instance, self.menubar)

    def clear_frame(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Menu):
                continue
            widget.destroy()

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.save_data_to_file()
            self.master.quit()

    def save_data_to_file(self):
        os.makedirs('database', exist_ok=True)
        with open(os.path.join('database', 'BookBag.dat'), 'wb') as book_file:
            pickle.dump(self.get_bags_instance.get_book_bag(), book_file)
        with open(os.path.join('database', 'ProfileBag.dat'), 'wb') as profile_file:
            pickle.dump(self.get_bags_instance.get_profile_bag(), profile_file)
        with open(os.path.join('database', 'AdminBag.dat'), 'wb') as admin_file:
            pickle.dump(self.get_bags_instance.get_admin_bag(), admin_file)

def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
