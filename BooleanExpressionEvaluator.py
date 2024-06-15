def evaluate_boolean_expression(expr):
    try:
        # Evaluate the expression and print the result
        result = eval(expr)
        print(f"The result of the expression '{expr}' is: {result}")
    except Exception as e:
        print(f"Invalid expression: {e}")

# Example usage:
expression = input("Enter a Boolean expression (e.g., 'True and False or not True'): ")
evaluate_boolean_expression(expression)
