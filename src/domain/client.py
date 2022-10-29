class Client:
    def __init__(self, client_id, client_name):
        self.__client_id = client_id
        self.__client_name = client_name

    @property
    def get_client_id(self):
        return self.__client_id

    def set_client_id(self, new_client_id):
        self.__client_id = new_client_id

    @property
    def get_client_name(self):
        return self.__client_name

    def set_client_name(self, new_client_name):
        self.__client_name = new_client_name

    def __str__(self):
        return "ID: " + str(self.__client_id) + ", name: " + self.__client_name

    def __eq__(self, other):
        return self.__client_id == other.__client_id
