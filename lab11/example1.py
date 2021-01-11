import math

class Cylinder:

    def __init__(self,radius,height):
        self.radius = radius
        self.height = height

    def setRadius(self,radius):
        self.radius = radius

    def setHeight(self,height):
        self.height = height

    def getRadius(self,radius):
        return self.radius

    def getHeight(self,height):
         return  self.height

    def calculate_base_area(self):
        return math.pi * self.radius ** 2
    def calculate_surface_area(self):
        return 2 * math.pi * self.radius *self.height


    def calculate_volume(self):
        return self.calculate_base_area() * self.height

    def calculate_area(self):
        base_area = self.calculate_base_area()
        surface_area = self.calculate_surface_area()
        area = 2 * base_area + surface_area
        return area

cylinder1 = Cylinder(2,10)
print(cylinder1.calculate_base_area())
print(cylinder1.calculate_volume())