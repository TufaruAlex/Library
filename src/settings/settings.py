from src.repository.repository import BookRepository, ClientRepository, RentalRepository
from src.repository.text_file_repository import BookTextFileRepository, ClientTextFileRepository, \
    RentalTextFileRepository
from src.repository.binary_file_repository import BookBinaryFileRepository, ClientBinaryFileRepository, \
    RentalBinaryFileRepository
from src.repository.json_file_repository import BooksJSONFileRepository, ClientJSONFileRepository, \
    RentalJSONFileRepository
from configparser import ConfigParser


class Settings:
    def __init__(self):
        config = ConfigParser()
        config.read(r'C:/Users/tufar/Desktop/Faculty/Year 1/Semester 1/FP/a9-917-Alex-Tufaru/src/settings/'
                    r'settings.properties')
        repository_type = config.get("options", "repository")
        books_file_name = config.get("options", "books")
        clients_file_name = config.get("options", "clients")
        rentals_file_name = config.get("options", "rentals")
        if repository_type == "inmemory":
            self.book_repository = BookRepository()
            self.client_repository = ClientRepository()
            self.rental_repository = RentalRepository()
        elif repository_type == "textfiles":
            self.book_repository = BookTextFileRepository(books_file_name)
            self.client_repository = ClientTextFileRepository(clients_file_name)
            self.rental_repository = RentalTextFileRepository(rentals_file_name)
        elif repository_type == "binaryfiles":
            self.book_repository = BookBinaryFileRepository(books_file_name)
            self.client_repository = ClientBinaryFileRepository(clients_file_name)
            self.rental_repository = RentalBinaryFileRepository(rentals_file_name)
        elif repository_type == "jsonfiles":
            self.book_repository = BooksJSONFileRepository(books_file_name)
            self.client_repository = ClientJSONFileRepository(clients_file_name)
            self.rental_repository = RentalJSONFileRepository(rentals_file_name)

    def get_all_repositories(self):
        return self.book_repository, self.client_repository, self.rental_repository
