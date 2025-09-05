u = int(input("Enter your number : "))

for i in range(u, u*11, u):
    if(i>u*10):
        break
    print(i)

# for i in range(1, 11):
#     print(f"{u} X {i} = {u * i}")