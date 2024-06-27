"""
For & While Loops
"""
my_list = [1, 2, 3, 4, 5]
sum = 0;
for x in my_list:
    sum += x
print (sum)

my_days = ["Luni", "Marti", "Miercuri", "Joi", "Vineri"]
for x in my_days:
    print(f"Ziua de {x} este fantastica!")

i = 0
while i<=5:
    i+=1
    if i==3: #daca s-a ajuns la i=3, atunci efectiv se sare peste el si se continua bucla while
        continue
    if i==4:
        break
    print(i)



# i = 0
#
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
#     if i == 4:
#         break
# else:
#     print("i is now larger or equal to 5")



















