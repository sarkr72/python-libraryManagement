from datetime import time
import pickle

class Book:
    def __init__(self, titles, isbn, author, price, borrow_time, return_time):
        self.titles = titles
        self.isbn = isbn
        self.author = author
        self.price = price
        self.borrow_time = borrow_time
        self.return_time = return_time

    def set_borrow_time(self, time):
        self.borrow_time = time

    def set_return_time(self, time):
        self.return_time = time

    def get_borrow_time(self):
        return self.borrow_time

    def get_return_time(self):
        return self.return_time

    def get_titles(self):
        return self.titles

    def set_titles(self, titles):
        self.titles = titles

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f"Book [titles={self.titles}, isbn={self.isbn}, author={self.author}, price={self.price}]"

    def __lt__(self, other):
        return self.isbn < other.isbn

    def serialize(self):
        return pickle.dumps(self)

    @staticmethod
    def deserialize(serialized_obj):
        return pickle.loads(serialized_obj)