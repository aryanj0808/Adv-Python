class emp:
    def __init__(self,name,prn,salary) -> None: #initiating Constructor
        print("Employee is created")
        self.name=name
        self.prn=prn
        self.salary=salary
    
    def getDetails(self):
        print(f"Name of Emp is {self.name}")
        print(f"prn of Emp is {self.prn}")
        print(f"salary of Emp is {self.salary}")

# emp1=emp()  this show error
emp1=emp("Aryan",1909,2500) #We have to pass 3 argu cuz constructor contain 3 argu
emp1.getDetails()

