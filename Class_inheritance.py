class Emp:
    salary=200

    def changesalary(self,salary):
        # self.salary=salary
        self.__class__.salary=salary #Assigning new salary value in class attribute
        print(salary)

e=Emp()
print(e.salary) #Class Attribute

e.changesalary(455) #Function  Attribute

print(e.salary) #Class Attribute
