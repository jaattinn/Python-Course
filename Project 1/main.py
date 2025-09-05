import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")

youDict = {"r" : 1, "p" : -1, "s" : 0}
reverseDict =  {1 : "Rock", -1 : "Paper", 0 : "Scissors"}



if youstr not in youDict:
    print("Your entered wrong!")
else:
    you = youDict[youstr]

    print (f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
    
    if(computer == you):
        print("It's a draw!")
    else:
        if(computer == 1 and you == 0):
            print("You lose!")
        elif(computer == 1 and you == -1):
            print("You win!")
        elif(computer == -1 and you == 1):
            print("You lose!")
        elif(computer == -1 and you == 0):
            print("You win!")
        elif(computer == 0 and you == -1):
            print("You lose!")
        elif(computer == 0 and you == 1):
            print("You win!")
        else:
            print("Something went wrong!")