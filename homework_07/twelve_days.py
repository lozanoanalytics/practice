""" Date: July 16, 2020 
    @Author: Ivan Lozano
    Filename: twelve_days.py
    Purpose: Homework 7: Practicing tuples
    and for loops """

"""
Write an application that prints the verses 
to "The Twelve Days of Christmas".  For example, if 
the user chooses to print all 12 verses, then the 
12th verse will look like this: 

        On the 12th day of Christmas, my true love sent to me:
        Twelve Drummers Drumming
        Eleven Pipers Piping
        Ten Lords a Leaping
        Nine Ladies Dancing
        Eight Maids a Milking
        Seven Swans a Swimming
        Six Geese a Laying
        Five Golden Rings
        Four Calling Birds
        Three French Hens
        Two Turtle Doves
        and a Partridge in a Pear Tree

"""

import time

lines = ( "Twelve Drummers Drumming",
          "Eleven Pipers Piping",
          "Ten Lords a Leaping",
          "Nine Ladies Dancing",
          "Eight Maids a Milking",
          "Seven Swans a Swimming",
          "Six Geese a Laying",
          "Five Golden Rings",
          "Four Calling Birds",
          "Three French Hens",
          "Two Turtle Doves",
          "and a Partridge in a Pear Tree" ) 

days = int(input("How many days should we do? (1 to 12): "))
if not (1 <= days <= 12):
    print("Days must be between 1 and 12.  Defaulting to 6.")
    days = 6

# Loop through the days, from the first
# until the number specified by the user
# NOTE: You may want to process Day 1 
# differently than the following days

# YOUR CODE STARTS HERE

days_name = ["1st",
             "2nd",
             "3rd",
             "4th",
             "5th",
             "6th",
             "7th",
             "8th",
             "9th",
             "10th",
             "11th",
             "12th"]

for day in range (1, days + 1):
    print ("On the " + days_name[day - 1] + " day of Christmas, my true love gave to me:")
    if day == 1:
        print ("A partridge in a Pear Tree")
    else:
        for i in range (-day, 0):
            print (lines[i])
    print()

# YOUR CODE ENDS HERE