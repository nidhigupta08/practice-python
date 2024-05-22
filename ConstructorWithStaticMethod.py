class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @staticmethod
    def from_fahrenheit(fahrenheit):
        return Temperature((fahrenheit - 32) * 5/9)

    def display(self):
        print(f"{self.celsius:.2f}°C / {self.to_fahrenheit():.2f}°F")

# Creating an instance of Temperature from Celsius
temp1 = Temperature(25)
temp1.display()

# Creating an instance of Temperature from Fahrenheit
temp2 = Temperature.from_fahrenheit(77)
temp2.display()
