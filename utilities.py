import random
import os
from author import Author
from book import Book
from myProfile import Profile
from profileBag import ProfileBag
from bookBag import BookBag

class Utilities:
    def __init__(self):
        self.author = self.emit_author(os.path.join("assets", "txtfiles", "First Names.txt"), os.path.join("assets", "txtfiles", "Last Names.txt"))
        self.bk_arr = self.make_books()

    def get_profile_bag(self):
        profile_bag = ProfileBag()
        for i in range(100):
            book_list = []
            phone = "".join(str(random.randint(0, 9)) for _ in range(10))
            zip_code = "".join(str(random.randint(0, 9)) for _ in range(5))
            street = str(random.randint(0, 999)) + self.author[i].last_name + " st"
            profile = Profile(self.author[i].first_name, self.author[i].last_name, street, phone, f"town{i}", zip_code, None, self.author[i].first_name.lower(), self.author[i].last_name, "Active", book_list)
            profile_bag.add_profile(profile)
        return profile_bag

    def get_books(self, n_elems):
        bag = BookBag()
        for _ in range(n_elems):
            rand = random.randint(0, len(self.bk_arr) - 1)
            bag.insert(self.bk_arr[rand])
        return bag

    def make_books(self):
        title_and_isbn = self.emit_title_and_isbn(os.path.join("assets", "txtfiles", "textbook_titles.txt"), os.path.join("assets", "txtfiles", "textbook_isbns.txt"), 5000)
        book_arr = []
        for title, isbn in title_and_isbn:
            book_arr.append(Book(title, isbn, self.get_random_author(self.author), self.emit_price(), None, None))
        return book_arr

    def emit_author(self, fname_file, lname_file):
        all_authors = []
        with open(fname_file, "r") as fname, open(lname_file, "r") as lname:
            for _ in range(110):
                first_name = fname.readline().strip()
                last_name = lname.readline().strip()
                all_authors.append(Author(first_name, last_name))
        return all_authors

    def get_random_author(self, names):
        return random.choice(names)

    def emit_title_and_isbn(self, title_file_name, isbn_file_name, n_elems):
        titles = []
        isbns = []
        with open(title_file_name, "r") as title_file, open(isbn_file_name, "r") as isbn_file:
            for _ in range(n_elems):
                titles.append(title_file.readline().strip())
                isbns.append(isbn_file.readline().strip())
        return list(zip(titles, isbns))

    def emit_price(self):
        rand = random.uniform(0, 500)
        return round(rand, 2)
