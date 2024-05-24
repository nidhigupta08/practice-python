class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number    # Public attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount!")

    def get_balance(self):
        return self.__balance

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.get_balance()}")

# Creating a BankAccount object
account = BankAccount("123456789", 1000)

# Depositing money
account.deposit(500)
account.display_account_details()
# Output:
# Account Number: 123456789
# Balance: 1500

# Withdrawing money
account.withdraw(300)
account.display_account_details()
# Output:
# Account Number: 123456789
# Balance: 1200
