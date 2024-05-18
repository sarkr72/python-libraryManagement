from sortedcontainers import SortedDict
from collections import deque


class BookBag:
    def __init__(self):
        self.book_tree_map = SortedDict()
        self.book_map = SortedDict()
        self.n_elems = 0
        self.history_list = deque()
        self.history_map = SortedDict()

    def get_n_elems(self):
        return self.n_elems

    def get_history_list(self):
        return self.history_list

    def get_history_map(self):
        return self.history_map

    def get_book_map2(self):
        return self.book_map

    def insert(self, book):
        if book.isbn in self.book_tree_map:
            self.book_map[book.author.last_name] = book
        else:
            self.book_tree_map[book.isbn] = book

    def search_by_isbn(self, isbn):
        available = []
        if isbn in self.book_tree_map:
            book = self.book_tree_map[isbn]
            available.append(book)
            if book.author.last_name in self.book_map:
                available.append(book)
        return available

    def delete_by_isbn(self, isbn):
        available = []
        if isbn in self.book_tree_map:
            book = self.book_tree_map.pop(isbn)
            available.append(book)
            if book.author.last_name in self.book_map:
                available.append(self.book_map.pop(book.author.last_name))
        return available

    def search_by_last_name(self, last_name):
        books = []
        if last_name in self.book_map:
            book = self.book_map[last_name]
            books.append(book)
            if book.isbn in self.book_tree_map:
                books.append(self.book_tree_map[book.isbn])
        return books

    def delete_by_last_name(self, last_name):
        books = []
        if last_name in self.book_map:
            book = self.book_map.pop(last_name)
            books.append(book)
            if book.isbn in self.book_tree_map:
                books.append(self.book_tree_map.pop(book.isbn))
        return books

    def search_by_title(self, title):
        books = []
        for value in self.book_tree_map.items():
            if value.author.last_name == title:
                books.append(value)
        return books

    def delete_by_title(self, title):
        keys = []
        books = []
        for key, value in self.book_tree_map.items():
            if value.author.last_name == title:
                keys.append(key)
        for key in keys:
            books.append(self.book_tree_map.pop(key))
        return books

    def get_book_map(self):
        return self.book_tree_map
