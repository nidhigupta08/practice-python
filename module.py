def lbs_to_kg(weight):
    return  weight *0.45

def kg_to_lbs(weight):
    return weight / 0.45

def find_max(num1):
    max=num1[0]
    for numbers in num1:
        if numbers>max:
            max=numbers
    return max

