#define an employee class with attributes role,dept and sal.
#this class also has a showDetails method
#create an engineer class that inherits properties from employee and has additional attributes 
#name and age

class Employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal

    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("sal =",self.sal)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75000")

eng1=Engineer("sarvan","20")
eng1.showDetails()


