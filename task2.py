#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""

num = input("Input a random number :")

num = float(num)

if num > 0:
    print(num,"is a positive!")
elif num < 0:
    print(num,"is a negative")
else: 
    num == num
    print(num,"is a 0")

#done