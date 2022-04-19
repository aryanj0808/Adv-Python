class Emp:       #Parent class
    company="Youtube"

    def getdata(self):
        print("This is class Parent")
class Emp1(Emp):    #Derived class 1
    def getdata(self):
        print("This is class Derived1")


class programmer(Emp1):      #Derived class 2
    def getdata(self):
      
        print("This is class Derived2")
        super().getdata()                  #super() method shows parent class data of same named fun here parent class is Derived class 1

a=Emp()       #Parent class object 
a.getdata()

b=Emp1()
b.getdata()

c=programmer() #Derived class object
c.getdata()      

