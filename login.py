import tkinter as tk
from tkinter import messagebox
from getBags import GetBags
from dashboard import Dashboard

class LoginPage:
    def __init__(self, master, go_to_signup, get_bags_instance, menubar):
        self.master = master
        self.go_to_signup = go_to_signup
        self.get_bags_instance = get_bags_instance
        self.menubar = menubar
        self.create_login_page()
        self.master.config(menu=self.menubar)

    def create_login_page(self):
        self.login_frame = tk.Frame(self.master)
        self.login_frame.grid(row=0, column=0)

        tk.Label(self.master, text="Login", font=("Helvetica", 16)).grid(row=0, column=1, pady=10)

        tk.Label(self.master, text="Username").grid(row=1, column=0)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Password").grid(row=2, column=0)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=2, column=1)

        tk.Button(self.master, text="Login", command=self.login).grid(row=3, column=1, pady=5)
        tk.Button(self.master, text="Sign Up", command=self.go_to_signup).grid(row=4, column=1, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not (username and password):
            messagebox.showerror("Error", "Please fill in all fields")
            return

        profile_bag = self.get_bags_instance.get_profile_bag()
        profile = profile_bag.search_profile_by_user_name(username)

        if profile:
            if profile.status != "Suspended":
                if profile.password != password:
                    messagebox.showerror("Error", "Password or Username did not match")
                else:
                    self.go_to_dashboard(username)
            else:
                messagebox.showerror("Error", "Your account is suspended")
        else:
            messagebox.showerror("Error", "You are not registered")


    def go_to_dashboard(self, username):
        self.clear_frame()
        Dashboard(self.master, self.get_bags_instance, username, self.menubar)

    def clear_frame(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Menu):
                continue
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    login_page = LoginPage(root, None)
    root.mainloop()
