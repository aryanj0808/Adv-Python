class emp:
    def simple(self):
        print("Hello Everyone")
# If we do not write self parameter it shows error
# We have to write '@staticmethod' to get output of without parameter function  

    @staticmethod
    def simple1():
        print("Hello Everyone")


emp1=emp()

emp1.simple()
emp1.simple1()
