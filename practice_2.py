# Working with functions in python
# Function for checking the divisibility
# Notice the indentation after function declaration
# and if and else statements
def checkDivisibility(a, b):
    if a % b == 0 :
        print ("%s is divisible by "%a,b)
    else:
        print ("%s is not divisible by "%a,b)
#Driver program to test the above function
checkDivisibility(9, 3)
checkDivisibility(10, 3)
checkDivisibility(13, 3)