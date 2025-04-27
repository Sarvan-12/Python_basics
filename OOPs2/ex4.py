#define a circle class to create a circle with radius r using constructor
#defne an Area() method of the class which cal the area of circle
#define a Perimeter() method of the class which allowas u to cal the perimeter of the circle 

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
    
c1=Circle(7)
print(c1.area())
print(c1.perimeter())
