import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from functools import partial
from profileBag import ProfileBag
from profile import Profile
from book import Book
from author import Author
from getBags import GetBags
from bookBag import BookBag

class Dashboard:
    def __init__(self, master, get_bags_instance, username, menubar):
        self.master = master
        self.get_bags_instance = get_bags_instance
        self.username = username
        self.profile = self.get_bags_instance.get_profile_bag().search_profile_by_user_name(self.username)
        self.borrowed_list = self.profile.borrowed_history
        self.fee = 0.0
        self.book_bag = self.get_bags_instance.get_book_bag
        self.found_books_list = []
        self.isbn = ""
        self.last_name = ""
        self.title = ""
        self.menubar = menubar
        self.master.config(menu=self.menubar)
        # self.dic = GetBags.get_dic()

        self.create_dashboard()

    def create_dashboard(self):
        self.clear_frame()

        title_label = tk.Label(self.master, text="Dashboard")
        title_label.grid(row=0, column=1, pady=10)

        search_label = tk.Label(self.master, text="Search")
        search_label.grid(row=1, column=0)

        self.search_entry = tk.Entry(self.master)
        self.search_entry.grid(row=1, column=1)

        search_button = tk.Button(self.master, text="Search", command=self.search)
        search_button.grid(row=1, column=2)

        self.search_result_label = tk.Label(self.master, text="")
        self.search_result_label.grid(row=2, column=1)

        self.book_table = ttk.Treeview(self.master, columns=("Title", "ISBN", "First Name", "Last Name", "Date"))
        self.book_table.heading("#0", text="")
        self.book_table.heading("Title", text="Title")
        self.book_table.heading("ISBN", text="ISBN")
        self.book_table.heading("First Name", text="First Name")
        self.book_table.heading("Last Name", text="Last Name")
        self.book_table.heading("Date", text="Date")
        self.book_table.grid(row=3, column=0, columnspan=3)

        borrow_button = tk.Button(self.master, text="Borrow Book", command=self.borrow_book)
        borrow_button.grid(row=4, column=0)

        return_button = tk.Button(self.master, text="Return Book", command=self.return_book)
        return_button.grid(row=4, column=1)

        overdue_button = tk.Button(self.master, text="View Overdue Books", command=self.view_overdue_books)
        overdue_button.grid(row=4, column=2)

        profile_button = tk.Button(self.master, text="Open Profile", command=self.open_profile)
        profile_button.grid(row=5, column=0)

        home_button = tk.Button(self.master, text="Go to Home Page", command=self.go_to_home_page)
        home_button.grid(row=5, column=1)

        self.display_books()

    def search(self):
        search_text = self.search_entry.get().lower()
        self.found_books_list.clear()

        for book in self.book_bag.get_book_map().values():
            if (book.titles.lower().find(search_text) != -1) or \
                (book.author.first_name.lower().find(search_text) != -1) or \
                (book.author.last_name.lower().find(search_text) != -1) or \
                (book.isbn.lower().find(search_text) != -1):
                self.found_books_list.append(book)

        if not self.found_books_list:
            self.search_result_label.config(text="No matching books found")
        else:
            self.search_result_label.config(text=f"{len(self.found_books_list)} books found")
            self.display_books()

    def borrow_book(self):
        selected_book = self.book_table.selection()
        if not selected_book:
            messagebox.showerror("Error", "Please select a book to borrow")
            return

        book_index = int(selected_book[0][1:]) - 1
        book = self.found_books_list[book_index]

        if book.isbn in self.profile.current_borrowing:
            messagebox.showerror("Error", "You have already borrowed this book")
            return

        self.book_bag.delete_by_isbn(book.isbn)
        self.profile.add_borrowed_book(book)
        self.profile.current_borrowing[book.isbn] = book
        self.profile_bag.history_list.append(book)
        self.profile_bag.history_map[book.isbn] = book
        book.borrow_time = datetime.now().strftime("%H:%M:%S")
        book.return_time = (datetime.now() + timedelta(minutes=5)).strftime("%H:%M:%S")
        self.book_bag.history_map[book.isbn] = book
        self.book_bag.history_list.append(book)

        self.display_books()

    def return_book(self):
        selected_book = self.book_table.selection()
        if not selected_book:
            messagebox.showerror("Error", "Please select a book to return")
            return

        book_index = int(selected_book[0][1:]) - 1
        book = self.found_books_list[book_index]

        if book.isbn not in self.profile.current_borrowing:
            messagebox.showerror("Error", "You have not borrowed this book")
            return

        self.book_bag.insert(book)
        self.profile_bag.history_list.remove(book)
        del self.profile_bag.history_map[book.isbn]
        del self.profile.current_borrowing[book.isbn]
        book.return_time = f"returned\n{datetime.now().strftime('%H:%M:%S')}"

        self.display_books()

    def view_overdue_books(self):
        overdue_books = [book for book in self.profile_bag.history_list if "OverDue" in book.return_time]
        if not overdue_books:
            messagebox.showinfo("Info", "No overdue books found.")
            return

        self.found_books_list.clear()
        self.found_books_list.extend(overdue_books)
        self.display_books()

    def open_profile(self):
        # Implement opening profile functionality
        pass

    def go_to_home_page(self):
        # Implement going to home page functionality
        pass

    def display_books(self):
        self.book_table.delete(*self.book_table.get_children())

        for idx, book in enumerate(self.found_books_list, start=1):
            self.book_table.insert("", "end", values=(book.titles, book.isbn, book.author.first_name, book.author.last_name, book.borrow_time))

    def clear_frame(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Menu):
                continue
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
