class Patient:
    def __init__(self, patient_id, name, age, diagnosis):
        self.patient_id = patient_id     # Public attribute
        self.name = name                 # Public attribute
        self.age = age                   # Public attribute
        self.__diagnosis = diagnosis     # Private attribute

    def get_diagnosis(self):
        return self.__diagnosis

    def set_diagnosis(self, diagnosis):
        if diagnosis:
            self.__diagnosis = diagnosis
        else:
            print("Invalid diagnosis!")

    def display_patient_details(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Diagnosis: {self.get_diagnosis()}")

# Creating a Patient object
patient = Patient("P001", "Jane Doe", 28, "Flu")

# Displaying patient details
patient.display_patient_details()
# Output:
# Patient ID: P001
# Name: Jane Doe
# Age: 28
# Diagnosis: Flu

# Setting new diagnosis
patient.set_diagnosis("Allergy")
patient.display_patient_details()
# Output:
# Patient ID: P001
# Name: Jane Doe
# Age: 28
# Diagnosis: Allergy
