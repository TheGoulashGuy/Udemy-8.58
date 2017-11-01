#!/usr/bin/python

import cmath

class Line(object):
    
    def __init__(self,  coor1,  coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        self.coor1 = list(self.coor1)
        self.coor2 = list(self.coor2)
        sum_of_squares = ((self.coor2[0]-self.coor1[0])**2) + ((self.coor2[1]-self.coor1[1])**2)
        distance = cmath.sqrt(sum_of_squares)
        distance = str(distance)
        print(distance + " units")
        
    def slope(self):
        self.coor1 = list(self.coor1)
        self.coor2 = list(self.coor2)
        rise = float(self.coor2[1]-self.coor1[1])
        run = float(self.coor2[0]-self.coor1[0])
        slope = (rise / run)
        slope = str(slope)
        print(slope + " units")
coordinate1 = (33,  4)
coordinate2 = (57,  12)
result = Line(coordinate1, coordinate2)
result.distance()
result.slope()
