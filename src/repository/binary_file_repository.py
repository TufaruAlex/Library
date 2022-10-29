from src.repository.repository import BookRepository, ClientRepository, RentalRepository
import pickle


class BookBinaryFileRepository(BookRepository):
    def __init__(self, books_file_name):
        super().__init__()
        self._books_list = dict()
        self._file_name = books_file_name
        # self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rb")
        self._books_list = pickle.load(file)
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")
        pickle.dump(self._books_list, file)
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


class ClientBinaryFileRepository(ClientRepository):
    def __init__(self, clients_file_name):
        super().__init__()
        self._clients_list = dict()
        self._file_name = clients_file_name
        # self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rb")
        self._clients_list = pickle.load(file)
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")
        pickle.dump(self._clients_list, file)
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


class RentalBinaryFileRepository(RentalRepository):
    def __init__(self, repository_file_name):
        super().__init__()
        self.__rentals_list = dict()
        self.__file_name = repository_file_name
        # self._load_file()

    def _load_file(self):
        file = open(self.__file_name, "rb")
        self.__rentals_list = pickle.load(file)
        file.close()

    def _save_file(self):
        file = open(self.__file_name, "wb")
        pickle.dump(self.__rentals_list, file)
        file.close()

    def add_rental(self, rental_id, book_id, client_id, rental_date):
        super().add_rental(rental_id, book_id, client_id, rental_date)
        self._save_file()

    def remove_rental(self, rental_id_to_be_removed):
        super().remove_rental(rental_id_to_be_removed)
        self._save_file()
