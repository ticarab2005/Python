
from User.user import User


class BankAccount:

# don't forget to add some default values for these parameters!
    def __init__(self, balance, int_rate = 0.5):
        self.int_rate = int_rate
        self.balance = balance

    def make_deposit(self, amount):
        self.balance +=amount
        return self

    def make_withdraw(self,amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -=amount
        else:
            print("Insufficient Funds")
        return self

    def display_user_balance(self):
        print(f"{self.name}, balance:{self.balance}")

    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        return self



    @classmethod
    def all_balance(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum


