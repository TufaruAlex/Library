from src.ui.ui import BookUI, UIException, ClientUI, RentalUI
from src.repository.repository import RepositoryException
from src.services.services import Services, ServicesException
from src.services.undo import Undo, UndoException
from src.settings.settings import Settings


def print_menu():
    print("1. Manage books")
    print("2. Manage clients")
    print("3. List books")
    print("4. List clients")
    print("5. List rentals")
    print("6. Rent a book")
    print("7. Return a book")
    print("8. Undo")
    print("9. Redo")
    print("10. Exit")


def print_book_menu():
    print("1. Add book")
    print("2. Remove book")
    print("3. Update book")
    print("4. Search book")
    print("5. Most rented books")
    print("6. Most rented authors")
    print("7. Back")


def print_client_menu():
    print("1. Add client")
    print("2. Remove client")
    print("3. Update client")
    print("4. Search client")
    print("5. Most active clients")
    print("6. Back")


class Menu:
    def __init__(self):
        book_repository, client_repository, rental_repository = Settings().get_all_repositories()
        undo = Undo()
        services = Services(book_repository, client_repository, rental_repository, undo)
        book_ui = BookUI(services)
        client_ui = ClientUI(services)
        rental_ui = RentalUI(services)
        while True:
            print_menu()
            user_option = input("Enter option: ").strip()
            if user_option == '1':
                while True:
                    print_book_menu()
                    user_option = input("Enter option: ").strip()
                    if user_option == '7':
                        break
                    elif user_option == '1':
                        try:
                            book_ui.add_book_ui()
                        except ServicesException as uie:
                            print(str(uie))
                        except RepositoryException as re:
                            print(str(re))
                    elif user_option == '2':
                        try:
                            book_ui.remove_book_ui()
                        except ServicesException as uie:
                            print(str(uie))
                        except RepositoryException as re:
                            print(str(re))
                    elif user_option == '3':
                        try:
                            book_ui.update_book_ui()
                        except ServicesException as uie:
                            print(str(uie))
                        except RepositoryException as re:
                            print(str(re))
                    elif user_option == '4':
                        try:
                            book_ui.search_book()
                        except UIException as uie:
                            print(str(uie))
                    elif user_option == '5':
                        book_ui.most_rented_books_ui()
                    elif user_option == '6':
                        book_ui.most_rented_authors_ui()
                    else:
                        print("Invalid option")
            elif user_option == '2':
                while True:
                    print_client_menu()
                    user_option = input("Enter option: ").strip()
                    if user_option == '6':
                        break
                    elif user_option == '1':
                        try:
                            client_ui.add_client_ui()
                        except ServicesException as uie:
                            print(str(uie))
                        except RepositoryException as re:
                            print(str(re))
                    elif user_option == '2':
                        try:
                            client_ui.remove_client_ui()
                        except ServicesException as uie:
                            print(str(uie))
                        except RepositoryException as re:
                            print(str(re))
                    elif user_option == '3':
                        try:
                            client_ui.update_client_ui()
                        except ServicesException as uie:
                            print(str(uie))
                        except RepositoryException as re:
                            print(str(re))
                    elif user_option == '4':
                        try:
                            client_ui.search_client()
                        except UIException as uie:
                            print(str(uie))
                    elif user_option == '5':
                        client_ui.most_active_clients_ui()
                    else:
                        print("Invalid option")
            elif user_option == '3':
                try:
                    book_ui.list_books()
                except UIException as uie:
                    print(str(uie))
            elif user_option == '4':
                try:
                    client_ui.list_clients()
                except UIException as uie:
                    print(str(uie))
            elif user_option == '5':
                try:
                    rental_ui.list_rentals()
                except UIException as uie:
                    print(str(uie))
            elif user_option == '6':
                try:
                    rental_ui.rent_book_ui()
                except ServicesException as uie:
                    print(str(uie))
                except RepositoryException as re:
                    print(str(re))
            elif user_option == '7':
                try:
                    rental_ui.return_book_ui()
                except RepositoryException as re:
                    print(str(re))
                except ServicesException as se:
                    print(str(se))
            elif user_option == '8':
                try:
                    undo.undo()
                except UndoException as ue:
                    print(str(ue))
            elif user_option == '9':
                try:
                    undo.redo()
                except UndoException as ue:
                    print(str(ue))
            elif user_option == '10':
                return
            else:
                print("Invalid option")


menu = Menu()
