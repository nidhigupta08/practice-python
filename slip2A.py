def string_fun(str):
    dic1={"UPPER_CASE":0, "LOWER_CASE":0}
    for i in str:
        if i.isupper():
           dic1["UPPER_CASE"]+=1
        elif i.islower():
           dic1["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", str)
    print ("No. of Upper case characters : ", dic1["UPPER_CASE"])
    print ("No. of Lower case Characters : ", dic1["LOWER_CASE"])

string_fun('The quick Brown Fox')