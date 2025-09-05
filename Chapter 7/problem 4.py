n = int(input("Enter a number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Your number is not prime")
        break

else:
    print("Your number is prime")