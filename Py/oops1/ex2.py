#constructor,all class have a funct called __init__(),which is always exicuted when the object is being initiated
class Student:     
    clg_name="SMVITM"
    def __init__(self,fullname,marks):   #self is must
        #print(self)      #same as print(s1)
        self.name=fullname
        self.marks=marks
        print("adding new student to the database")
    #methods
    def welcome(self):
        print("welcome student",self.name)
    def get_marks(self):
        return self.marks
    @staticmethod
    def hello():
        print("hello")

s1=Student("sarvan",100)
print(s1.name,s1.marks)
s2=Student("athul",88)
print(s2.name,s2.marks)
print(s1.clg_name)
print(Student.clg_name)
s1.welcome()
print(s1.get_marks())
s1.hello()


