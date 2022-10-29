from src.repository.repository import BookRepository, ClientRepository, RentalRepository
from src.domain.book import Book
from src.domain.client import Client
from datetime import datetime


class BookTextFileRepository(BookRepository):
    def __init__(self, books_file_name):
        super().__init__()
        self._books_list = dict()
        self.__file_name = books_file_name
        self._load_file()

    def _load_file(self):
        file = open(self.__file_name, "rt")
        for line in file.readlines():
            book_id, title, author = line.split(", ")
            author = author.removesuffix("\n")
            self.add_book(Book(int(book_id), title, author))
        file.close()

    def _save_file(self):
        file = open(self.__file_name, "wt")
        for book in self.get_books_list.values():
            file.write(str(book.get_book_id) + ", " + book.get_title + ", " + book.get_author + "\n")
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


class ClientTextFileRepository(ClientRepository):
    def __init__(self, clients_file_name):
        super().__init__()
        self._clients_list = dict()
        self.__file_name = clients_file_name
        self._load_file()

    def _load_file(self):
        file = open(self.__file_name, "rt")
        for line in file.readlines():
            client_id, name = line.split(", ")
            name = name.removesuffix("\n")
            self.add_client(Client(int(client_id), name))
        file.close()

    def _save_file(self):
        file = open(self.__file_name, "wt")
        for client in self.get_clients_list.values():
            file.write(str(client.get_client_id) + ", " + client.get_client_name + "\n")
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


class RentalTextFileRepository(RentalRepository):
    def __init__(self, repository_file_name):
        super().__init__()
        self.__rentals_list = dict()
        self.__file_name = repository_file_name
        self._load_file()

    def _load_file(self):
        file = open(self.__file_name, "rt")
        for line in file.readlines():
            rental_id, book_id, client_id, rented_date = line.split(", ")
            rented_date = rented_date.removesuffix("\n")
            rented_date = datetime.strptime(rented_date, '%Y-%m-%d')
            self.add_rental(int(rental_id), int(book_id), int(client_id), rented_date)
        file.close()

    def _save_file(self):
        file = open(self.__file_name, "wt")
        for rental in self.get_rentals_list.values():
            file.write(str(rental.get_rental_id) + ", " + str(rental.get_book_id) + ", " + str(rental.get_client_id) +
                       ", " + rental.get_rented_date.strftime('%Y-%m-%d') + "\n")
        file.close()

    def add_rental(self, rental_id, book_id, client_id, rental_date):
        super().add_rental(rental_id, book_id, client_id, rental_date)
        self._save_file()

    def remove_rental(self, rental_id_to_be_removed):
        super().remove_rental(rental_id_to_be_removed)
        self._save_file()
