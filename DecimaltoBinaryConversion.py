def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

decimal_num = 15
binary_num = decimal_to_binary(decimal_num)
print("Binary equivalent:", binary_num)
