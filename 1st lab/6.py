# WAP to check whether a variable id an integer or string or float.

a = 5.6

if(type(a) == str):
    print(type(a))
    print("string")

elif(type(a) == int):
    print(type(a))
    print("Integer")

elif(type(a) == float):
    print(type(a))
    print("Float")
