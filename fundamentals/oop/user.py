from bank_account import BankAccount
##importing the class from bank_account file so no copy and pasting

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        #everyone starts with a checking account
        self.accounts = {"checking" : BankAccount(int_rate=0.02, balance = 0)}

    def make_deposit(self, amount, acc_name ="checking"):
        #increases user's balance by amount specified
        self.accounts[acc_name].deposit(amount)
        return self

    def make_withdrawal(self, amount, acc_name = "checking"):
        #decrease user's balance by amount specified
        self.accounts[acc_name].withdraw(amount)
        return self

    def display_user_balance(self):
        #prints user name and account balance to terminal
        print(f"{self.name} Accounts:")
        for key_name in self.accounts:
            self.accounts[key_name].display_account_info()
        return self
        
    def transfer_money(self, amount, dep_to_user, dep_to_acc_name = "checking", withdraw_acc_name = "checking"):
        #default to draw from checking account to deposit only to dep_to_user's checking
        self.make_withdrawal(amount, withdraw_acc_name)
        dep_to_user.make_deposit(amount, dep_to_acc_name)
        return self
    
    def add_account(self, new_acc_name, new_int_rate = 0.01, new_balance = 0):
        self.accounts[new_acc_name] = BankAccount(new_int_rate, new_balance, new_acc_name)
        return self

betty = User("Betty Boop", "betty@boop.com")
annie = User("Annie Ok", "annie_r_u_ok@helpmail.com")
stacy = User("Stacy Mom", "gotItGoing@onmail.com")

"""
##make first user do 3 deposits and 1 withdrawal
#betty.display_user_balance()
betty.make_deposit(300).make_deposit(30).make_deposit(9).make_withdrawal(89).display_user_balance()
betty.make_deposit(30)
betty.make_deposit(9)
betty.make_withdrawal(89)
#betty.display_user_balance()

##make second user do 2 deposits and 2 withdrawals
annie.make_deposit(2222).make_deposit(77).make_withdrawal(99).make_withdrawal(32).display_user_balance()
annie.make_deposit(77)
annie.make_withdrawal(32)
annie.make_withdrawal(99)
annie.display_user_balance()

##make third user do 1 deposit and 3 withdrawals

stacy.make_deposit(9999).make_withdrawal(66).make_withdrawal(300).make_withdrawal(33).display_user_balance()
stacy.make_withdrawal(66)
stacy.make_withdrawal(300)
stacy.make_withdrawal(33)
#stacy.display_user_balance()

## stacy transfers money to annie

stacy.transfer_money(annie, 600).display_user_balance()
annie.display_user_balance()
annie.add_account("savings", new_balance=300)
"""

betty.make_deposit(1000)
annie.make_deposit(1000)
stacy.make_deposit(1000)

betty.add_account("savings", new_balance=200)
betty.display_user_balance()
betty.transfer_money(50,stacy, "checking", "savings")
betty.display_user_balance()
betty.transfer_money(25,betty,"savings","checking")#can target yourself
betty.display_user_balance()
betty.transfer_money(200, annie)#can target friend and default transfers to checking accounts
annie.display_user_balance()
betty.display_user_balance()
