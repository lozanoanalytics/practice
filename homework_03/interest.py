""" Date: June 15, 2020 
    @Author: Ivan Lozano
    Filename: interest.py
    Purpose: Homework 3: Calculating compounding interest over time  """

import math

P = 8000.0
r = .065
t = 7.0
n = 4.0

##  A(t) = the compounded amount of your investment at time t
comp_amt_t = P*math.pow((1 +(r/n)),n*t)

print ("The initial investment is " + str(P) + " dollars.")
print ("The interest rate is " + str(r*100) + " percent per year.")
print ("There are " + str(n) + " compounding periods in a year.")
print ("The time frame is " + str(t) + " years.")
print ("After that time, you will have " + str(comp_amt_t) + " dollars.")