""" Date: June 15, 2020 
    @Author: Ivan Lozano
    Filename: ellipse.py
    Purpose: Homework 3: Programming a mathematical equation  """

import math

A = 10.0
B = 3.0
THETA = 2.9

print ("The horiontal semi-axis A is " + str(A) + " units.")
print ("The vertical semi-axis B is " + str(B) + " units.")
print ("The angle THETA is " + str(THETA) + " radians.")

### Math calculation for the radius math equation

rad_ellipse = (A * B) / math.sqrt(
    math.pow(A, 2) * math.pow(math.sin(THETA), 2)
    + math.pow(B, 2) * math.pow(math.cos(THETA), 2)
)

print("The radius (at " + str(THETA) + " radians) is " + str(rad_ellipse) + " units")

