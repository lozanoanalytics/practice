""" Date: June 15, 2020 
    @Author: Ivan Lozano
    Filename: student_registrations.py
    Purpose: Homework 5:  If/Else Statements, 
    and Nested If else Statements"""

import random
message_to_student = "(empty)"

name = input ("What is your name? ")
print()

student_ID = random.randint(1000000000, 9999999999)
print ("Your student id number is: " + str(student_ID))
print ()

major = input ("What is your major? ")
print()

print ("What school is this? \n1 = Engineering\n2 = Business\n(Or any other number for liberal arts)")
print()

school = int (input ("Please enter the number: "))
print()

"""
Depending on which school the student belongs to...
   *Ask the student the appropriate yes/no question
   *Depending on the student's response, assign the appropriate text string to the variable 
       message_to_student
   *DO NOT do any printing in this part of the program!  That part is taken care of by the LAST line of the program,
    which will print whatever is contained in the variable message_to_student.

For students in the Engineering school, ask if they have 
    started their engineering project yet.  If so, the 
    message is: "Good for you!  Keep me updated on your progress!"
    Otherwise:  "That's not good at all.  It's nearly November!"

For students in the Business school, ask if they have 
    found an internship yet.  If so, the 
    message is: "Congratulations!  I know you must have impressed 
                     the company quite a bit."
    Otherwise:  "You may be out of luck because most of the 
                     internships are probably gone by now."

For students in the Liberal Arts school, ask if they have 
    chosen a senior thesis topic yet.  If so, the 
    message is: "That sounds interesting, and I look forward to reading it."
    Otherwise:  "You're going to be under a huge time crunch, 
                     if you don't even have a topic by this point."
"""

# YOUR CODE GOES HERE

if school == 1:
    project = input("Have you started your engineering project yet (yes/no)? ")
    if project == "yes":
        message_to_student = "Good for you! Keep me updated on your progress!"
    else:
        message_to_student = "That's not good at all. It's nearly November!"
elif school == 2:
    internship = input("Have you found an internship yet(yes/no)? ")
    if internship == "yes":
        message_to_student = "Congratulations! I know you must have impressed the company quite a bit"
    else:
        message_to_student = "You may be out of luck because most of the internships are probably gone by now."
else:
    thesis = input("Have you chosen a senior topic yet (yes/no)? ")
    if thesis == "yes":
        message_to_student = "That sounds interesting, and I look forward to reading it."
    else:
        message_to_student = "You're going to be under a huge time crunch, if you don't even have a topic by this point."

print ()

print ("Our Message --:" + message_to_student)