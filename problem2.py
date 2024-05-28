#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

import numbers

num = input("Please input a random number! :")

if num.isdecimal():
	print("The number is an integer!")
else:
	print("The number is not an integer!")




#done