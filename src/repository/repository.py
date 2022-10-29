from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from random import randint
from datetime import date

BOOK_LIST = {
    "title": ["Watchmen", "Batman: Year One", "Journey to the Center of the World", "Twenty Thousand Leagues Under "
                                                                                    "the Seas",
              "Are You Smart Enough to Work at Google?", "The Silver Eyes", "Kenobi", "The Art of War",
              "Dune", "Sans Famille"],
    "author": ["Alan Moore", "Frank Miller", "Jules Verne", "Jules Verne", "William Poundstone", "Scott Cawthon, "
                                                                                                 "Kira Breed-Wrisley",
               "John Jackson Miller", "Sun Tzu", "Frank Herbert", "Hector Malot"]
}

CLIENTS_LIST = ["Bruce Wayne", "Theresa Roberts", "Steven Hawkings", "Philip Screw", "Stan Lee",
                "Carl Stewart", "Dwight Schrute", "Maria Perry", "Andrew Garfield", "Amanda Waller"]


class RepositoryException(Exception):
    def __init__(self, message):
        self.__message = message

    @property
    def get_error_message(self):
        return self.__message

    def __str__(self):
        return self.__message


class BookRepository:
    def __init__(self):
        self._books_list = generate_books()

    @property
    def get_books_list(self):
        return self._books_list

    def add_book(self, book_to_add):
        validate_book_id(book_to_add.get_book_id, self._books_list)
        self._books_list[book_to_add.get_book_id] = book_to_add

    def remove_book(self, book_to_remove_id):
        del self._books_list[book_to_remove_id]

    def update_book(self, book_id_to_update, new_book_id, new_title, new_author):
        validate_book_id(new_book_id, self._books_list)
        self._books_list[book_id_to_update].set_book_id(new_book_id)
        self._books_list[book_id_to_update].set_title(new_title)
        self._books_list[book_id_to_update].set_author(new_author)
        self._books_list[new_book_id] = self._books_list[book_id_to_update]
        del self._books_list[book_id_to_update]

    def set_rental_state(self, book_id, new_rental_state):
        self._books_list[book_id].set_rental_state(new_rental_state)

    def get_rental_state(self, book_id):
        return self._books_list[book_id].get_rental_state

    def find_book(self, book_id_to_find):
        if book_id_to_find in self._books_list.keys():
            return True
        else:
            raise RepositoryException("This is not the book you're looking for")


class ClientRepository:
    def __init__(self):
        self._clients_list = generate_clients()

    @property
    def get_clients_list(self):
        return self._clients_list

    def add_client(self, client_to_add):
        validate_client_id(client_to_add.get_client_id, self._clients_list)
        self._clients_list[client_to_add.get_client_id] = client_to_add

    def remove_client(self, client_to_remove_id):
        del self._clients_list[client_to_remove_id]

    def update_client(self, client_id_to_update, new_client_id, new_name):
        validate_client_id(new_client_id, self._clients_list)
        self._clients_list[client_id_to_update].set_client_id(new_client_id)
        self._clients_list[client_id_to_update].set_client_name(new_name)
        self._clients_list[new_client_id] = self._clients_list[client_id_to_update]
        del self._clients_list[client_id_to_update]

    def find_client(self, client_id_to_find):
        if client_id_to_find in self._clients_list.keys():
            return True
        else:
            raise RepositoryException("This is not the client you're looking for")


class RentalRepository:
    def __init__(self):
        self._rentals_list = generate_rentals()

    @property
    def get_rentals_list(self):
        return self._rentals_list

    def get_rental_id(self, book_id, client_id):
        for rental_id in self._rentals_list:
            if self._rentals_list[rental_id].get_book_id == book_id and self._rentals_list[rental_id].get_client_id \
                    == client_id:
                return rental_id

    def get_book_id_from_rental(self, rental_id):
        return self._rentals_list[rental_id].get_book_id

    def get_rental_date_from_rental(self, rental_id):
        return self._rentals_list[rental_id].get_rented_date

    def get_returned_date_from_rental(self, rental_id):
        return self._rentals_list[rental_id].get_returned_date

    def add_rental(self, rental_id, book_id, client_id, rental_date):
        rental_to_add = Rental(rental_id, book_id, client_id, rental_date)
        self._rentals_list[rental_to_add.get_rental_id] = rental_to_add

    def remove_rental(self, rental_id_to_be_removed):
        del self._rentals_list[rental_id_to_be_removed]

    def find_rental(self, rental_id_to_find):
        if rental_id_to_find in self._rentals_list.keys():
            return True
        else:
            raise RepositoryException("This is not the rental you're looking for")

    def get_client_id_from_rental(self, rental_id):
        return self._rentals_list[rental_id].get_client_id

    def get_rental_from_id(self, rental_id):
        return self._rentals_list[rental_id]


def generate_books(n=10):
    books_list = dict()
    for i in range(n):
        book_id = 1000 + i
        title = BOOK_LIST["title"][i]
        author = BOOK_LIST["author"][i]
        book = Book(book_id, title, author)
        if book_id % 2 == 0:
            book.update_number_of_rentals()
        books_list[book_id] = book
    return books_list


def validate_book_id(book_id, books_list):
    if book_id in books_list.keys():
        raise RepositoryException("A book with the ID: " + str(book_id) + " already exists")


def generate_clients(n=10):
    clients_list = dict()
    for i in range(n):
        client_id = 1000 + i
        name = CLIENTS_LIST[i]
        client = Client(client_id, name)
        clients_list[client_id] = client
    return clients_list


def validate_client_id(client_id, clients_list):
    if client_id in clients_list.keys():
        raise RepositoryException("A client with the ID: " + str(client_id) + " already exists")


def generate_rentals(n=5):
    rentals_list = dict()
    today = date.today()
    for i in range(n):
        rental_id = 1000 + i
        book_id = 1000 + i * 2
        client_id = 1000 + i * 2 + 1
        day = randint(1, 28)
        while day >= today.day:
            day = randint(1, 28)
        month = randint(1, 12)
        while month > today.month:
            month = randint(1, 12)
        year = today.year
        rental_date = date(year, month, day)
        rental = Rental(rental_id, book_id, client_id, rental_date)
        rentals_list[rental_id] = rental
    return rentals_list


def validate_rental_id(rental_id, rental_list):
    if rental_id in rental_list.keys():
        raise RepositoryException("A rental with the ID: " + str(rental_id) + " already exists")
