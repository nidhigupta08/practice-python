class Employee:
    company_name = "Tech Corp"  # Class variable

    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Company: {Employee.company_name}")

# Creating instances of the Employee class
emp1 = Employee(101, "Alice", "Engineering")
emp1.display_info()

emp2 = Employee(102, "Bob", "Marketing")
emp2.display_info()
