import math
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self,x):
        self.x=x
        print("the area of the circle",math.pi*x*x)

    def perimeter(self,x):
        self.x=x
        print("the perimeter of the circle",2*math.pi*x)


class Circle(Shape):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self,x):
        self.x=x
        print("the area of the circle",math.pi*x*x)

    def perimeter(self,x):
        self.x=x
        print("the perimeter of the circle",2*math.pi*x)   

obj=Shape(2,3)
obj.area(2)
obj.perimeter()

obj1=Circle(4,5)
obj1.area(4)
obj1.perimeter()
