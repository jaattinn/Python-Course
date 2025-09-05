class employee:
    language = "Py" #This a class attribute 
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}, And the salary is {self.salary}")
 

Jatin = employee()

Jatin.getInfo()
