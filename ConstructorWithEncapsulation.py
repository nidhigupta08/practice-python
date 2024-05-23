class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.__balance:.2f}")

# Creating an instance of the BankAccount class
account = BankAccount("123456789", 500)
account.display_info()

# Performing transactions
account.deposit(150)
account.withdraw(100)
account.display_info()
