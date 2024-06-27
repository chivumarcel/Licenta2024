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


# set1 = {1,2,3,4,5,1,2}
# #setul contine valori unice // 1 si 2 nu se vor printa
# #setul contine elemente neordonate, si nu au index, ele se pot regasi oriunde in memorie !!!
#
# print(set1)
# print(f"Setul contine {len(set1)} elemente")
# for x in set1: print(x)
#
# set1.discard(5) #elimina din set elementul cu valoare data ca parametru
# print(set1)
# # set1.clear()
# # print(set1)
#
# set1.add(50) #adaug un singur element
# print(set1)
#
# set1.update([9,99,999, 8, 9]) #adaug multiple elemente
# print(set1) #la rulari diferite, afisarea elementelor este in ordine diferita :))


tuplu1 = (1,2,3,4,5)
print(tuplu1)
print (f"tuplul are {(len(tuplu1))} elemente")
print(tuplu1[3])
#nu se pot face add, sau update pe tuplu, nu se poate face nici asignare la un anumit index // tuplu1[1] = 100
# setul se foloseste cand vrei o lista super rapida, sau sa elimi duplicatele
# tuplul il folosesti cand nu vrei sa schimbi elemente dintr-o lista, el fiind un element static















