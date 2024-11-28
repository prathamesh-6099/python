#Create a class “Programmer” for storing information of few programmers 
 #working at Microsoft
class Programmer:
    company="microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

pratham=Programmer("prathamesh", "50LPA", "410501")
print("name=",pratham.name)
print("salary=", pratham.salary)
print("pin code", pratham.pin)