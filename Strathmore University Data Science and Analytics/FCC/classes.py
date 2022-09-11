'''
Strings: " "/''
Lists : []
Dictionaries: {}
Sets: ()
Tuples: ()
'''

# name = "Strathmore"

# print(name)
# Printing home from the word strathmore
# name = "Strathmore"
# print(name[5], name[7], name[6], name[-1])
# print(name[-2] + name[-3] + name[3] + name[-2])
# print(''.join([name[5], name[7], name[6], name[-1]]))

'''
Create a function that takes in the index numbers of letters and returns the word from these indices.
modify the function to take in an optional parameter (transform_to_lower) that true would transform the outputto lowercase
'''


# def create_names():
#     n = int(input("enter the number of letter"))
#     name = "strathmore"
#     for i in name:
#         print


# name = "Strathmore"
# def create_word(n1, n2, n3, n4, transform_to_lower = False):
#     word = name[n1] + name[n2] + name[n3] + name[n4]
#     if transform_to_lower:
#         return word.lower()
#     return word

# print(create_word(0, -3, 6, -1, transform_to_lower = True))


# # String operations
# print('boy'.upper()) # All uppercase
# print('boy'.capitalize()) # First letter Uppercase
# print('boy'. lower()) # All lowercase

# check = '5'

# print(check.isalpha()) # Check if text
# print(check.isdigit()) # Check if number

# /////////Lists//////// #
# basket = ['orange', 'apple', 'banana', 'mango','grapes', 'mango']
# print(type(basket))

# print(basket[1], basket[-4])

# o = basket[0]
# print(o[1:] + o[4:6])
# print(o[2] + o[-2:]) #age



'''
Using the variable basket as specified above: Create a function that takes in a list it returns all items
in the list that have less than 6 letters
'''

# def less_6():
#     n = 6
#     for i in basket:
#         if len(i) < n:
#             print(i)
#         else:
#             pass
#     return i

# print(less_6())

# def less_than_6(mylist):
#     output = []
#     for item in mylist:
#         if len(item) < 6:
#             output.append(item)
#     if len(output) > 0:
#         print("we found {} items".format(len(output)))
#         return output
#     else:
#         print("no items found")
#     return output
    
# b = less_than_6(basket)
# print(b)

# # Append
# basket.append('watermelon')
# basket.append('pineapple')
# basket.remove('banana')
# basket.pop(0)
# print(basket)

'''
Create a function that takes in two lists
1. List of student names (6)
2. List of student grades (6)

Your function should return the name of the student with the highest grade.
'''
names = ["John", "Ric", "Pete", "Mary", "Rio", "Job"]
grades = [100, 89, 97, 20, 50, 30]

print(max(grades))

def highest_grade(s_names, s_grades):
    # Find index of highest grades
    max_grade = max(s_grades)

    index_max = s_grades.index(max_grade)

    return s_names[index_max]

print(highest_grade(names, grades))
