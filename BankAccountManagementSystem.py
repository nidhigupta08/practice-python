class Account:
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def calculate_interest(self, balance):
        return balance * 0.05

class FixedDepositAccount(Account):
    def calculate_interest(self, balance):
        return balance * 0.08

# Usage
savings_account = SavingsAccount()
print("Interest for savings account:", savings_account.calculate_interest(1000))

fixed_deposit_account = FixedDepositAccount()
print("Interest for fixed deposit account:", fixed_deposit_account.calculate_interest(10000))
