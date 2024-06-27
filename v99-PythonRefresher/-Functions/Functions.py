"""
Functions
"""
# def my_function():
#     print("Inside my_function")
# my_function()

# def print_my_name(name, surname):
#     print (f"Hello {name} {surname}")
#
# print_my_name("Cata","Chivu")

# def print_color_red():
#     color = "Red"
#     print (color)
#
# color = "Blue"
# print(color)
# print_color_red()

# def print_numbers(highest, lowest):
#     print(highest)
#     print(lowest)
# print_numbers(2, 3)
# print_numbers (lowest=5, highest=3)

# def multiply(a, b):
#     return a * b
#
# result = multiply(10, 20)
# print(result)
#
# def print_list(list_of_numbers):
#     for x in list_of_numbers:
#         print(x)
#
# list_of_numbers = [1, 2, 3, 4, 5]
# print_list(list_of_numbers)

def achizitie(cost):
    return cost + taxe(cost)

def taxe(cost):
    tva = .19
    return cost*tva

cost_total = achizitie(50)
print(cost_total)


# def buy_item(cost_of_item):
#     return cost_of_item + add_tax_to_item(cost_of_item)
#
#
# def add_tax_to_item(cost_of_item):
#     current_tax_rate = .03
#     return cost_of_item * current_tax_rate
#
#
# final_cost = buy_item(50)
# print(final_cost)














