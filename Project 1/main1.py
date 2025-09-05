import random

computer = random.choice([1, 0])
youstr = input("Enter your choice: ")

coinDict = {"Heads" : 1, "Tails" : 0}
reverseCoin = {1 : " Heads", 0 : "Tails"}


if youstr not in coinDict:
    print("Your entered wrong!")
else:
    you = coinDict[youstr]
    if(computer == you):
        print(f"Its {reverseCoin[computer]}, You win!")
    else:
        print(f"Its {reverseCoin[computer]}, You lose!")
