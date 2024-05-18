from sortedcontainers import SortedDict

class Profile:
    def __init__(self, first_name, last_name, address, phone, town, zip_code, image, user_name, password, status,
                 borrowed_history):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.town = town
        self.zip = zip_code
        self.user_name = user_name
        self.password = password
        self.image = image
        self.borrowed_history = list(borrowed_history)
        self.current_borrowing = SortedDict()
        self.status = status
        self.book_counter = 0
        self.fee = 0.0
        self.borrow_date = 0.0
        self.return_date = 0

    def __str__(self):
        return f"Profile [name=, address={self.address}, phone={self.phone}, town={self.town}, zip={self.zip}, userName={self.user_name}, password={self.password}, image={self.image}, status={self.status}]"

    def __lt__(self, other):
        return self.user_name < other.user_name
