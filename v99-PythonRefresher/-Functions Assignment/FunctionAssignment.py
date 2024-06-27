"""
Function Assignment
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
"""


def user_dictionary(firstname, lastname, age):
    created_user_dictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return created_user_dictionary


solution_dictionary1 = user_dictionary( lastname="Roby2", firstname="Eric2", age=32)
solution_dictionary2 = user_dictionary("Eric", "Roby", 32)
print(solution_dictionary1)
print(solution_dictionary2)









