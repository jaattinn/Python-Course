class employee:
    language = "Py" #This a class attribute 
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}, And the salary is {self.salary}")
    
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        
Jatin = employee("Jatin", 1300000, "Javascript")

print(Jatin.name, Jatin.salary, Jatin.language)