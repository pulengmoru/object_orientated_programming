class BankAccount:

    def __init__(self, interest, balance, monthly_fee, customer):
        self.interest = interest
        self.balance = balance
        self.monthly_fee = monthly_fee
        self.customer = customer

    def finish_month(self):
        interest = (self.balance*self_interest)/12
        self.balance = self.balance + interest - self.monthly_fee
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

