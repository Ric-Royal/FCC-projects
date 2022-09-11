'''
a) Create a list of 100 students whose records will be stored in this format:
{
    "name" : "Alice",
    "homework" : [100.0, 92.0, 98.0, 100.0],
    "quizzes" : [82.0, 83.0, 91.0],
    "tests" : [89.0, 97.0]
}

NOTE:
- The numbers should be randomly generated between 30 and 95
- The students names should all be unique

b)create a function that can return the student with the highest average grade
given either the argument of homework, quizzes, tests. {output: student Name : Marks}
c)The average score of the top n students given the argument of homework, quizzes, tests
    (output[Student name - Average, .......])

'''
# import random

# student_names = []
# n = 0
# for i in range(1, 101):
#     n = "student {}". format(i)
#     student_names.append(n)

# print(student_names)

# homework = []
# m = 0
# for i in range(1, len(student_names)):
#     score = random.randint(30,95)
#     homework.append(score)

# print(homework)

# quizzes = []
# m = 0
# for i in range(1, len(student_names)):
#     score = random.randint(30,95)
#     homework.append(score)

# print(homework)

# def student_highest_grade(homework, quizzes,tests):



import random
# Create 100 records
def random_list(n):
    store = []
    for x in range(1, n+1):
        store.append(float(random.randint(30,95)))

    return store


list_100 = []
for n in range(0,101):
    list_100.append(
        {
            "name": "Student {}".format(n), # [random.randint(30,95) for n in range(0,n)]
            "homework" : random_list(4), # [random.randint(30,95) for n in range(0,4)]
            "quizzes": random_list(3), # [random.randint(30,95) for n in range(0,3)]
            "tests" : random_list(2) # [random.randint(30,95) for n in range(0,2)]
        }
    )

print(list_100[:2])

# print([random.randint(30,95) for n in range(0,4)])

'''
b)create a function that can return the student with the highest average grade
given either the argument of homework, quizzes, tests. {output: student Name : Marks}
'''

# for i in list_100:
#        homework_score = sum(list_100.homework) / 4
#        quizzes_score = sum(list_100.quizzes) / 3
#        tests_score = sum(list_100.tests) / 2

# print(tests_score)


# # def average_score(list_100): #homework, quizzes, test
#     for i in list_100:
#        homework_score = sum(list_100.homework) / 4
#        quizzes_score = sum(list_100.quizzes) / 3
#        tests_score = sum(list_100.tests) / 2

#     return homework_score, quizzes_score, tests_score
def calc_average(items):
    return sum(items)/len(items)
list_100_avg = list_100

for x in range(0, len(list_100_avg)):
   list_100_avg[x]['homework'] = calc_average(list_100_avg[x]['homework'])
   list_100_avg[x]['quizzes'] = calc_average(list_100_avg[x]['quizzes'])
   list_100_avg[x]['tests'] = calc_average(list_100_avg[x]['tests'])

print(list_100_avg[:3])