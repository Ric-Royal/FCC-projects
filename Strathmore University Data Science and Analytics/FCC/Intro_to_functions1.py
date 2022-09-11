'''
Types of functions
- Built in functions (print, float, int, input
- User defined functions (def)
- Anonymous functions (Lambda functions)
'''
# # len - gets the value of the container
# v = len('strathmore')
# print(v)

# # Min 
# m = min(1,4,6,8,0)
# print(m)

'''
def name(input parameters):
    Body/Action to be performed by the function
    return output *provides output for future use*
'''

# def summation(num1, num2):
#     result = num1 + num2
#     return result

# r = summation(2,3)
# print(r)

# def summation(num1, num2):
#     result = num1 + num2
#     #print(result)
#     #return result

# summation(2,3)

# def summation(num1, num2):
#     #result = num1 + num2
#     return num1 + num2

# r = summation(2,3)
# print(r)

'''
Exercise 1: Grading system
Create a function that given an input of marks given an output of grade
A 
'''











'''
Exercise 2: Grading system
Consider three vehicles travelling to different locations. 
Details of their journey is given below:

Car A - 118 Km : 89 Km/h
Car B - 75 miles: 90 Km/h
Car C - 50 Km : 40 miles/h

Which vehicle arrived at its destination last?
Required:
Create a single function that takes in inputs of distance 
and speed and return the time taken in hours and minutes.

HINT: Your function should consider the units of the input.
'''
# car_a = calc_time(118, 89)
# car_b = calc_time(75, 90, km = False)
# car_b = calc_time(50, 40, km_hr = False)
# print('Time take \n Car A: {}, \n Car B: {}, \n'. format(
#     car_a, car_b, car_c))
# def measure(dist_unit, spd):
#     dist_unit = input("Enter k for Kilometres and m for miles:")
#     spd_unit = int("Enter the speed of the vehicle:")
# def measure():
#     dist_unit= int(input("k for km and m for miles"))
#     dist= int(input("Enter the distance the vehicle has covered:"))
#     spd = int(input("Enter the speed of the vehicle:"))
#     time = dist / spd
#     if dist_unit = k:
#         calc
#     return time

# t_time = measure()
# print(t_time, "hours")
######### Example 1: Equation of a straight line #########
# y = mx + c

# def calc_y(m,x,c):
#     output = m * x + c
#     return output



# y1 = calc_y(1,2,4)
# y2 = calc_y(1,3,4)
# print(y1, y2)


# def calc():
#     m = int(input("enter m:"))
#     x = int(input("enter x:"))
#     c = int(input("enter x:"))
#     output = m * x + c
#     return output

# def calc_c(x, c add_5 = False, m = 0.5):
#     if add_5 == True:
#         c = c+5

# Solution
# def calc_time(distance, speed, km = False, km_hr = True):
#     if km == True:
#         distance = distance * 1.6
#     if km == False:
#         speed = speed * 1.6

#     time = distance / speed
#     hours = int(time)
#     minutes = int((time - hours) * 60)
#     return "{}hrs {}min".format(hours,minutes)

# t = calc_time(90, 60)
# print(t)

# car_a = calc_time(118, 89)
# car_b = calc_time(75, 90, km = False)
# car_c = calc_time(50, 40, km_hr = False)
# print('Time take \n Car A: {}, \n Car B: {}, \n Car C: {}, \n'. format(
#     car_a, car_b, car_c))




# # Lambda Function
# sum_custom = lambda x,y: x+y
# x = sum_custom(1,2)
# print(x)

cmpnd_interest = lambda amt, tm, rt : amt * (1+rt/100) ** tm
y = cmpnd_interest(100,1,10)

print(y)