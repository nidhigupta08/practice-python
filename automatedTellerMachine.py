class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        print("Your balance is: ${}".format(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("${} deposited successfully.".format(amount))
        self.check_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("${} withdrawn successfully.".format(amount))
            self.check_balance()

# Creating an instance of the ATM class
atm = ATM()

# ATM interface loop
while True:
    print("\nWelcome to the ATM!")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        atm.check_balance()
    elif choice == '2':
        amount = float(input("Enter amount to deposit: $"))
        atm.deposit(amount)
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: $"))
        atm.withdraw(amount)
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
