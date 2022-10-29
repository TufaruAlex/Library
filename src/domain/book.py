class Book:
    def __init__(self, book_id, title, author, is_rented=False):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__is_rented = is_rented
        self.__number_of_rentals = 0

    @property
    def get_book_id(self):
        return self.__book_id

    def set_book_id(self, new_book_id):
        self.__book_id = new_book_id

    @property
    def get_title(self):
        return self.__title

    def set_title(self, new_title):
        self.__title = new_title

    @property
    def get_author(self):
        return self.__author

    def set_author(self, new_author):
        self.__author = new_author

    @property
    def get_rental_state(self):
        return self.__is_rented

    def set_rental_state(self, new_rental_state):
        self.__is_rented = new_rental_state

    def update_number_of_rentals(self):
        self.__number_of_rentals += 1

    @property
    def get_number_of_rentals(self):
        return self.__number_of_rentals

    def __str__(self):
        return "ID: " + str(self.__book_id) + ", title: " + self.__title + ", author: " + self.__author + ", rental " \
               "state: " + str(self.__is_rented) + ", " + str(self.__number_of_rentals) + " rentals"

    def __eq__(self, other):
        return self.__book_id == other.__book_id and self.__title == other.__title and self.__author == \
               other.__author and self.__is_rented == other.__is_rented
