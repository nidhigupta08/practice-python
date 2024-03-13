def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    temperature = float(input("Enter the temperature: "))
    choice = input("Enter 'C' for Celsius to Fahrenheit conversion, 'F' for Fahrenheit to Celsius conversion: ").upper()

    if choice == 'C':
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"{temperature} Celsius is equal to {converted_temperature} Fahrenheit.")
    elif choice == 'F':
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"{temperature} Fahrenheit is equal to {converted_temperature} Celsius.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
