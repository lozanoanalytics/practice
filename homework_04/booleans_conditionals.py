""" Date: June 15, 2020 
    @Author: Ivan Lozano
    Filename: booleans_conditionals.py
    Purpose: Homework 4: Writing Booleans,
    If/Else Statements, and Nested If else Statements"""

# Prompt user for values for each of the variables
# (b1, b2, _a, _b, _c, _d, and _e) and store said 
# value into the variable (see sample output)

b1 = input ("What is the value (True or False) of b1?: ")  == "True"
b2 = input ("What is the value (True or False) of b2?: ") == "True"
_a = float (input ("What is the value (int/float) of _a?: ") )
_b = float (input ("What is the value (int/float) of _b?: ") )
_c = float (input ("What is the value (int/float) of _c?: ") )
_d = float (input ("What is the value (int/float) of _d?: ") )
_e = float (input ("What is the value (int/float) of _e?: ") )

print()

"""

   PART 1: BOOLEAN EXPRESSION PRACTICE
   Place your line of code UNDERNEATH the 
   instruction comment.  Follow the format I
   provide for you here, with the expression 
   as part of the string literal and in parentheses
   after the plus sign for concatenation
  
"""

# EXAMPLE
# Write an expression that is true if 
# b1 and b2 are BOTH true
print ("b1 and b2 is " + str(b1 and b2) )

# Write an expression that is true if 
# EITHER b1 OR b2 (or both) is true
print ("b1 or b2 is " + str(b1 or b2) )


# Write an expression that is true if
# b1 and b2 are BOTH false
print ("b1 and b2 are BOTH " + str(not b1 and not b2))


# Write an expression that is true if _a 
# is GREATER THAN _b
print ("_a is greater _b " + str(_a > _b) )

# Write an expression that is true if _c 
# and _e are NOT EQUAL
print ("_c is NOT equal to _e " + str(_c != _e) )


print ()

######################/
#
# PART 2: BASIC IF/ELSE STATEMENTS 
#
######################/

# EXAMPLE
# if b1 is true, print out: b1 is true!
if b1 == True: 
    print ("b1 is True!")

# if b2 is true, print out: b2 is true!
if b2 == True: 
    print ("b1 is True!")


# if at least one of b1 and b2 is true, print out: 
#      At least one, b1 or b2, is true!
# Otherwise, print out: b1 and b2 are BOTH false!
if b1 == True or b2 == True:
    print("At least one, b1 or b2, true")
else:
    print ("b1 and b2 are BOTH false!")

print ()

######################/
#
# PART 3: NESTED IF/ELSE STATEMENTS
# See example code below
#
######################/

# if _a is less than _b, print out: 
#     _a is less than _b
# if _a is less than _c as well, also print out: 
#     _a is less than _c, too!
# Otherwise, print out: 
#     _a may be less than _b, but it is greater than or equal to _c
#
# However, if _a is NOT less than _b, print out:
#     _a is greater than or equal to _b, but we don't know its relation to c
# In addition, if _a is less than _d, print out:
#     _a is less than _d

# YOUR CODE GOES HERE

if _a < _b:
    print ("_a is less than _b")
    if _a < _c:
        print("_a is less than _c, too!")
    else:
        print("_a may be less than _b, but it is greater than or equal to _c")
else:
    if not (_a < _b):
        print("_a is greater than or equal to _b, but we don't know its relation to _c")
    if _a < _d:
        print("_a is less than _d")


"""

EXAMPLE CODE

if _d is greater than or equal to _e, print out: 
    _d is greater than or equal to _e
if _d is also less than or equal to _c, also print out:
    _d is also less than or equal to _c

However, if _d is less than _e, print out:
    _d is less than _e
In addition, if _d is greater than _b, also print out: 
    ...but _d is greater than _b
Otherwise, also print out:
    ...and _d is less than or equal to _b


if _d >= _e:
    print ("_d is greater than or equal to _e")
    if _d <= _c:
        print ("_d is also less than or equal to _c")
else:
    print ("_d is less than _e")
    if _d > _b:
        print ("...but _d is greater than _b")
    else:
        print ("...and _d is less than or equal to _b")

"""