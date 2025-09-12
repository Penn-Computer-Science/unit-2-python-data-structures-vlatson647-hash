
grades_ryan = {"ryan1": "23", "ryan2": "76", "ryan3": "78"}
# print(grades_ryan)

grades_mary = {"mary1": "87", "mary2": "90", "mary3": "34"}
# print(grades_mary)

grades_jim = {"jim1": "93", "jim2": "56", "jim3": "88"}
# print(grades_jim)

user_dict ={}
student_name = input(print("What is your student's name?:  "))
# print(student_name)

user_key1 = input(print("What's the name of the first key you'd like to add to your gradebook?:   "))
#print(user_key1)
user_grade1 = int(input("Input your first number for grades:  "))
user_key2 = input(print("What's the name of the second key you'd like to add to your gradebook?:  "))
#print(user_key2)
user_grade2 = int(input("Input your second number for grades:  "))
user_key3 = input(print("What's the name of the last key you'd like to add to your gradebook?:   "))
#print(user_key3)
user_grade3 = int(input("Input your last number for grades:  "))

user_dict[user_key1] = user_grade1
user_dict[user_key2] = user_grade2
user_dict[user_key3] = user_grade3
print(user_dict)
counter = 0
uSum = 0
for v in user_dict.values():
    uSum=  uSum +int(v)
    counter+=1
print(user_dict.values())    
counter = 0
uRyan = 0
for v in grades_ryan.values():
    uRyan= uRyan +int(v)
    counter+=1
print(grades_ryan.values())

counter = 0
uMary = 0
for v in grades_mary.values():
    uMary= uMary +int(v)
    counter+=1
print(grades_mary.values())

counter = 0
uJim = 0
for v in grades_jim.values():
    uJim= uJim +int(v)
    counter+=1
print(grades_jim.values())

average_user = uSum/counter
print(student_name + "'s grade average is: " + str(average_user))

average_ryan = uRyan/counter
print("Ryan's grade average is: " + str(average_ryan))

average_mary = uMary/counter
print("Mary's grade average is: " + str(average_mary))

average_jim = uJim/counter
print("Jim's grade average is: " + str(average_jim))


grade_remove = input(print("Select a key to remove a grade from Mary. "))
del grades_mary[grade_remove]
print(grades_mary)

# average_selector = input(print("Please select a student's average to calculate grade letter for average."))

# if average_selector == range(90, 100):
#     print("A")
# elif average_selector == range(80, 89):
#     print("B")
# elif average_selector == range(70, 79):
#     print("C")
# elif average_selector == range(60, 69):
#     print("D")
# elif average_selector <= (59):
#     print("F")
#change