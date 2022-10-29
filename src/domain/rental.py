from datetime import date


class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date="not returned"):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    @property
    def get_rental_id(self):
        return self.__rental_id

    def set_rental_id(self, new_rental_id):
        self.__rental_id = new_rental_id

    @property
    def get_book_id(self):
        return self.__book_id

    def set_book_id(self, new_book_id):
        self.__book_id = new_book_id

    @property
    def get_client_id(self):
        return self.__client_id

    def set_client_id(self, new_client_id):
        self.__client_id = new_client_id

    @property
    def get_rented_date(self):
        return self.__rented_date

    def set_rented_date(self, new_rented_date):
        self.__rented_date = new_rented_date

    @property
    def get_returned_date(self):
        return self.__returned_date

    def set_returned_date(self, new_returned_date):
        self.__returned_date = new_returned_date

    def __len__(self):
        if self.__returned_date != "not returned":
            return (self.__returned_date - self.__rented_date).days + 1
        return (date.today() - self.__rented_date).days + 1

    def __str__(self):
        if self.__returned_date != "not returned":
            return "Rental: " + str(self.__rental_id) + "\nBook: " + str(self.__book_id) + "\nClient: " + str(
                self.__client_id) + "\nPeriod: " + self.__rented_date.strftime("%Y-%m-%d") + " to " + \
                   self.__returned_date.strftime("%d-%m-%Y")
        else:
            return "Rental: " + str(self.__rental_id) + "\nBook: " + str(self.__book_id) + "\nClient: " + str(
                self.__client_id) + "\nPeriod: " + self.__rented_date.strftime("%d-%m-%Y") + " to be returned"
