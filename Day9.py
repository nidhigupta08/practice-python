#Exception
try:
    age=int(input('age:'))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("age cannot be 0")
except ValueError:       # it happens when u pass str in place of int value
    print("Invalid value")
