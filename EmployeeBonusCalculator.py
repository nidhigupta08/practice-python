class Employee:
    def calculate_bonus(self):
        pass

class Manager(Employee):
    def calculate_bonus(self, salary):
        return salary * 0.15

class Developer(Employee):
    def calculate_bonus(self, salary):
        return salary * 0.10

# Usage
manager = Manager()
print("Bonus for manager with salary $5000:", manager.calculate_bonus(5000))

developer = Developer()
print("Bonus for developer with salary $4000:", developer.calculate_bonus(4000))
