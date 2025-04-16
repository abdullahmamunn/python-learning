# Create a BankAccount class with: owner and balance attributes

# Methods:
# deposit(amount)
# withdraw(amount)
# show_balance()
# Make sure the withdraw() method checks if the balance is sufficient.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"Account created for {self.owner} with initial balance: {self.balance}")

    
    def deposit(self, amount):
        if amount >= 500:
            self.balance +=amount
            print(f"Congrats! {self.owner}, Deposited {amount}tk")
        else:
            print(f"Sorry, Sir deposite amount must be greater then 500 or more")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance! pleae withdraw {self.balance} or less")
        else:
            if amount < 500:
                print("Sorry Sir, withdraw amount must be 500 or greater")
                return
            self.balance -= amount
            print(f"Mr. {self.owner}, You withdrew {amount}")
    
    def show_balance(self):
        print(f"Mr.{self.owner}, Your current balance is {self.balance}")



abdullah = BankAccount("Abdullah", 500)
abdullah.deposit(500)
abdullah.show_balance()
abdullah.deposit(1500)
abdullah.show_balance()
abdullah.withdraw(500)
abdullah.show_balance()
abdullah.withdraw(2000)
abdullah.show_balance()
abdullah.withdraw(2000)
abdullah.show_balance()

# output:
# Account created for Abdullah with initial balance: 500
# Congrats! Abdullah, Deposited 500tk
# Mr.Abdullah, Your current balance is 1000
# Congrats! Abdullah, Deposited 1500tk
# Mr.Abdullah, Your current balance is 2500
# Mr. Abdullah, You withdrew 500
# Mr.Abdullah, Your current balance is 2000
# Mr. Abdullah, You withdrew 2000
# Mr.Abdullah, Your current balance is 0


