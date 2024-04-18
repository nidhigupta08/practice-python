def find_largest_number(numbers):
    if not numbers:
        print("List is empty.")
        return

    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    print("The largest number in the list is:", max_number)

# Main program
def main():
    # Get input from the user
    numbers_str = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(x) for x in numbers_str.split()]

    # Find and print the largest number
    find_largest_number(numbers)

if __name__ == "__main__":
    main()
