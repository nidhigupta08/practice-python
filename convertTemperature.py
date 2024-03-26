class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        return TemperatureConverter.celsius_to_kelvin(celsius)

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)

# Taking input for temperature value and unit
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

# Converting temperature to Celsius
if unit == 'C':
    celsius_temp = temperature
elif unit == 'F':
    celsius_temp = TemperatureConverter.fahrenheit_to_celsius(temperature)
elif unit == 'K':
    celsius_temp = TemperatureConverter.kelvin_to_celsius(temperature)
else:
    print("Invalid temperature unit entered.")
    exit()

# Converting Celsius temperature to other units
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
kelvin_temp = TemperatureConverter.celsius_to_kelvin(celsius_temp)

# Displaying results
print("Temperature in Celsius:", celsius_temp)
print("Temperature in Fahrenheit:", fahrenheit_temp)
print("Temperature in Kelvin:", kelvin_temp)
