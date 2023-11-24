def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number > limit:
            break
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

# Input the limit from the user
limit = int(input("Enter the limit for Fibonacci sequence: "))

# Generate and display Fibonacci numbers up to the limit
fibonacci_numbers = generate_fibonacci(limit)
print("Fibonacci sequence up to", limit, ":", fibonacci_numbers)
