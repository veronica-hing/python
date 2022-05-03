class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        #increases user's balance by amount specified
        self.account_balance += amount

    def make_withdrawal(self, amount):
        #decrease user's balance by amount specified
        self.account_balance -= amount

    def display_user_balance(self):
        #prints user name and account balance to terminal
        print(f"{self.name} {self.account_balance}")
        
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

betty = User("Betty Boop", "betty@boop.com")
annie = User("Annie Ok", "annie_r_u_ok@helpmail.com")
stacy = User("Stacy Mom", "gotItGoing@onmail.com")

##make first user do 3 deposits and 1 withdrawal
betty.display_user_balance()
betty.make_deposit(300)
betty.make_deposit(30)
betty.make_deposit(9)
betty.make_withdrawal(89)
betty.display_user_balance()

##make second user do 2 deposits and 2 withdrawals
annie.make_deposit(2222)
annie.make_deposit(77)
annie.display_user_balance()

##make third user do 1 deposit and 3 withdrawals

stacy.make_deposit(9999)
stacy.make_withdrawal(66)
stacy.make_withdrawal(300)
stacy.make_withdrawal(33)
stacy.display_user_balance()

## stacy transfers money to annie

stacy.transfer_money(annie, 600)
stacy.display_user_balance()
annie.display_user_balance()