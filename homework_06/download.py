""" Date: July 11, 2020 
    @Author: Ivan Lozano
    Filename: download.py
    Purpose: Homework 6: Practicing  with For, While loops,
    and time modules"""

import random # for generating random values
import time   # for pausing execution
import sys    # needed for pausing component
              # to work

# Here, DELAY represents the pause length,
# in seconds, after each * is printed
#
# For example, 0.05 would be 50 milliseconds
#
# If you like, you can change the value of
# this constant to something else, though I
# would not go over 0.5.
DELAY = 0.05

count = 0      # Number files downloaded
answer = "yes" # User response to 
               # prompt to continue

# YOUR CODE STARTS HERE

variable = random.randint(10000000,100000000)
number = variable//1000000

while answer == "yes":
    print("Downloading a file of " + str(variable) + " bytes.")
    for i in range(number):
        print("* ", end="")
        sys.stdout.flush()
        time.sleep(DELAY)
    print("COMPLETE!")
    answer = input("Another file? (yes/no) ")
    variable = random.randint(10000000,100000000)
    number = variable//1000000
    count += 1

# YOUR CODE ENDS HERE

print ()
print ("You downloaded", count, "files, total.")