name="John Smith"
age=20
is_new=True

name=input("enter a your name: ")
fav_color=input("WHt is your favriote color?")
print(name + " likes " +fav_color )

birth_year=int(input("enter the birth year"))
current_year=int(input("enter the current year"))
result=(current_year-birth_year)
print(f"my name is Nidhi Gupta and i m {result} years old")

weight_lbs=input('weight in lbs: ')
weight_kg= float(weight_lbs) * 0.45  # int
print(weight_kg)


print(
    '''
    Hi,
    My name is nidhi gupta. i m a recent graduate passout student with bechelor degree in computer applicater.

    Thanks

    '''
)
print("""
My name  is a  Nidhi Gupta.
i am a fresher of BBACA
""")

phone_number = input("Enter a phone number: ")
phone_number_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

phone_number_in_words = " "
for digit in phone_number:
    phone_number_in_words += phone_number_dict[int(digit)] + " "

print(phone_number_in_words)