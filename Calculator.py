def calculate():
    # Get user input for numbers and operation
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform the operation based on the chosen operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    # Print the result
    print(f"The result is: {result}")

# Run the calculator loop
while True:
    print("\nSimple Calculator")
    calculate()

    # Ask the user if they want to perform another calculation
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != 'y':
        print("Exiting the calculator. Goodbye!")
        break
