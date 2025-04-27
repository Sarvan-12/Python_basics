#del keyword,used to delete object properties or object itself
class Student:     
    clg_name="SMVITM"
    def __init__(self,name,marks):   
        self.name=name
        self.__marks=marks    #privite,__ means its private ,it cannot be accessed
    def get_marks(self):
        return self.__marks     #it can be called inside the class
    
s1=Student("sarvan",[100,81,80])
print(s1.name)
del s1.name
#print(s1.name)    #error
#print(s1.__marks)    #error
print(s1.get_marks())