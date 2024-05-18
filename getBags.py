import pickle
import random
from author import Author
from book_bag import BookBag
from collections import deque
from sortedcontainers import SortedDict
from admin_bag import AdminBag
from profile_bag import ProfileBag
from utilities import Utilities


class GetBags:
    def __init__(self):
        self.helper = Utilities()
        self.admin_bag = AdminBag()
        self.book_bag = BookBag()
        self.profile_bag = ProfileBag()
        self.dic = None
        self.admin_username = "admin"
        self.admin_image = None

    def start(self):
        if self.dic is None:
            self.dic = self.helper.get_dictionary()
        try:
            with open("BookBag.pkl", "rb") as file:
                self.book_bag = pickle.load(file)
        except FileNotFoundError:
            self.book_bag = self.helper.get_books(5000)
        try:
            with open("ProfileBag.pkl", "rb") as file:
                self.profile_bag = pickle.load(file)
        except FileNotFoundError:
            self.profile_bag = self.helper.get_profile_bag()
        try:
            with open("AdminBag.pkl", "rb") as file:
                self.admin_bag = pickle.load(file)
        except FileNotFoundError:
            pass

    def get_book_bag(self):
        return self.book_bag

    def get_profile_bag(self):
        return self.profile_bag

    def get_admin_bag(self):
        return self.admin_bag

    def get_dic(self):
        return self.dic
