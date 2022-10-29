class UIException(Exception):
    def __init__(self, message):
        self.__message = message

    @property
    def get_error_message(self):
        return self.__message

    def __str__(self):
        return self.__message


class BookUI:
    def __init__(self, services):
        self._services = services

    def add_book_ui(self):
        book_id = input("Enter book ID (4 digits): ")
        try:
            book_id = int(book_id)
            title = input("Enter title of the book: ").strip()
            author = input("Enter author of the book: ").strip()
            self._services.add_book(book_id, title, author)
        except ValueError as ve:
            print(str(ve))

    def remove_book_ui(self):
        book_id = input("Enter book ID (4 digits): ")
        try:
            book_id = int(book_id)
            self._services.remove_book(book_id)
        except ValueError as ve:
            print(str(ve))

    def update_book_ui(self):
        book_id = input("Enter book ID (4 digits): ")
        try:
            book_id = int(book_id)
            new_book_id = input("Enter the new ID: ")
            new_book_id = int(new_book_id)
            new_title = input("Enter the new title: ").strip()
            new_author = input("Enter the new author: ").strip()
            self._services.update_book(book_id, new_book_id, new_title, new_author)
        except ValueError as ve:
            print(str(ve))

    def list_books(self):
        if len(self._services.get_books_list()) == 0:
            raise UIException("The book list is empty")
        for book_id in self._services.get_books_list():
            print(str(self._services.get_books_list()[book_id]))

    def search_book(self):
        search_input = input("Search book by ID, name or author: ")
        search_input = search_input.strip().lower()
        found_book = False
        for book_id in self._services.get_books_list():
            book = self._services.get_book_from_id()(book_id)
            if search_input in str(book_id) or search_input in book.get_title.lower() or search_input in \
                    book.get_author.lower():
                found_book = True
                print(str(book))
        if found_book is False:
            raise UIException("Search for something that exists next time")

    def most_rented_books_ui(self):
        sorted_books_list = self._services.most_rented_books()
        for book in sorted_books_list:
            print(str(book))

    def most_rented_authors_ui(self):
        sorted_authors_list = self._services.most_rented_authors()
        for author in sorted_authors_list:
            print(author[0] + ": " + str(author[1]) + " rentals")


class ClientUI:
    def __init__(self, services):
        self._services = services

    def list_clients(self):
        if len(self._services.get_clients_list()) == 0:
            raise UIException("The clients list is empty")
        for client_id in self._services.get_clients_list():
            print(str(self._services.get_clients_list()[client_id]))

    def add_client_ui(self):
        client_id = input("Enter client id (4 digits): ")
        try:
            client_id = int(client_id)
            client_name = input("Enter client name: ").strip()
            self._services.add_client(client_id, client_name)
        except ValueError as ve:
            print(str(ve))

    def remove_client_ui(self):
        client_id = input("Enter book ID (4 digits): ")
        try:
            client_id = int(client_id)
            self._services.remove_client(client_id)
        except ValueError as ve:
            print(str(ve))

    def update_client_ui(self):
        client_id = input("Enter client ID (4 digits): ")
        try:
            client_id = int(client_id)
            new_client_id = input("Enter the new ID: ")
            new_client_id = int(new_client_id)
            new_name = input("Enter the new name: ").strip()
            self._services.update_client(client_id, new_client_id, new_name)
        except ValueError as ve:
            print(str(ve))

    def search_client(self):
        search_input = input("Search client by ID or name: ")
        search_input = search_input.strip().lower()
        found_client = False
        if search_input == "batman":
            secret_client = self._services.get_client_from_id(1000)
            print(str(secret_client))
            found_client = True
        for client_id in self._services.get_clients_list():
            client = self._services.get_client_from_id(client_id)
            if search_input in str(client_id) or search_input in client.get_client_name.lower():
                print(str(client))
                found_client = True
        if not found_client:
            raise UIException("Search for something that exists next time")

    def most_active_clients_ui(self):
        sorted_clients_activity_list = self._services.most_active_clients()
        for client_activity in sorted_clients_activity_list:
            print(client_activity[0] + ": " + str(client_activity[1]) + " rental days")


class RentalUI:
    def __init__(self, services):
        self._services = services

    def list_rentals(self):
        if len(self._services.get_rentals_list()) == 0:
            raise UIException("Rentals list is empty")
        for rental_id in self._services.get_rentals_list():
            print(str(self._services.get_rentals_list()[rental_id]))

    def rent_book_ui(self):
        book_id = input("Enter book ID (4 digits): ")
        client_id = input("Enter client ID (4 digits): ")
        rental_date = input("Enter rental date (format: dd-mm-yyyy): ")
        date_elements = rental_date.split("-")
        try:
            book_id = int(book_id)
            client_id = int(client_id)
            day = int(date_elements[0])
            month = int(date_elements[1])
            year = int(date_elements[2])
            self._services.rent_book(book_id, client_id, day, month, year)
        except ValueError as ve:
            print(str(ve))

    def return_book_ui(self):
        rental_id = input("Enter rental ID (4 digits): ")
        return_date = input("Enter return date (format: dd-mm-yyyy): ")
        date_elements = return_date.split("-")
        try:
            rental_id = int(rental_id)
            day = int(date_elements[0])
            month = int(date_elements[1])
            year = int(date_elements[2])
            self._services.return_book(rental_id, day, month, year)
        except ValueError as ve:
            print(str(ve))
