class AccountBalanceException(Exception):
    def __init__(self):
        self.msg = 'Minimum balance should be 5000'
    def __str__(self):
        return self.msg

balance = 10000
def withdraw(amt):
    global balance
    if balance - amt < 5000:
        raise AccountBalanceException
    else:
        return balance - amt

try:
    balance = withdraw(2000)
    print(f"Remaining balance: {balance}")
except AccountBalanceException as e:
    print(e)

try:
    balance -= withdraw(9000)
    print(f"Remaining balance: {balance}")
except AccountBalanceException as e:
    print(e)

