from bank_account import BankAccount
##importing the class from bank_account file so no copy and pasting

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account = BankAccount(int_rate=0.02, balance = 0)

    def make_deposit(self, amount):
        #increases user's balance by amount specified
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        #decrease user's balance by amount specified
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        #prints user name and account balance to terminal
        self.account.display_account_info()
        return self
        
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

betty = User("Betty Boop", "betty@boop.com")
annie = User("Annie Ok", "annie_r_u_ok@helpmail.com")
stacy = User("Stacy Mom", "gotItGoing@onmail.com")

##make first user do 3 deposits and 1 withdrawal
betty.display_user_balance()
betty.make_deposit(300).make_deposit(30).make_deposit(9).make_withdrawal(89).display_user_balance()
#betty.make_deposit(30)
#betty.make_deposit(9)
#betty.make_withdrawal(89)
#betty.display_user_balance()

##make second user do 2 deposits and 2 withdrawals
annie.make_deposit(2222).make_deposit(77).make_withdrawal(99).make_withdrawal(32).display_user_balance()
#annie.make_deposit(77)
#annie.make_withdrawal(32)
#annie.make_withdrawal(99)
#annie.display_user_balance()

##make third user do 1 deposit and 3 withdrawals

stacy.make_deposit(9999).make_withdrawal(66).make_withdrawal(300).make_withdrawal(33).display_user_balance()
#stacy.make_withdrawal(66)
#stacy.make_withdrawal(300)
#stacy.make_withdrawal(33)
#stacy.display_user_balance()

## stacy transfers money to annie

stacy.transfer_money(annie, 600).display_user_balance()
annie.display_user_balance()