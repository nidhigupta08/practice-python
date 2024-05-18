class Employee:
    def calculate_benefits(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_benefits(self, salary):
        return salary * 0.2

class PartTimeEmployee(Employee):
    def calculate_benefits(self, hourly_rate, hours_worked):
        return hourly_rate * hours_worked * 0.05

# Usage
full_time_employee = FullTimeEmployee()
print("Benefits for full-time employee with salary $5000:", full_time_employee.calculate_benefits(5000))

part_time_employee = PartTimeEmployee()
print("Benefits for part-time employee with hourly rate $15 and 40 hours worked:", part_time_employee.calculate_benefits(15, 40))
