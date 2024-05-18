from collections import OrderedDict

class AdminBag:
    def __init__(self):
        self.admin_map = OrderedDict()
        self.n_elems = 0

    def insert_admin(self, admin):
        self.admin_map[admin.user_name] = admin

    def search_admin(self, user_name):
        return self.admin_map.get(user_name)

    def delete_admin(self, user_name):
        return self.admin_map.pop(user_name, None)

    def get_admin_map(self):
        return self.admin_map
