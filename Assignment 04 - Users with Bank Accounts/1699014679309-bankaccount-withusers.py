class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insuffiecient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance:{self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self

account1 = BankAccount(0.02, 1000)
account2 = BankAccount(0.03, 500)

account1.deposit(200).deposit(300).deposit(400).withdraw(100).yield_interest().display_account_info()
account2.deposit(100).deposit(200).withdraw(50).withdraw(75).withdraw(100).withdraw(75).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
         self.account.withdraw(amount)
         return self
    def display_user_balance(self):
         print(self.name)
         self.account.display_account_info()
         return self
user3 = User("Brradley", "bw@gmail.com")
user3.make_deposit(100).make_deposit(250)
print(user3.account.balance)

user4 = User("Jordan", "jj@gmail.com")
user4.make_deposit(1000).display_user_balance().make_withdrawal(450).display_user_balance()