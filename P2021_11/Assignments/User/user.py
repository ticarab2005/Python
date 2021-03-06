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

ticara.make_deposit(900)
ticara.make_deposit(700)
ticara.make_deposit(850)
ticara.make_withdrawal(830)
ticara.display_user_balance()

antonette.make_deposit(3500)
antonette.make_deposit(1500)
antonette.make_withdrawal(500)
antonette.make_withdrawal(1000)
antonette.display_user_balance()

sparkle.make_deposit(1500)
sparkle.make_withdrawal(500)
sparkle.make_withdrawal(400)
sparkle.make_withdrawal(750)
sparkle.display_user_balance()


