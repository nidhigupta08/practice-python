class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id            # Public attribute
        self.name = name                # Public attribute
        self.position = position        # Public attribute
        self.__salary = salary          # Private attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary amount!")

    def display_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.get_salary()}")

# Creating an Employee object
employee = Employee("E123", "John Doe", "Manager", 75000)

# Displaying employee details
employee.display_employee_details()
# Output:
# Employee ID: E123
# Name: John Doe
# Position: Manager
# Salary: $75000

# Setting new salary
employee.set_salary(80000)
employee.display_employee_details()
# Output:
# Employee ID: E123
# Name: John Doe
# Position: Manager
# Salary: $80000
