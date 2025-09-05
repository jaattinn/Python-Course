def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c
    
a = int(input("Enter your number = "))
b = int(input("Enter your number = "))
c = int(input("Enter your number = "))

print(greatest(a, b, c))