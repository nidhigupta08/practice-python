class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance is ${self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn ${amount}. Current balance is ${self.balance}.")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")


# Creating an instance of the BankAccount class
account1 = BankAccount("123456", 1000)

# Accessing methods of the BankAccount instance
account1.get_balance()
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)
account1.get_balance()
