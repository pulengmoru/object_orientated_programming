from bank_account import BankAccount
from bank import Bank

class Customer:
    def __init__(self, secret_password):
        self.__secret_password = secret_password

    def set_password(self, new_password):
        self.__secret_password = new_password

    def check_password(self, password):
        self.__secret_password = password
        if password != secret_password
            raise Exception("password invalid")

        else:
            if password == secret_password
            return ("password correct")