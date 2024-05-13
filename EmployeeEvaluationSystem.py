class Employee:
    def evaluate_performance(self):
        pass

class Manager(Employee):
    def evaluate_performance(self, projects_completed):
        if projects_completed > 10:
            return "Excellent performance!"
        elif projects_completed > 5:
            return "Good performance."
        else:
            return "Needs improvement."

class Developer(Employee):
    def evaluate_performance(self, lines_of_code_written):
        if lines_of_code_written > 10000:
            return "Excellent performance!"
        elif lines_of_code_written > 5000:
            return "Good performance."
        else:
            return "Needs improvement."

# Usage
manager = Manager()
print("Manager performance evaluation:", manager.evaluate_performance(12))

developer = Developer()
print("Developer performance evaluation:", developer.evaluate_performance(8000))
