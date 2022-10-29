from src.repository.repository import BookRepository, ClientRepository, RentalRepository
from src.domain.book import Book
from src.domain.client import Client
import json
from datetime import datetime


class BooksJSONFileRepository(BookRepository):
    def __init__(self, books_file_name):
        super().__init__()
        self._books_list = dict()
        self.__file_name = books_file_name
        self._load_file()

    def _load_file(self):
        file = open(self.__file_name, "r")
        for book in json.load(file):
            book = Book(int(book["id"]), book["title"], book["author"])
            super().add_book(book)
        file.close()

    def _save_file(self):
        file = open(self.__file_name, "w")
        books_list = []
        for book in super().get_books_list.values():
            book_to_add = {"id": book.get_book_id, "title": book.get_title, "author": book.get_author}
            books_list.append(book_to_add)
        json.dump(books_list, file, indent=4)
        file.close()

    def add_book(self, book_to_add):
        super().add_book(book_to_add)
        self._save_file()

    def remove_book(self, book_to_remove_id):
        super().remove_book(book_to_remove_id)
        self._save_file()

    def update_book(self, book_id_to_update, new_book_id, new_title, new_author):
        super().update_book(book_id_to_update, new_book_id, new_title, new_author)
        self._save_file()


class ClientJSONFileRepository(ClientRepository):
    def __init__(self, clients_file_name):
        super().__init__()
        self._clients_list = dict()
        self.__file_name = clients_file_name
        self._load_file()

    def _load_file(self):
        file = open(self.__file_name, "r")
        for client in json.load(file):
            client = Client(int(client["id"]), client["name"])
            super().add_client(client)
        file.close()

    def _save_file(self):
        file = open(self.__file_name, "w")
        clients_list = []
        for client in super().get_clients_list.values():
            client_to_add = {"id": client.get_client_id, "name": client.get_client_name}
            clients_list.append(client_to_add)
        json.dump(clients_list, file, indent=4)
        file.close()

    def add_client(self, client_to_add):
        super().add_client(client_to_add)
        self._save_file()

    def remove_client(self, client_to_remove_id):
        super().remove_client(client_to_remove_id)
        self._save_file()

    def update_client(self, client_id_to_update, new_client_id, new_name):
        super().update_client(client_id_to_update, new_client_id, new_name)
        self._save_file()


class RentalJSONFileRepository(RentalRepository):
    def __init__(self, repository_file_name):
        super().__init__()
        self.__rentals_list = dict()
        self.__file_name = repository_file_name
        self._load_file()

    def _load_file(self):
        file = open(self.__file_name, "r")
        for rental in json.load(file):
            rented_date = datetime.strptime(rental["rental date"], '%Y-%m-%d')
            super().add_rental(int(rental["rental id"]), int(rental["book id"]), int(rental["client id"]), rented_date)
        file.close()

    def _save_file(self):
        file = open(self.__file_name, "w")
        rentals_list = []
        for rental in super().get_rentals_list.values():
            rental_to_add = {"rental id": rental.get_rental_id, "book id": rental.get_book_id,
                             "client id": rental.get_client_id, "rental date": str(rental.get_rented_date)}
            rentals_list.append(rental_to_add)
        json.dump(rentals_list, file, indent=4)
        file.close()

    def add_rental(self, rental_id, book_id, client_id, rental_date):
        super().add_rental(rental_id, book_id, client_id, rental_date)
        self._save_file()

    def remove_rental(self, rental_id_to_be_removed):
        super().remove_rental(rental_id_to_be_removed)
        self._save_file()
