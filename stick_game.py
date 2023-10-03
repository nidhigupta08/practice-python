from random import shuffle
# initial test

sticks = ['|', '||', '|||', '||||', '|||||', '||||||', '|||||||']

# mixing sticks

def mix(my_list):
    shuffle(my_list)
    return (my_list)


# choose numbers
def try_your_luck():
    a_try = ' '
    while a_try not in ['1', '2', '3', '4', '5','6','7']:
        a_try = input("Choose a number:")
    return int(a_try)


#check players try
def verify_try(a_list, a_try):
    if a_list[a_try-1]=='|':
        print("Wash the dishes😁😅😭")
    elif a_list[a_try-1]=='|||':
        print("Clean the bathroom😂😂😂")
    elif a_list[a_try-1]=='|||||':
        print("Laundry time 😁😁😅")
    else:
        print('You are safe this time')
        print(f'You got {a_list[a_try-1]}')


#calling all the function
mixed_sticks=mix(sticks)
selection=try_your_luck()
verify_try(mixed_sticks, selection)