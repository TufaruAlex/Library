from services import Services, ServicesException
from src.repository.repository import BookRepository, ClientRepository, RentalRepository, RepositoryException
from src.domain.book import Book
from src.domain.client import Client
from src.services.undo import Undo, UndoException
import unittest
from datetime import date


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self._book_repository = BookRepository()
        self._client_repository = ClientRepository()
        self._rental_repository = RentalRepository()
        self._undo = Undo()
        self._services = Services(self._book_repository, self._client_repository, self._rental_repository, self._undo)

    def tearDown(self) -> None:
        pass

    def test_add_book__unique_id__add_successfully(self):
        book_id = 1234
        title = "Ion"
        author = "Liviu Rebreanu"
        self._services.add_book(book_id, title, author)
        self.assertEqual(self._services.get_books_list()[1234], Book(1234, title, author))

    def test_add_book__3_digits_id__throw_exception(self):
        book_id = 123
        title = "Ion"
        author = "Liviu Rebreanu"
        with self.assertRaises(ServicesException):
            self._services.add_book(book_id, title, author)

    def test_add_book__5_digits_id__throw_exception(self):
        book_id = 12345
        title = "Ion"
        author = "Liviu Rebreanu"
        with self.assertRaises(ServicesException):
            self._services.add_book(book_id, title, author)

    def test_add_book__duplicate_id__throw_exception(self):
        book_id = 1003
        title = "Ion"
        author = "Liviu Rebreanu"
        with self.assertRaises(RepositoryException):
            self._services.add_book(book_id, title, author)

    def test_remove_book__valid_id__remove_successfully(self):
        book_id = 1003
        self._services.remove_book(book_id)
        with self.assertRaises(RepositoryException):
            self._book_repository.find_book(book_id)

    def test_remove_book__3_digits_id__throw_exception(self):
        book_id = 100
        with self.assertRaises(ServicesException):
            self._services.remove_book(book_id)

    def test_remove_book__5_digits_id__throw_exception(self):
        book_id = 10031
        with self.assertRaises(ServicesException):
            self._services.remove_book(book_id)

    def test_remove_book__id_not_in_books_list__throws_exception(self):
        book_id = 1010
        with self.assertRaises(RepositoryException):
            self._services.remove_book(book_id)

    def test_update_book__valid_book_id_and_new_book_id__update_successfully(self):
        book_id = 1003
        new_book_id = 1010
        new_title = "Ion"
        new_author = "Liviu Rebreanu"
        self._services.update_book(book_id, new_book_id, new_title, new_author)
        self.assertEqual(self._services.get_books_list()[1010], Book(1010, "Ion", "Liviu Rebreanu"))

    def test_update_book__3_digits_book_id__throws_exception(self):
        book_id = 100
        new_book_id = 1010
        new_title = "Ion"
        new_author = "Liviu Rebreanu"
        with self.assertRaises(ServicesException):
            self._services.update_book(book_id, new_book_id, new_title, new_author)

    def test_update_book__5_digits_book_id__throws_exception(self):
        book_id = 10031
        new_book_id = 1010
        new_title = "Ion"
        new_author = "Liviu Rebreanu"
        with self.assertRaises(ServicesException):
            self._services.update_book(book_id, new_book_id, new_title, new_author)

    def test_update_book__3_digits_new_book_id__throws_exception(self):
        book_id = 1003
        new_book_id = 101
        new_title = "Ion"
        new_author = "Liviu Rebreanu"
        with self.assertRaises(ServicesException):
            self._services.update_book(book_id, new_book_id, new_title, new_author)

    def test_update_book__5_digits_new_book_id__throws_exception(self):
        book_id = 1003
        new_book_id = 10103
        new_title = "Ion"
        new_author = "Liviu Rebreanu"
        with self.assertRaises(ServicesException):
            self._services.update_book(book_id, new_book_id, new_title, new_author)

    def test_update_book__duplicate_new_book_id__throws_exception(self):
        book_id = 1003
        new_book_id = 1004
        new_title = "Ion"
        new_author = "Liviu Rebreanu"
        with self.assertRaises(RepositoryException):
            self._services.update_book(book_id, new_book_id, new_title, new_author)

    def test_add_client__unique_id__add_successfully(self):
        client_id = 1234
        name = "Tony Stark"
        self._services.add_client(client_id, name)
        self.assertEqual(self._services.get_clients_list()[client_id], Client(1234, "Bruce Wayne"))

    def test_add_client__3_digits_id__throw_exception(self):
        client_id = 123
        name = "Tobey Maguire"
        with self.assertRaises(ServicesException):
            self._services.add_client(client_id, name)

    def test_add_client__5_digits_id__throw_exception(self):
        client_id = 12345
        name = "Andrew Garfield"
        with self.assertRaises(ServicesException):
            self._services.add_client(client_id, name)

    def test_add_client__duplicate_id__throw_exception(self):
        client_id = 1003
        name = "Otto Octavius"
        with self.assertRaises(RepositoryException):
            self._services.add_client(client_id, name)

    def test_remove_client__valid_id__remove_successfully(self):
        client_id = 1003
        self._services.remove_client(client_id)
        with self.assertRaises(RepositoryException):
            self._client_repository.find_client(client_id)

    def test_remove_client__3_digits_id__throw_exception(self):
        client_id = 100
        with self.assertRaises(ServicesException):
            self._services.remove_client(client_id)

    def test_remove_client__5_digits_id__throw_exception(self):
        client_id = 10031
        with self.assertRaises(ServicesException):
            self._services.remove_client(client_id)

    def test_remove_client__id_not_in_clients_list__throws_exception(self):
        client_id = 1010
        with self.assertRaises(RepositoryException):
            self._services.remove_client(client_id)

    def test_update_client__valid_client_id_and_new_client_id__update_successfully(self):
        client_id = 1003
        new_client_id = 1010
        new_name = "Norman Osborn"
        self._services.update_client(client_id, new_client_id, new_name)
        self.assertEqual(self._client_repository.get_clients_list[new_client_id], Client(new_client_id, new_name))

    def test_update_client__3_digits_client_id__throws_exception(self):
        client_id = 100
        new_client_id = 1010
        new_name = "Samuel L. Jackson"
        with self.assertRaises(ServicesException):
            self._services.update_client(client_id, new_client_id, new_name)

    def test_update_client__5_digits_client_id__throws_exception(self):
        client_id = 10031
        new_client_id = 1010
        new_name = "Mary-Jane Watson"
        with self.assertRaises(ServicesException):
            self._services.update_client(client_id, new_client_id, new_name)

    def test_update_client__3_digits_new_client_id__throws_exception(self):
        client_id = 1003
        new_client_id = 101
        new_name = "Gwen Stacy"
        with self.assertRaises(ServicesException):
            self._services.update_client(client_id, new_client_id, new_name)

    def test_update_client__5_digits_new_client_id__throws_exception(self):
        client_id = 1003
        new_client_id = 10103
        new_name = "Stan Lee"
        with self.assertRaises(ServicesException):
            self._services.update_client(client_id, new_client_id, new_name)

    def test_update_client__duplicate_new_client_id__throws_exception(self):
        client_id = 1003
        new_client_id = 1004
        new_name = "Alan Turing"
        with self.assertRaises(RepositoryException):
            self._services.update_client(client_id, new_client_id, new_name)

    def test_rent_book__valid_book_and_client_id__rent_successfully(self):
        book_id = 1003
        client_id = 1005
        day = date.today().day
        month = date.today().month
        year = date.today().year
        self._services.rent_book(book_id, client_id, day, month, year)
        self.assertEqual(self._book_repository.get_rental_state(book_id), True)

    def test_rent_book__3_digits_book_id__throws_exception(self):
        book_id = 100
        client_id = 1005
        day = date.today().day
        month = date.today().month
        year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_rent_book__5_digits_book_id__throws_exception(self):
        book_id = 10031
        client_id = 1005
        day = date.today().day
        month = date.today().month
        year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_rent_book__3_digits_client_id__throws_exception(self):
        book_id = 1003
        client_id = 100
        day = date.today().day
        month = date.today().month
        year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_rent_book__5_digits_client_id__throws_exception(self):
        book_id = 1003
        client_id = 10051
        day = date.today().day
        month = date.today().month
        year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_rent_book__book_id_not_in_book_list__throws_exception(self):
        book_id = 2010
        client_id = 1005
        day = date.today().day
        month = date.today().month
        year = date.today().year
        with self.assertRaises(RepositoryException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_rent_book__client_id_not_in_client_list__throws_exception(self):
        book_id = 1003
        client_id = 2010
        day = date.today().day
        month = date.today().month
        year = date.today().year
        with self.assertRaises(RepositoryException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_rent_book__book_already_rented__throws_exception(self):
        book_id = 1003
        client_id = 1005
        day = date.today().day
        month = date.today().month
        year = date.today().year
        self._services.rent_book(book_id, client_id, day, month, year)
        other_client_id = 1006
        with self.assertRaises(ServicesException):
            self._services.rent_book(book_id, other_client_id, day, month, year)

    def test_rent_book__invalid_rental_day__throws_exception(self):
        book_id = 1003
        client_id = 1005
        day = 40
        month = date.today().month
        year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_rent_book__invalid_rental_month__throws_exception(self):
        book_id = 1003
        client_id = 1005
        day = date.today().day
        month = 15
        year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_rent_book__invalid_rental_year__throws_exception(self):
        book_id = 1003
        client_id = 1005
        day = date.today().day
        month = date.today().month
        year = 2077
        with self.assertRaises(ServicesException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_rent_book__rental_day_before_today__throws_exception(self):
        book_id = 1003
        client_id = 1005
        day = date.today().day - 1
        month = date.today().month
        year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_rent_book__rental_month_before_current_month__throws_exception(self):
        book_id = 1003
        client_id = 1005
        day = date.today().day
        month = date.today().month - 1
        year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.rent_book(book_id, client_id, day, month, year)

    def test_return_book__valid_rental_id__return_book_successfully(self):
        rental_id = 1001
        book_id = self._rental_repository.get_book_id_from_rental(rental_id)
        return_day = date.today().day + 1
        return_month = date.today().month
        return_year = date.today().year
        self._services.return_book(rental_id, return_day, return_month, return_year)
        self.assertEqual(self._book_repository.get_rental_state(book_id), False)

    def test_return_book__3_digits_rental_id__throws_exception(self):
        rental_id = 100
        return_day = date.today().day + 1
        return_month = date.today().month + 1
        return_year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.return_book(rental_id, return_day, return_month, return_year)

    def test_return_book__5_digits_rental_id__throws_exception(self):
        rental_id = 10011
        return_day = date.today().day + 1
        return_month = date.today().month + 1
        return_year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.return_book(rental_id, return_day, return_month, return_year)

    def test_return_book__book_already_returned__throws_exception(self):
        rental_id = 1001
        return_day = date.today().day + 1
        return_month = date.today().month
        return_year = date.today().year
        self._services.return_book(rental_id, return_day, return_month, return_year)
        with self.assertRaises(ServicesException):
            self._services.return_book(rental_id, return_day, return_month, return_year)

    def test_return_book__invalid_return_day__throws_exception(self):
        rental_id = 1001
        return_day = 40
        return_month = date.today().month + 1
        return_year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.return_book(rental_id, return_day, return_month, return_year)

    def test_return_book__invalid_return_month__throws_exception(self):
        rental_id = 1001
        return_day = date.today().day
        return_month = 15
        return_year = date.today().year
        with self.assertRaises(ServicesException):
            self._services.return_book(rental_id, return_day, return_month, return_year)

    def test_return_book__invalid_return_year__throws_exception(self):
        rental_id = 1001
        return_day = date.today().day
        return_month = date.today().month + 1
        return_year = 2077
        with self.assertRaises(ServicesException):
            self._services.return_book(rental_id, return_day, return_month, return_year)

    def test_undo__no_operation_to_undo__throws_exception(self):
        with self.assertRaises(UndoException):
            self._undo.undo()

    def test_redo__no_operation_to_redo__throws_exception(self):
        book_id = 1003
        client_id = 1005
        day = date.today().day
        month = date.today().month
        year = date.today().year
        self._services.rent_book(book_id, client_id, day, month, year)
        with self.assertRaises(UndoException):
            self._undo.redo()

    def test_undo_rent_book__one_rental__undo_successfully(self):
        book_id = 1003
        client_id = 1005
        day = date.today().day
        month = date.today().month
        year = date.today().year
        self._services.rent_book(book_id, client_id, day, month, year)
        rental_id = self._rental_repository.get_rental_id(book_id, client_id)
        self._undo.undo()
        with self.assertRaises(RepositoryException):
            self._rental_repository.find_rental(rental_id)

    # def test_undo_rent_book__2_rentals__undo_successfully(self):
    #     book_id = 1003
    #     client_id = 1005
    #     day = date.today().day
    #     month = date.today().month
    #     year = date.today().year
    #     self._services.rent_book(book_id, client_id, day, month, year)
    #     first_rental_id = self._rental_repository.get_rental_id(book_id, client_id)
    #     book_id = 1005
    #     client_id = 1002
    #     self._services.rent_book(book_id, client_id, day, month, year)
    #     second_rental_id = self._rental_repository.get_rental_id(book_id, client_id)
    #     self._undo.undo()
    #     with self.assertRaises(RepositoryException):
    #         self._rental_repository.find_rental(second_rental_id)
    #     self._undo.undo()
    #     with self.assertRaises(RepositoryException):
    #         self._rental_repository.find_rental(first_rental_id)

    def test_redo_rent_book__one_rental__redo_successfully(self):
        book_id = 1003
        client_id = 1005
        day = date.today().day
        month = date.today().month
        year = date.today().year
        self._services.rent_book(book_id, client_id, day, month, year)
        rental_id = self._rental_repository.get_rental_id(book_id, client_id)
        self._undo.undo()
        self._undo.redo()
        self.assertEqual(self._rental_repository.find_rental(rental_id), True)

    def test_undo_return_book__one_return__undo_successfully(self):
        rental_id = 1001
        return_day = date.today().day + 1
        return_month = date.today().month
        return_year = date.today().year
        self._services.return_book(rental_id, return_day, return_month, return_year)
        self._undo.undo()
        self.assertEqual(self._rental_repository.find_rental(rental_id), True)

    def test_redo_return_book__one_return__redo_successfully(self):
        rental_id = 1001
        return_day = date.today().day + 1
        return_month = date.today().month
        return_year = date.today().year
        self._services.return_book(rental_id, return_day, return_month, return_year)
        self._undo.undo()
        self._undo.redo()
        book_id = self._rental_repository.get_book_id_from_rental(rental_id)
        self.assertEqual(self._book_repository.get_rental_state(book_id), False)

    def test_undo_add_book__one_book__undo_successfully(self):
        book_id = 1234
        title = "Ion"
        author = "Liviu Rebreanu"
        self._services.add_book(book_id, title, author)
        self._undo.undo()
        with self.assertRaises(RepositoryException):
            self._book_repository.find_book(book_id)

    def test_redo_add_book__one_book_redo_successfully(self):
        book_id = 1234
        title = "Ion"
        author = "Liviu Rebreanu"
        self._services.add_book(book_id, title, author)
        self._undo.undo()
        self._undo.redo()
        self.assertEqual(self._services.get_books_list()[book_id], Book(book_id, title, author))

    def test_undo_remove_book__one_book__undo_successfully(self):
        book_id = 1003
        self._services.remove_book(book_id)
        self._undo.undo()
        self.assertEqual(self._book_repository.find_book(book_id), True)

    def test_redo_remove_book__one_book_redo_successfully(self):
        book_id = 1003
        self._services.remove_book(book_id)
        self._undo.undo()
        self._undo.redo()
        with self.assertRaises(RepositoryException):
            self._book_repository.find_book(book_id)

    def test_undo_update_book__one_book__undo_successfully(self):
        book_id = 1003
        new_book_id = 1010
        new_title = "Ion"
        new_author = "Liviu Rebreanu"
        book = self._services.get_book_from_id(book_id)
        self._services.update_book(book_id, new_book_id, new_title, new_author)
        self._undo.undo()
        self.assertEqual(self._services.get_book_from_id(book_id), Book(book_id, book.get_title, book.get_author))

    def test_redo_update_book__one_book__redo_successfully(self):
        book_id = 1003
        new_book_id = 1010
        new_title = "Ion"
        new_author = "Liviu Rebreanu"
        self._services.update_book(book_id, new_book_id, new_title, new_author)
        self._undo.undo()
        self._undo.redo()
        self.assertEqual(self._services.get_book_from_id(new_book_id), Book(new_book_id, new_title, new_author))

    def test_undo_add_client__one_client__undo_successfully(self):
        client_id = 1234
        name = "Tony Stark"
        self._services.add_client(client_id, name)
        self._undo.undo()
        with self.assertRaises(RepositoryException):
            self._client_repository.find_client(client_id)

    def test_redo_add_client__one_client__redo_successfully(self):
        client_id = 1234
        name = "Tony Stark"
        self._services.add_client(client_id, name)
        self._undo.undo()
        self._undo.redo()
        self.assertEqual(self._client_repository.find_client(client_id), True)

    def test_undo_remove_client__one_client__undo_successfully(self):
        client_id = 1003
        self._services.remove_client(client_id)
        self._undo.undo()
        self.assertEqual(self._client_repository.find_client(client_id), True)

    def test_redo_remove_client__one_client__redo_successfully(self):
        client_id = 1003
        self._services.remove_client(client_id)
        self._undo.undo()
        self._undo.redo()
        with self.assertRaises(RepositoryException):
            self._client_repository.find_client(client_id)

    def test_undo_update_client__one_client__undo_successfully(self):
        client_id = 1003
        new_client_id = 1010
        new_name = "Norman Osborn"
        client = self._services.get_client_from_id(client_id)
        self._services.update_client(client_id, new_client_id, new_name)
        self._undo.undo()
        self.assertEqual(self._services.get_client_from_id(client_id), Client(client_id, client.get_client_name))
