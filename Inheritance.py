class Emp:       #Parent class
    company="Youtube"

    def showdetail(self):
        print("This is class Emp")

class programmer(Emp):      #Derived class 
    def getdata(self):
        print("This is class programmer")

a=Emp()       #Parent class object 

b=programmer() #Derived class object

b.getdata()      #Calling derived class method
b.showdetail()   #Calling parent class method