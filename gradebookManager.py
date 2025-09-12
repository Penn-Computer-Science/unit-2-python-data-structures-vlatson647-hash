grades_ryan = {}

grades_ryan = {"ryan1": "23", "ryan2": "76", "ryan3": "78"}
print(grades_ryan)

grades_mary = {}

grades_mary = {"mary1": "87", "mary2": "90", "mary3": "34"}
print(grades_mary)

grades_jim = {}

grades_jim = {"jim1": "93", "jim2": "56", "jim3": "88"}
print(grades_jim)

user_dict ={}

user_key1 = input(print("What's the name of the first key you'd like to add to your gradebook? "))
print(user_key1)
user_grade1 = int(input("Input your first number for grades"))
user_key2 = input(print("What's the name of the second key you'd like to add to your gradebook? "))
print(user_key2)
user_grade2 = int(input("Input your second number for grades"))
user_key3 = input(print("What's the name of the last key you'd like to add to your gradebook? "))
print(user_key3)
user_grade3 = int(input("Input your last number for grades"))

user_dict[user_key1] = user_grade1
user_dict[user_key2] = user_grade2
user_dict[user_key3] = user_grade3


#change