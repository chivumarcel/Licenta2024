"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""

# my_set = {1, 2, 3, 4, 5, 1, 2}
# print(my_set)
# print(len(my_set))
#
#
# for x in my_set:
#     print(x)
#
#
# my_set.discard(3)
# print(my_set)
# my_set.add(6)
# print(my_set)
# my_set.update([7, 8])
# print(my_set)


# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[1])
# my_tuple[1] = 100


set1 = {1,2,3,4,5,1,2}
#setul contine valori unice // 1 si 2 nu se vor printa
#setul contine elemente neordonate, si nu au index, ele se pot regasi oriunde in memorie

print(set1)
print(f"Setul contine {len(set1)} elemente")
for x in set1: print(x)

set1.discard(5) #elimina din set elementul cu valoare data ca parametru
print(set1)
set1.clear()
print(set1)





















