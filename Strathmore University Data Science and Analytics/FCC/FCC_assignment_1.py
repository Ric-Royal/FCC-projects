# Richard Kabiru 150684 - Assignment 1
# Import libraries
import math
# Prompt the user to enter the value of x and reject non integer values
try:
    x = int(input("Enter a number x: "))
    print("The value of x is: ", x)
except ValueError:
    print("The value of x is not an integer.")

# Prompt the user to enter the value of y and reject non integer values
try:
    y = int(input("Enter a number y: "))
    print("The value of y is: ", y)
except ValueError:
    print("The value of y is not an integer.")

# Using the inbuilt function pow print out x raised to the power y
print("x power y is:", pow(x, y))
 
# Calculate the log base 2 of x using the math library. 
# If the value of x is less than 1, prompt the user to enter a positive integer value.
try:
    z = math.log2(x)
    print("The log base 2 of x: ", z)
except ValueError:
    print("Math domain error. Try a positive integer value for x.")
