class User:
    def __init__(self, name,):
        self.name = name        
        self.account = 0

    def make_deposit(self, amount):
        self.account +=amount
        return self

    def make_withdrawal(self,amount):
        self.account -=amount
        return self

    def display_user_balance(self):
        print(f"{self.name}, balance:{self.account_balance}")


ticara = User ("Ticara")

class BankAccount:

# don't forget to add some default values for these parameters!
    def __init__(self, balance,):
        self.balance = balance

    def make_deposit(self, amount):
        self.balance +=amount
        return self

    def display_user_balance(self):
        print(f"Balance:{self.balance}")

account_one = BankAccount()
account_two = BankAccount()

account_one.make_deposit(500).make_deposit(750).make_deposit(900).make_withdraw(2500)
account_one.display_user_balance ()

account_two.make_deposit(150).make_withdraw(830).make_withdraw(350).make_withdraw(700)
account_two.display_user_balance()


