
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number "))
print("choose your operator" + "+, /, -, *")
num3 = input()
if num1 == 45 and num2 == 3 and num3 == '*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == "+":
    print("77")
elif num1 == 56 and num2 == 6 and num3 == "/":
    print("4")
elif num1 == 56 and num2 == 6 and num3 == "-":
    print("4")
elif num3 == "*":
    num4 = num1 * num2
    print(num4)
elif num3 == "+":
    plus = num1 + num2
    print(plus)
elif num3 == "-":
    minus = num1 - num2
    print(minus)
elif num3 == "/":
    divide = num1 / num2
    print(divide)
else:
    print("Error! please check your input")
#  NO OF GUESSES 5 OR 9 ****** PRINT NO GUESSES LEFT ***********GAME OVER


