class BankAccount:

# don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance,):
        self.int_rate = int_rate
        self.balance = balance

    def make_deposit(self, amount):
        self.balance +=amount
        return self

    def make_withdraw(self,amount):
        if (self.balance - amount) >=0:
            self.balance -=amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_user_balance(self):
        print(f"Balance:{self.balance}")

    def yield_interest(self):
        self.balance += (self.balance*self.int_rate)
        return self

account_one = BankAccount(0.01,5000)
account_two = BankAccount(0.03, 1500)

account_one.make_deposit(500).make_deposit(750).make_deposit(900).make_withdraw(2500)
account_one.display_user_balance ()

account_two.make_deposit(150).make_withdraw(830).make_withdraw(350).make_withdraw(700)
account_two.display_user_balance()
