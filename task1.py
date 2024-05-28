#! python3

"""
Have the user input a number. 
Determine if the number is larger than 100 
If it is, the output should read "The number is larger than 100" 
(2 points)
Inputs:
number
Outputs:
"The number is larger than 100"
"The number is smaller than 100"
"The number is 100"

Example:
Enter a number: 100
The number is 100

Enter a number: 102
The number is larger than 100
"""

num = input("Input a random number: ")

num = float(num)

if 100 < num:
    print(num,"is greater than 100!")
elif 100 > num:
    print(num,"is NOT greater than 100!")
else: 
    100 == 100
    print(num,"is 100")

#done