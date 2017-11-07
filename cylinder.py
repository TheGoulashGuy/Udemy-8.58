#!/usr/bin/python

class Cylinder(object):
    def __init__(self,  height,  radius):
        self.height = height
        self.radius = radius
    
    def volume(self):
        volume = (3.14159)*(self.radius**2)*(self.height)
        print("The volume is " + str(volume) + " units.")
    
    def surface_area(self):
        lateral = 2*3.14159*self.radius*self.height
        total = lateral + 2*3.14159*self.radius**2
        print("The surface area is " + str(total) + " units.")
cylinderHeight = input("Enter the height of the cylinder: ")
cylinderRadius = input("Enter the radius of the cylinder: ")
cylinder = Cylinder(cylinderHeight,  cylinderRadius)
cylinder.volume()
cylinder.surface_area()
