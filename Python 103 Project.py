from datetime import datetime

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):     # Define a method to deposit money into the account
        self.__balance += amount
        print(f'A {amount} Bank account has been deposited')
        print('The date and time', datetime.now())

    def withdraw(self, amount):
        if amount <= self.__balance:    # Check that the withdrawal amount does not exceed the balance
            self.__balance -= amount
            print(f'A {amount} Bank account has been withdrawn')
            print('The date and time', datetime.now())
        else:                                            # Run this block if the balance is insufficient
            print('The balance is not enough')

    def get_balance(self):        # Define a method to retrieve the current balance
        return self.__balance     # Return the current balance 

class PremiumAccount(BankAccount):     # Create a premium account class that inherits from BankAccount
    def withdraw(self, amount):        # Override the withdraw method to demonstrate polymorphism
        print('Premium account')
        super().withdraw(amount)       # Call the withdraw method from the parent class

user = PremiumAccount()            # Create an object from the PremiumAccount class
user.deposit(1350)
user.withdraw(500)
print('The current balance is :', user.get_balance())
