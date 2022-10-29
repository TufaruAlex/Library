from src.domain.book import Book
from src.domain.client import Client
from datetime import date
from src.services.undo import Operation, CascadingOperation, CallFunction


class ServicesException(Exception):
    pass


class Services:
    def __init__(self, book_repository, client_repository, rental_repository, undo):
        self._book_repository = book_repository
        self._client_repository = client_repository
        self._rental_repository = rental_repository
        self._undo = undo

    def get_books_list(self):
        return self._book_repository.get_books_list

    def get_clients_list(self):
        return self._client_repository.get_clients_list

    def get_rentals_list(self):
        return self._rental_repository.get_rentals_list

    def rent_book(self, book_id, client_id, day, month, year):
        """
        Function rents an available book to the specified customer
        :param day: day of the rental
        :param month: month of the rental
        :param year: month of the rental
        :param book_id: id of the book to be rented
        :param client_id: id of the client to rent the book
        """
        if book_id < 1000 or book_id > 9999:
            raise ServicesException("ID must be 4 digits")
        if client_id < 1000 or client_id > 9999:
            raise ServicesException("ID must be 4 digits")
        if day < 1 or day > 30:
            raise ServicesException("Not a day of the month")
        if month < 1 or month > 12:
            raise ServicesException("Not a month of the year")
        today = date.today()
        if year != today.year:
            raise ServicesException("Please enter the current year")
        elif month < today.month:
            raise ServicesException("The rental date must be at least today")
        elif day < today.day:
            raise ServicesException("The rental date must be at least today")
        self._book_repository.find_book(book_id)
        self._client_repository.find_client(client_id)
        if self._book_repository.get_rental_state(book_id) is True:
            raise ServicesException("Book is already rented. Please try again later")
        rental_date = date(year, month, day)
        for i in range(len(self.get_rentals_list().keys()) + 1):
            possible_id = 1000 + i
            if possible_id not in self.get_rentals_list().keys():
                rental_id = possible_id
                break
        self._rental_repository.add_rental(rental_id, book_id, client_id, rental_date)
        self._book_repository.set_rental_state(book_id, True)
        self.get_book_from_id(book_id).update_number_of_rentals()
        operations = []
        undo_function = CallFunction(self._rental_repository.remove_rental, rental_id)
        redo_function = CallFunction(self.rent_book, book_id, client_id, day, month, year)
        operations.append(Operation(undo_function, redo_function))
        undo_function = CallFunction(self._book_repository.set_rental_state, book_id, False)
        operations.append(Operation(undo_function))
        self._undo.record(CascadingOperation(operations))

    def return_book(self, rental_id, day, month, year):
        """
        Function returns rented book by setting the rental state of the book
        :param day: day of return
        :param month: month of return
        :param year: year of return
        :param rental_id: id of the rental to be returned
        """
        # todo better date system
        if rental_id < 1000 or rental_id > 9999:
            raise ServicesException("ID must be 4 digits")
        if day < 1 or day > 30:
            raise ServicesException("Not a day of the month")
        if month < 1 or month > 12:
            raise ServicesException("Not a month of the year")
        current_year = date.today().year
        if year != current_year:
            raise ServicesException("Please enter the current year")
        rental = self._rental_repository.get_rental_from_id(rental_id)
        if month < rental.get_rented_date.month:
            raise ServicesException("The return date must be after the rental date")
        elif day < rental.get_rented_date.day:
            raise ServicesException("The return date must be after the rental date")
        return_date = date(year, month, day)
        self._rental_repository.find_rental(rental_id)
        if self._rental_repository.get_returned_date_from_rental(rental_id) != "not returned":
            raise ServicesException("Book was already returned")
        self._book_repository.set_rental_state(self._rental_repository.get_book_id_from_rental(rental_id), False)
        self._rental_repository.get_rentals_list[rental_id].set_returned_date(return_date)
        operations = []
        book_id = self._rental_repository.get_book_id_from_rental(rental_id)
        client_id = self._rental_repository.get_client_id_from_rental(rental_id)
        rental_date = self._rental_repository.get_rental_date_from_rental(rental_id)
        undo_function = CallFunction(self._rental_repository.remove_rental, rental_id)
        redo_function = CallFunction(self.return_book, rental_id, day, month, year)
        operations.append(Operation(undo_function, redo_function))
        undo_function = CallFunction(self._rental_repository.add_rental, rental_id, book_id, client_id, rental_date)
        operations.append(Operation(undo_function))
        undo_function = CallFunction(self._book_repository.set_rental_state, book_id, True)
        operations.append(Operation(undo_function))
        self._undo.record(CascadingOperation(operations))

    def add_book(self, book_id, title, author):
        """
        Function adds a book to the book list
        :param book_id: unique id of the book
        :param title: title of the book
        :param author: author of the book
        """
        if book_id < 1000 or book_id > 9999:
            raise ServicesException("ID must be 4 digits")
        book = Book(book_id, title, author)
        self._book_repository.add_book(book)
        operations = []
        undo_function = CallFunction(self._book_repository.remove_book, book_id)
        redo_function = CallFunction(self._book_repository.add_book, book)
        operations.append(Operation(undo_function, redo_function))
        for rental in list(self.get_rentals_list().values()):
            if rental.get_book_id == book_id:
                undo_function = CallFunction(self._rental_repository.remove_rental, rental.get_rental_id)
                operations.append(Operation(undo_function))
        self._undo.record(CascadingOperation(operations))

    def remove_book(self, book_id):
        """
        Function removes a book from the book list
        :param book_id: id of the book to be removed
        """
        if book_id < 1000 or book_id > 9999:
            raise ServicesException("ID must be 4 digits")
        self._book_repository.find_book(book_id)
        book = self.get_book_from_id(book_id)
        operations = []
        undo_function = CallFunction(self._book_repository.add_book, book)
        redo_function = CallFunction(self._book_repository.remove_book, book_id)
        operations.append(Operation(undo_function, redo_function))
        for rental in list(self.get_rentals_list().values()):
            if rental.get_book_id == book_id:
                self._rental_repository.remove_rental(rental.get_rental_id)
                undo_function = CallFunction(self._rental_repository.add_rental, rental.get_rental_id,
                                             rental.get_book_id, rental.get_client_id, rental.get_rented_date)
                redo_function = CallFunction(self._rental_repository.remove_rental, rental.get_rental_id)
                operations.append(Operation(undo_function, redo_function))
        self._book_repository.remove_book(book_id)
        self._undo.record(CascadingOperation(operations))

    def update_book(self, book_id, new_book_id, new_title, new_author):
        """
        The function updates a book by changing the id, title and author
        :param book_id: id of the book to be updated
        :param new_book_id: the id to replace the old one
        :param new_title: new title of the book
        :param new_author: new author of the book
        """
        if book_id < 1000 or book_id > 9999:
            raise ServicesException("ID must be 4 digits")
        self._book_repository.find_book(book_id)
        if new_book_id < 1000 or new_book_id > 9999:
            raise ServicesException("ID must be 4 digits")
        book = self.get_book_from_id(book_id)
        undo_function = CallFunction(self._book_repository.update_book, new_book_id, book_id, book.get_title,
                                     book.get_author)
        redo_function = CallFunction(self._book_repository.update_book, book_id, new_book_id, new_title, new_author)
        self._undo.record(Operation(undo_function, redo_function))
        self._book_repository.update_book(book_id, new_book_id, new_title, new_author)
        for rental in list(self.get_rentals_list().values()):
            if rental.get_book_id == book_id:
                rental.set_book_id(new_book_id)

    def get_book_from_id(self, book_id):
        return self.get_books_list()[book_id]

    def add_client(self, client_id, client_name):
        """
        Function adds a client to the client list
        :param client_id: unique id of the client
        :param client_name: name of the client
        """
        if client_id < 1000 or client_id > 9999:
            raise ServicesException("ID must be 4 digits")
        client = Client(client_id, client_name)
        self._client_repository.add_client(client)
        operations = []
        undo_function = CallFunction(self._client_repository.remove_client, client_id)
        redo_function = CallFunction(self._client_repository.add_client, client)
        operations.append(Operation(undo_function, redo_function))
        for rental in list(self.get_rentals_list().values()):
            if rental.get_client_id == client_id:
                undo_function = CallFunction(self._rental_repository.remove_rental, rental.get_rental_id)
                operations.append(Operation(undo_function))
        self._undo.record(CascadingOperation(operations))

    def remove_client(self, client_id):
        """
        Function removes a client from the client list
        :param client_id: id of the client to be removed
        """
        if client_id < 1000 or client_id > 9999:
            raise ServicesException("ID must be 4 digits")
        self._client_repository.find_client(client_id)
        client = self.get_client_from_id(client_id)
        operations = []
        undo_function = CallFunction(self._client_repository.add_client, client)
        redo_function = CallFunction(self._client_repository.remove_client, client_id)
        operations.append(Operation(undo_function, redo_function))
        for rental in list(self.get_rentals_list().values()):
            if rental.get_client_id == client_id:
                self._rental_repository.remove_rental(rental.get_rental_id)
                undo_function = CallFunction(self._rental_repository.add_rental, rental.get_rental_id,
                                             rental.get_book_id, rental.get_client_id, rental.get_rented_date)
                redo_function = CallFunction(self._rental_repository.remove_rental, rental.get_rental_id)
                operations.append(Operation(undo_function, redo_function))
        self._client_repository.remove_client(client_id)
        self._undo.record(CascadingOperation(operations))

    def update_client(self, client_id, new_client_id, new_name):
        """
        Function updates a client by changing the id and the name
        :param client_id: id of the client to be updated
        :param new_client_id: new client id to replace the old one
        :param new_name: new name of the client
        """
        if client_id < 1000 or client_id > 9999:
            raise ServicesException("ID must be 4 digits")
        self._client_repository.find_client(client_id)
        if new_client_id < 1000 or new_client_id > 9999:
            raise ServicesException("ID must be 4 digits")
        client = self.get_client_from_id(client_id)
        undo_function = CallFunction(self._client_repository.update_client, new_client_id, client_id,
                                     client.get_client_name)
        redo_function = CallFunction(self._client_repository.update_client, client_id, new_client_id, new_name)
        self._undo.record(Operation(undo_function, redo_function))
        self._client_repository.update_client(client_id, new_client_id, new_name)
        for rental in list(self.get_rentals_list().values()):
            if rental.get_client_id == client_id:
                rental.set_client_id(new_client_id)

    def get_client_from_id(self, client_id):
        return self.get_clients_list()[client_id]

    def most_rented_books(self):
        sorted_book_list = sorted(self.get_books_list().values(), key=lambda book: book.get_number_of_rentals,
                                  reverse=True)
        return sorted_book_list

    def most_active_clients(self):
        clients_activity_list = dict()
        for client in self.get_clients_list().values():
            clients_activity_list[client.get_client_id] = [client.get_client_name, 0]
        for rental in self.get_rentals_list().values():
            clients_activity_list[rental.get_client_id][1] += len(rental)
        sorted_clients_activity_list = sorted(clients_activity_list.values(), key=lambda client_activity:
                                              client_activity[1], reverse=True)
        return sorted_clients_activity_list

    def most_rented_authors(self):
        authors_list = dict()
        for book in self.get_books_list().values():
            if book.get_author not in authors_list.keys():
                authors_list[book.get_author] = [book.get_author, book.get_number_of_rentals]
            else:
                authors_list[book.get_author][1] += book.get_number_of_rentals
        sorted_authors_list = sorted(authors_list.values(), key=lambda author: author[1], reverse=True)
        return sorted_authors_list
