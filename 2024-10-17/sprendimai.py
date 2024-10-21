# Paprašykite vartotojo įvesti 5-is savo pažymius.
# Paskaičiuokite pažymių vidurkį. Išveskite atsakymą.

# pirmas = int(input("Įveskite pažymį: "))
# antras = int(input("Įveskite pažymį: "))
# trecias = int(input("Įveskite pažymį: "))
# ketvirtas = int(input("Įveskite pažymį: "))
# penktas = int(input("Įveskite pažymį: "))

# rezultatas = (pirmas + antras + trecias + ketvirtas + penktas) / 5

# PIRMOS UŽDUOTIES VARIACIJA

# print("Vidurkis yra:", rezultatas)

# skaiciai = []

# skaiciai.append(int(input("Įveskite pažymį: ")))
# skaiciai.append(int(input("Įveskite pažymį: ")))
# skaiciai.append(int(input("Įveskite pažymį: ")))
# skaiciai.append(int(input("Įveskite pažymį: ")))
# skaiciai.append(int(input("Įveskite pažymį: ")))

# rezultatas = sum(skaiciai) / len(skaiciai)

# print("Vidurkis yra:", rezultatas)


# Leiskite vartotojui įvesti metrus. Išveskite, kiek tai gaunasi
# centimetrais, milimetrais ir kilometrais.

# metrai = int(input("Įveskite metrus: "))

# centimetrai = metrai * 100
# milimetrai = metrai * 1000
# kilometrai = metrai / 1000

# print(
#     "Įvesti metrai:", metrai, "\n"
#     "Centimetrai:", centimetrai, "\n"
#     "Milimetrai:", milimetrai, "\n"
#     "Kilometrai:", kilometrai, "\n"
# )

# Leiskite vartotojui įvesti du norimus skaičius. 
# Išveskite kokia gaunasi liekana padalinus vieną skaičių iš kito.

# pirmas = int(input("Įveskite pirmą skaičių: "))
# antras = int(input("Įveskite antrą skaičių: "))

# print("Gautas rezultatas:", pirmas / antras)

# Leiskite vartotojui įvesti du skaičius. Išveskite kiek gautųsi
# vieną skaičių pakėlus kito skaičiaus laipsniu (pvz, pirmas
# skaičius eina už pagrindą, o antras skaičius yra laipsnis,
# kuriuo ir keliame).

# pirmas = int(input("Įveskite pirmą skaičių: "))
# antras = int(input("Įveskite antrą skaičių: "))

# print("Gautas rezultatas:", pirmas ** antras)

lst = ["Python", "yra", "lengva", "programavimo", "kalba"]

# Išveskite pirmą, paskutinį elementus
print("Pirmas elementas:", lst[0])
print("Paskutinis elementas:", lst[-1])

# Išveskite kas antrą elementą

print("Kas antras elementas", lst[1::2])

# Išveskite priešpaskutinio elemento tipą
print(type(lst[-2]))

# Patikrinkite, ar pirmasis sąrašo elementas yra tekstas, ir kiek simbolių jis turi.
print(len(lst[0]))

txt = "Aš rytais mėgstu kavą su sumuštiniais ir arbatą su pyragu"

print("Tekste yra: ", len(txt.split()), "žodžių")

# Išveskite tekstą be kas antro žodžio

print(txt.split()[::2])
