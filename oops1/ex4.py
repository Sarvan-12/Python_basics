#abstraction
#hiding the implementation details of a class and only showing the essential features to the user 
#encapsulation
#wrapping data and functions into a single unit(object)
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True      #unneccasry impletation hide,only necessary details show,abstraction
        print("car started")

car1=Car()
car1.start()



