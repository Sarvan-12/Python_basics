#multi lvl inheritence
class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("diesel")
car1.start()