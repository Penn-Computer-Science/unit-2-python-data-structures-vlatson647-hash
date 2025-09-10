gradebook = {"Ryan": "94, 87, 81", "Mary": "81, 76, 89", "Kyle": "19, 23, 11"}

user_student = input(print("What's the name of the student you'd like to add to your gradebook? "))
print(user_student)
gradebook

user_grade = input(print("What grades will this student have?"))
print(user_grade)

gradebook[user_student] = user_grade
print(gradebook)






#change