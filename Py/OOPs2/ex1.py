#class method,is bound to the cls and recives the class as an implicit 1st argument
#static method cant access or modify class state or genrally for utility

class Person:
    name="anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("sarvan")
print(p1.name)
print(Person.name)