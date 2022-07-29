
# Python program to illustrate 
# function with main
# Using Pyton modules/libraries
import math
def getInteger():
    result = int(input("Enter integer: "))
    return result
def getProduct(num):
    product = num*5
    print("Your Integer %s multiplied by 5 is: "%num,product)
def Main():
    print("Started")

    # calling the getInteger function and 
    # storing its returned value in the output variable
    output = getInteger()     
    print(output)
    getProduct(output)
    # fabs is used to get the absolute 
    # value of a decimal
    num = output
    num = math.fabs(num) 
    print("Absolute Value of your intger is: ",num)

# now we are required to tell Python 
# for 'Main' function existence
if __name__=="__main__":
    Main()
