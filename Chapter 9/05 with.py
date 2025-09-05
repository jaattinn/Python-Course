f = open("D:\Python\Code With Harry Python\Chapter 9\jatin.txt")
print(f.read())
f.close()

#the same can be written using with statement like this:

with open("D:\Python\Code With Harry Python\Chapter 9\jatin.txt") as f:
    print(f.read())

# you dont have to close the file