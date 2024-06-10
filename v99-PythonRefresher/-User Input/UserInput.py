# """
# User Input
# """
#
# first_name = input("Enter your first name: ")
# days = input("How many days before your birthday: ")
# print(f"Hi {first_name}, only {days} days "
#       f"before your birthday!")
#
#
#


prenume = input("Care este prenumele tau?: \n")
print (f"Salutare {prenume}!")
an_nastere = input("Care este anul tau de nastere?\n")
varsta = 2024 - (int(an_nastere))
print(f"Minunat! Inseamna ca ai {varsta} ani! La multi ani {prenume}!")
numar_zile = input("Cam cate zile mai sunt pana la ziua ta de nastere?\n")
saptamani = round(int(numar_zile)/7)
print(f"Wow! inseamna ca mai sunt aproximativ {saptamani} saptamani pana la ziua ta {prenume}!")
