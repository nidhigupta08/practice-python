#unpacking A TUPLES

coordinates=(1,2,3)
result=coordinates[0]+ coordinates[1]+ coordinates[2]
print(result)
### OOOOOOOOOOOOOORRRRRRRRRRRR
X=coordinates[0]
Y=coordinates[1]
Z=coordinates[2]
result=X+Y+Z
print(result)

# #OOOOOOOOOOORRRRRRRRRRRRR        we are unpacking the coordinates one by one.

X,Y,Z=coordinates         # we have assign tuple "coordinates"
print(X)
print(Y)
print(Z)

#unpacking A LIST

coordinates=[1,2,3]
X,Y,Z=coordinates         # we have assign tuple "coordinates"
print(X)
print(Y)
print(Z)

#DICTIONARIES-  mutable. a collection of key-value pairs. values can be any data type.

customer={
    "name":"nidhi gupta",
    "age": 21,
    "email":"nidhi@gmail.com",
    "is_verified":True
}
print(customer["name"])
customer["name"]="gupta"  #updating the name
print(customer["name"])
#
#get()  return the value of the item with the specified key.
print(customer.get("birth_date", "March 8th 2003"))

customer["birthdate"]="March 8th 2003 "
print(customer)

# program to take input phone number and converted to words?
user_phone=input("enter your phone number: ").split()
dict={

    "1" :"one", "2":"two","3":"three"," 4":"four","5":"five", "6":"six", "7":"seven","8":"eight", "9":"nine", "0":"zero"
}
output=""
for ch in user_phone:
    output+=dict.get(ch,"!") + " "
print(output)

# OUTPUT
# enter your phone number: 5 2 12 6
# five two ! six

#OOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

user_inputs = input("Enter multiple inputs, separated by spaces: ").split()
key_value_dict = {

"1" :"one", "2":"two","3":"three"," 4":"four","5":"five", "6":"six", "7":"seven","8":"eight", "9":"nine", "0":"zero"
}

for user_input in user_inputs:
  if user_input in key_value_dict:
    print(key_value_dict[user_input])
  else:
    print("Key not found")


message=input(">")
words=message.split(" ")
emojis={
    ":)":"😀", ":(": "😔", ":D":"😁 ",":O":"😲",":')":"😂"
}
output=""
for word in words:
    output+=emojis.get(word,word) + " "
print(output)
