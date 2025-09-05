n = int(input("Enter your number : "))
if n<1:
    print("You entered invalid value")

else:   
     for i in range(2, n+1):
         if(n%i== 0):
            print("Your number is not prime")
            break
     else:
         print("Your number is prime")
