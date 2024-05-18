class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"firstName: {self.first_name}, lastName: {self.last_name}"