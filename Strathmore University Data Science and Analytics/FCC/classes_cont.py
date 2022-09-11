'''
29/07/2022
Recap:
1. Strings
2. indexing
3. Lists
4. Appending
5. Pop
6. index

Dictionaries: {}
Sets : set(), {}
Tuples : ()
'''


names = ['A', 'B', 'C', 'B', 'D']

set_names = set(names)
print(type(set_names))

# To access an item in a set we can 
# 1. USE A FOR LOOP
# 2. Convert set into a list and use index to locate it
#print(set_names[0])

# Tuples
# A tuple is immutable
# a = tuple((1, 2, 3, 4, 5))

# print(a)
# print(a[0])
# print(type(a))

# Dictionaries
# Object mapped using a key and value

# dict_results = {
#     'names' : ['john', 'Jane', 'Kevin', 'Rachel'],
#     'grades' : [89, 90, 77, 76]
# }

# print(dict_results['names'])


# Exercise 1: Loops, Dictionaries, Function
'''
1. Create a list of 1000 students names  "Student {number}" using a for loop
2. Create a list of random scores between 0 and

'''
import random
names = []
n = 0
for i in range(1, 1001):
    n = "student {}". format(i)
    names.append(n)

print(names)

student_score = []
m = 0
for i in range(1, len(names)):
    score = random.randint(0,100)
    student_score.append(score)

print(student_score)


# Function
def grade():

    if student_score >= 80 and student_score <= 100:
        grades = print("A")
    elif student_score >= 70 and student_score <= 79:
        grades = print("B")
    elif student_score >= 60 and student_score <= 69:
        grades = print("C")
    elif student_score >= 50 and student_score <= 59:
        grades = print("D")
    elif student_score >= 0 and student_score <= 49:
        grades = print("E")

    return grades

#print(grade())

grades = []

for x in student_score:
    student_grade = grade(x)
    grades.append(student_grade)

print(grades[:5])

class_list = []

for x in names:
    index_name = names.index(x)
    info_dict = {
        'name' : x,
        'score' : score(index_name),
        'grades' : grades
    }
