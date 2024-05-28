#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a obtuse triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""

import math

a = float(input("Please input a number for the 1st side of a triangle: "))
b = float(input("Please input a number for the 2nd side of a triangle: "))
c = float(input("Please input a number for the 3rd side of a triangle: "))

a2 = pow(a,2)
b2 = pow(b,2)
c2 = pow(c,2)

hyp = max(a2,b2,c2)

if c2 == hyp:
    if a2 + b2 > c2:
        print('that is a acute triangle')
    if a2 + b2 == c2:
        print('that is a right triangle')
    if a2 +b2 < c2:
        print('that is a obtuse triangle')

if b2 == hyp:
    if a2 + c2 > b2:
        print('that is a acute triangle')
    if a2 + c2 == b2:
        print('that is a right triangle')
    if a2 +c2 < b2:
        print('that is a obtuse triangle')

if a2 == hyp:
    if c2 + b2 > a2:
        print('that is a acute triangle')
    if c2 + b2 == a2:
        print('that is a right triangle')
    if c2 +b2 < a2:
        print('that is a obtuse triangle')


#done







