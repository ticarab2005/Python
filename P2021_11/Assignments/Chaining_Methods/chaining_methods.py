class User:
    def __init__(self, name,):
        self.name = name        
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance +=amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -=amount
        return self

    def display_user_balance(self):
        print(f"{self.name}, balance:{self.account_balance}")


ticara = User ("Ticara")
antonette = User("Antonette")
sparkle = User("Sparkle")

ticara.make_deposit(900).make_deposit(700).make_deposit(850).make_withdrawal(830).make_withdrawal(830)
antonette.make_deposit(2500).make_deposit(1500).make_withdrawal(500).make_withdrawal(1000)
sparkle.make_deposit(1500).make_withdrawal(500).make_withdrawal(750).make_withdrawal(400)

ticara.display_user_balance()
antonette.display_user_balance()
sparkle.display_user_balance()