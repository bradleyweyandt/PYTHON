class BankAccount:
    balance = 0.00
    int_rate = .01
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

