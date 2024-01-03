# Function to swap two numbers
def swap_numbers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2

# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the numbers before swapping
print("Before swapping: num1 =", num1, ", num2 =", num2)

# Call the function to swap the numbers
num1, num2 = swap_numbers(num1, num2)

# Display the numbers after swapping
print("After swapping: num1 =", num1, ", num2 =", num2)
