import os
import pickle
from adminBag import AdminBag
from bookBag import BookBag
from profileBag import ProfileBag
from utilities import Utilities

class GetBags:
    def __init__(self):
        self.helper = Utilities()
        self.admin_bag = AdminBag()
        self.book_bag = None
        self.profile_bag = None
        self.dic = None
        self.admin_image = None

        try:
            self.book_bag = BookBag()
        except Exception as e:
            print("Error initializing book bag:", e)

    def start(self):
        try:
            # Load book bag
            book_bag_path = os.path.join('database', 'BookBag.dat')
            if os.path.exists(book_bag_path):
                with open(book_bag_path, "rb") as file:
                    self.book_bag = pickle.load(file)
                print("BookBag loaded successfully.")
            else:
                self.book_bag = self.helper.get_books(5000)
                print("BookBag created with default values.")

            # Load profile bag
            profile_bag_path = os.path.join('database', 'ProfileBag.dat')
            if os.path.exists(profile_bag_path):
                with open(profile_bag_path, "rb") as file:
                    self.profile_bag = pickle.load(file)
                print("ProfileBag loaded successfully:")
                self.print_profile_bag()
            else:
                self.profile_bag = self.helper.get_profile_bag()
                print("ProfileBag created with default values.")

            # Load admin bag
            admin_bag_path = os.path.join('database', 'AdminBag.dat')
            if os.path.exists(admin_bag_path):
                with open(admin_bag_path, "rb") as file:
                    self.admin_bag = pickle.load(file)
                print("AdminBag loaded successfully.")
        except Exception as e:
            print("Error loading bags:", e)

    def print_profile_bag(self):
        for profile in self.profile_bag.get_profile_map():
            print(f"Username: {profile.user_name}, First Name: {profile.first_name}, username: {profile.user_name}, ppp: {profile.password}")

    def get_book_bag(self):
        return self.book_bag

    def get_profile_bag(self):
        return self.profile_bag

    def get_admin_bag(self):
        return self.admin_bag


    # @staticmethod
    # def get_dic():
    #     return dic

# Example usage
if __name__ == "__main__":
    get_bags_instance = GetBags()
    get_bags_instance.start()
