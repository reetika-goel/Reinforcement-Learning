# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:34:04 2019

@author: jahan
"""

from Circle import Circle

def main():
# Create a circle with radius 1
    circle1 = Circle()
    print("The area of the circle of radius", circle1.radius, "is", circle1.getArea() )

# Create a circle with radius 25
    circle2 = Circle(25)
    print("The area of the circle of radius", circle2.radius, "is", circle2.getArea() )


# Create a circle with radius 125
    circle1 = Circle(125)
    print("The area of the circle of radius", circle2.radius, "is", circle2.getArea() )

# modify circle2 radius, two ways to do it
    circle2.radius = 100
    circle2.setRadius(111)
    print("The area of the circle of radius", circle2.radius, "is", circle2.getArea() )
    
main()