class BankAccount:
    def __init__(self):
        self._balance = 0  

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount} Birr. New Balance: {self._balance} Birr")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}Birr. New Balance: {self._balance} Birr")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: {self._balance} Birr")

account = BankAccount()
account.deposit(1000)
account.withdraw(500)
account.display_balance()

import unittest

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount()
        account.deposit(500)
        self.assertEqual(account._balance, 500)

    def test_withdraw(self):
        account = BankAccount()
        account.deposit(1000)
        account.withdraw(300)
        self.assertEqual(account._balance, 700)

    def test_insufficient_funds(self):
        account = BankAccount()
        account.deposit(200)
        account.withdraw(300)
        self.assertEqual(account._balance, 200)

    def test_invalid_deposit(self):
        account = BankAccount()
        account.deposit(-100)
        self.assertEqual(account._balance, 0)

if __name__ == '__main__':
    unittest.main()
