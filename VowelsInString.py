string = "hello"
vowels = 'aeiou'
count = sum(1 for char in string if char.lower() in vowels)
print("Number of vowels:", count)
