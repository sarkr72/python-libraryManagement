import tkinter as tk
from tkinter import messagebox
from utilities import Utilities
from tkinter import PhotoImage
from signup import SignupPage

class LibraryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.utilities = Utilities()

        self.show_home_page()

    def show_home_page(self):
        self.clear_frame()

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Welcome to the Library Management System")
        self.label.pack()

        self.button1 = tk.Button(self.frame, text="Log In", command=self.show_login_page)
        self.button1.pack()

        self.button3 = tk.Button(self.frame, text="Sign Up", command=self.show_signup_page)
        self.button3.pack()

        self.button2 = tk.Button(self.frame, text="Exit", command=self.exit_app)
        self.button2.pack()

        

    def show_login_page(self):
        self.clear_frame()

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Login")
        self.label.pack()

        self.username_label = tk.Label(self.frame, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.frame, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        self.image = PhotoImage(file="default.png")
        self.image_label = tk.Label(self.frame, image=self.image)
        self.image_label.pack()

        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.pack()

        self.back_button = tk.Button(self.frame, text="Back", command=self.show_home_page)
        self.back_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Replace with actual authentication logic
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome to the Library Management System!")
            self.show_home_page()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()


    def show_signup_page(self):
        self.clear_frame()
        SignupPage(self.master, self.show_home_page)

def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
