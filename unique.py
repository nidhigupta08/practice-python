print('Enter 5 numbers..')

a=list()
for i in range(5):

   a.append(int(input('Enter: ')))

print("Entered list is:", a)
print(['Unique.','DUPLICATES.'][len(set(a))!=len(a)])