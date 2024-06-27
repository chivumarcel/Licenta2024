'''
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals
'''

zoo = ["animal1", "animal2", "animal3", "animal4", "animal5"]
zoo.pop(3) #sterg animanul de pe index3 = animal4
print(zoo)
zoo.append("animal6")
zoo.pop(0)
print(zoo)
print(zoo[:3])
x = len(zoo)
print(x)
for x in zoo: print(x)


#
# zoo = ["Monkey", "Zebra", "Gorilla", "Lion", "Tiger"]
# zoo.pop(3)
# zoo.append("Lizard")
# zoo.pop(0)
# print(zoo)
# for x in zoo:
#     print(x)
# print(zoo[0:3])
# i = 0
# while i < 3:
#     print(zoo[i])
#     i += 1
#
#
