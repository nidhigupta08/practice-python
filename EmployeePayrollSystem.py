class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_pay(self):
        return self.salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, hourly_rate)
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.salary * self.hours_worked


# Usage
full_time_employee = FullTimeEmployee("John", 50000)
print("Full-time employee pay:", full_time_employee.calculate_pay())

part_time_employee = PartTimeEmployee("Alice", 20, 25)
print("Part-time employee pay:", part_time_employee.calculate_pay())
