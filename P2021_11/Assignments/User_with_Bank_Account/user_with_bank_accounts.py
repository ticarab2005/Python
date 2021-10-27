class BankAccount:

    accounts = []
    def __init__(self, int_rate, balance,):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

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
    
    def display_account_balance(self):
        return f"{self.balance}"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance*self.int_rate)
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.accounts:
            account.display_account_balance()
        
class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "savings" : BankAccount (0.03,2500),
            "checkings" : BankAccount (0.03,2500)
        }

    def display_user_balance(self):
        print(f"User: {self.name}, Savings Balance:{self.account['savings'].display_account_balance()}")
        print(f"User: {self.name}, Checkings Balance: {self.account['checkings'].display_account_balance()}")
        return self     


ticara = User ("Ticara")

ticara.account['checkings'].make_withdraw(430)
ticara.account['savings'].make_deposit(530).make_deposit(700).make_withdraw(925)
ticara.display_user_balance()
