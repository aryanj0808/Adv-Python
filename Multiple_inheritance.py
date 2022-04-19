class Emp:       #Parent class
    company="Youtube"

    def showdetail(self):
        print("This is class Parent derived in class derived 1")

    def showdetail1(self):
        print("This is class Parent derived in class derived 2")

class Emp1(Emp):    #Derived class 1
    def getdata(self):
        print("This is class Derived 1")


class programmer(Emp):      #Derived class 2 
    def getdata1(self):
        print("This is class Derived 2")

a=Emp()       #Parent class object 
b=Emp1()
c=programmer() #Derived class object

b.showdetail()   #Calling parent class method from derived class 1
c.showdetail1()  #Calling parent class method from derived class 1

b.getdata()      #Calling derived class 1 method
c.getdata1()      #Calling derived class 2 method
