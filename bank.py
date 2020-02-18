from bank_account import BankAccount

class Bank:
    def __init__(self, accounts):
        self.__accounts = accounts
        self.deposit = deposit

    def withdraw(self,bank_account_number, amount, secret_password):
        if len(bank_account_number) == 10:
            account = self.__accounts.get(bank_account_number)

            if account is None:
                raise Exception("Account does not exist.")

            if account.customer.check_password(password) is False:
                raise Exception("Wrong password")

        else:
            raise Exception("Invalid accounts number")
        
        account.withdraw(amount)

    def deposit(bank_account_number, amount):
        if len(bank_account_number) == 10:
            account = self.__accounts.get(bank_account_number)

            if account is None:
                raise Exception("Account does not exist.")

            if account.customer.check_password(password) is False:
                raise Exception("Wrong password")

        else:
            raise Exception("Invalid accounts number")
        
        account.deposit(amount)

    def transfer(from_bank_account_number,to_bank_account_number, amount, secret_password):
        if len(from_bank_account_number) == 10:
            account = self.__accounts.get(bank_account_number)
            if account is None:
                raise Exception("Account does not exist.")

            if account.customer.check_password(password) is False:
                raise Exception("Wrong password")
        
        else:
            raise Exception("Invalid accounts number")

        if len(to_bank_account_number) == 10:
            account = self.__accounts.get(bank_account_number)
            if account is None:
                raise Exception("Account does not exist.")
        
        account.transfer(amount)