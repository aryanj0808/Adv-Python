class Emp:       #Parent class
    company="Youtube"

    def showdetail(self):
        print("This is class Parent")
class Emp1(Emp):    #Derived class 1
    def getdata(self):
        print("This is class Derived1")


class programmer(Emp1):      #Derived class 2
    def getdata1(self):
        print("This is class Derived2")

a=Emp()       #Parent class object 
b=Emp1()
c=programmer() #Derived class object
c.showdetail()   #Calling parent class method
c.getdata()      #Calling derived class method
c.getdata1()      #Calling derived class method
