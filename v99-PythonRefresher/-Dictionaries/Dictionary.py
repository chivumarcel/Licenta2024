"""
Dictionaries
"""
user_dict = {
    'user':'catalin',
    'email':"c@t.ro",
    'files': 25
}
user_dict["married"] = True


# print(user_dict)
# print(user_dict.get('user'))
# print(user_dict.get('married'))
# print (f"Dictionarul are {(len(user_dict))} elemente")
#
# user_dict.pop("files") #stergem elementul / perechea "files" din dictionar
# print(user_dict)
# print (f"Dupa pop, dictionarul are {(len(user_dict))} elemente")
#
# del user_dict['user']
# print(user_dict)
#
# user_dict.clear()
# print (f"Dupa clear, dictionarul are {(len(user_dict))} elemente")
#
# del user_dict #sterge tot dictionarul

# for x in user_dict:
#     print(x)
#
# for x, y in user_dict.items():
#     print(x, y)

print("--- copy shallow, and deep ---\n")

user_dict2 = user_dict #shallow
#user_dict2 = user_dict.copy()
user_dict2.pop("files")
print(user_dict)
print(user_dict2)

#---------
#
# """
# Dictionaries with additional explanations
# """
# user_dict = {
#     'user':'catalin',
#     'email':"c@t.ro",
#     'files': 25
# }
# user_dict["married"] = True
# print(user_dict)
# print(user_dict.get('user'))
# print(user_dict.get('married'))
# print (f"Dictionarul are {(len(user_dict))} elemente")
#
# user_dict.pop("files") #stergem elementul / perechea "files" din dictionar
# print(user_dict)
# print (f"Dupa pop, dictionarul are {(len(user_dict))} elemente")
#
# user_dict.clear()
# print (f"Dupa clear, dictionarul are {(len(user_dict))} elemente")
#
# # Verificăm dacă dicționarul conține cheia 'user' înainte de a o șterge
# if 'user' in user_dict:
#     del user_dict['user']
#     print("Cheia 'user' a fost stearsa")
# else:
#     print("Cheia 'user' nu exista in dictionar")
#
# print(user_dict)
#
# # Verificăm dacă dicționarul există înainte de a încerca să-l ștergem
# try:
#     del user_dict
#     print("Dicționarul a fost șters.")
# except NameError:
#     print("Dicționarul nu exista.")
#
# # Aceasta linie va genera o eroare daca dicționarul a fost șters, deci o putem elimina sau trata:
# try:
#     print(user_dict)
# except NameError:
#     print("user_dict nu mai exista.")
#

# user_dictionary = {
#     'username': 'codingwithroby',
#     'name': 'Eric',
#     'age': 32
# }
#
#
# user_dictionary2 = user_dictionary.copy()
# user_dictionary2.pop("age")
# print(user_dictionary2)






















