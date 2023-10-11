def C_3_D(list1):
    for n in list1:
        if n in range(100, 1000):
            return n
        else:
            pass


result = C_3_D([12,1234,333, 456, 78, 65])
print(result)