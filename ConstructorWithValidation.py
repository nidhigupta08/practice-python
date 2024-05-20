class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}")

# Creating instances of the BankAccount class
account1 = BankAccount("123456789", 1000.50)
account1.display_info()

# The following will raise a ValueError
# account2 = BankAccount("987654321", -500)
# account2.display_info()
