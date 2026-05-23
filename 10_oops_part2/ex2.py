#property method

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property           #it can be updated later after any changes 
    def percentage(self):
        return (self.chem+self.phy+self.math)/3
    
s1=Student(80,81,100)
print(s1.percentage)
s1.phy=96
print(s1.percentage)
