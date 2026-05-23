#create a student class that takes name and marks of 3 sub as arguments in constructor .
#then create a method to print avg
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(self.name,"'s avg marks is",sum/3)
s1=Student("sarvan",[100,81,80])
s2=Student("sinchana",[99,82,85])
s1.get_avg()
s2.get_avg()

#we can change the name and marks
s1.name="Sharvan"
s1.marks=[100,96,80]
s1.get_avg()