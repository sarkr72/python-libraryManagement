from sortedcontainers import SortedDict
from profile import Profile

class ProfileBag:
    def __init__(self):
        self.profile_map = {}
        self.n_elems = 0
        self.history_list = []
        self.history_map = SortedDict()

    def add_profile(self, profile):
        self.profile_map[profile.user_name] = profile
        self.n_elems += 1

    def search_profile_by_user_name(self, username):
        return self.profile_map.get(username)

    def delete_profile_by_user_name(self, username):
        return self.profile_map.pop(username, None)

    def get_history_list(self):
        return self.history_list

    def get_history_map(self):
        return self.history_map

    def get_profile_map(self):
        return self.profile_map
