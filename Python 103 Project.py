from datetime import datetime

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print(f'A {amount} Bank account has been deposited')
        print('The date and time', datetime.now())

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'A {amount} Bank account has been withdrawn')
            print('The date and time', datetime.now())
        else:
            print('The balance is not enough')

    def get_balance(self):
        return self.__balance

class PremiumAccount(BankAccount):
    def withdraw(self, amount):
        print('Premium account ')
        super().withdraw(amount)

user = PremiumAccount()
user.deposit(1350)
user.withdraw(500)
print('The current balance is :', user.get_balance())
