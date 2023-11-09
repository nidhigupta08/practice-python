petName = 'Rocky'  # Global variable

def myFunction():
    global fruit
    fruit = 'apple'  # Considered global
    print(type(petName).__name__ + '- My pet name is ' + petName)

myFunction()

print(type(petName).__name__ + '- My pet name is ' + petName + ' Fruit name is ' + fruit)
