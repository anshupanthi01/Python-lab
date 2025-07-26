# WAP to test if a variable is a list, tuple or set.

a = [2,4,6,8]

if(type(a) == tuple):
    print("tuple")
    
elif(type(a) == list):
    print("list")

else:
    print("set")
    
