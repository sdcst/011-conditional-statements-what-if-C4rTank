#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# There are many ways to solve this problem
# Hint: One method is to use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

import math

num1 = input("Please input a random number! :")

num1 =int(num1)

num2 = num1/2

num2 =str(num2)

if num1 == 0:
    print("The number is a 0!")
elif ".0" in num2:
    print("The number",num1,"is EVEN!")
else:
    print("The number",num1,"is ODD!")

#done

