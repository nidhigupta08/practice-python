def check_even_odd(num):
    if num & 1 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Input an integer
num = int(input("Enter an integer to check if it's even or odd: "))

# Call the function to check even or odd
check_even_odd(num)
