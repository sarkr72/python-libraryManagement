class Admin:
    def __init__(self, user_name, password, image):
        self.user_name = user_name
        self.password = password
        self.image = image

    def __str__(self):
        return f"Admin [userName={self.user_name}, password={self.password}, image={self.image}]"

    def __eq__(self, other):
        return self.user_name == other.user_name
