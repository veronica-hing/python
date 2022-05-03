class BankAccount:
    #class attribute
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0, acc_type = "checking"): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        self.acc_type = acc_type
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        #add amount to balance
        self.balance += amount
        return self

    def withdraw(self, amount):
        # deduct amount from balance if balance is available. else deduct 5$ fee
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Account Type: {self.acc_type}")
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        # increases balance by balance* interest rate if balance is greater than 0
        if self.balance > 0:
            self.balance *= (1+ self.int_rate)
        return self
    ##class method to print all instances of a Bank Account's info
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

##create the two accounts
"""betty = BankAccount(.01,500)
letty = BankAccount(.02,800)

##chain 3 deposits and 1 withdrawal then yield then display account info
betty.deposit(22).deposit(88).deposit(333).withdraw(50).yield_interest().display_account_info()

##chain 2 deposits 4 withdrawals then yeild then display
letty.deposit(999).deposit(888).withdraw(22).withdraw(44).withdraw(111).withdraw(93).yield_interest().display_account_info()

print("Calling class method to display all accounts")
BankAccount.all_balances()"""