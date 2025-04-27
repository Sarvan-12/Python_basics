#inheritence,when one class derives the properties and methods of another class

#single lvl inheritence

class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
print(car1.name)
print(car1.start())
print(car1.color)


    