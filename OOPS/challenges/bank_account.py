class MinimumBalanceError(Exception):
    pass

class Account:
    AccNumber = 1001

    def __init__(self, name, balance):
        if balance<1000:
            raise MinimumBalanceError('Account cannot be created')
        self.name = name
        self.balance = balance
        self.account_number = Account.AccNumber
        Account.AccNumber+=1

    def deposit(self,amt):
        self.balance+=amt

    def withdraw(self,amt):
        if self.balance - amt < 1000:
            raise MinimumBalanceError('Amount cannot be withdrawn')

    def show_details(self):
        print(f'Account Number: {self.account_number}')
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')

a1 = Account('John', 2000)
a1.show_details()

print('')
a1.deposit(1000)

a1.show_details()
"""
    These will throw error
    # a1.withdraw(2500)
    # a2 = Account('Doe',800) 
"""
