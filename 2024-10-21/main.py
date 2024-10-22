# Taip / Ne - Boolean

# teigiamas = True
# neigiamas = False

tikrinimas = True

print(type(tikrinimas))

if tikrinimas: 
    print("Kintamasis yra teigiamas")
else:
    print("Kintamasis yra neigiamas")

print("Patikrinimas baigėsi")


# Sukurkite du kintamuosiuos, priskirkite jiems 
# norimas reikšmes ir didesnę reikšmę padalinkite iš mažesnės

pirmas = 8
antras = 12

if pirmas > antras : 
    # False
    print(pirmas / antras)
elif pirmas == antras :
    # True 
    print("Skaičiai yra lygūs")
else :
    print(antras / pirmas)


# Elif alternatyva:
if pirmas > antras :
    print(pirmas / antras)
else :
    if pirmas == antras:
         print("Skaičiai yra lygūs")
    else:
        print(antras / pirmas)


skaicius = 15

if skaicius == 15 :
    print("Skaičius yra lygus penkiolikai")


procentas = 79

# Kai naudojamas and operatorius visos sąlygos privalo būti teigiamos
if procentas >= 80 and procentas <= 90 :
    print("Procentas papuola į A kategoriją")


skaicius = 7

# Naudojant or operatorių, tik viena iš išvardintų sąlygų turi būti teigiama
if skaicius == 1 or skaicius == 4 or skaicius == 7 or skaicius == 10 :
    print("Jūs laimėjote")


skaicius = 10

if skaicius > 5 and skaicius > 8:
    print("Salyga teigiama")


stringas = "Labadienavarototojauusername511515"

if stringas.isalnum() :
    print("Stringas neturi specialiųjų simbolių")

stringas = "labas"

if stringas.isalpha() :
    print("Stringas yra tik iš raidžių")

skaicius = input("Įveskite skaičių:")

# TERNARY OPERATORIAUS PANAUDOJIMAS

# Sąlygos aprašymas nenaudojant ternary operatoriaus
# if skaicius.isnumeric() :
#     skaicius = int(skaicius)
# else :
#     skaicius = 0

# print(skaicius)

# Su ternary operatoriumi

skaicius = int(skaicius) if skaicius.isnumeric() else 0

print(skaicius)

# Tikriname stringus:

tekstas = ''

if tekstas :
    # False dėl to nieko nevyksta
    print("Stringas nėra tuščias")

skaicius = 0

if skaicius :
    # False dėl to nieko nevyksta
    print("Skaičius yra teigiamas")

vardas = input("Įveskite vardą: ")

if vardas :
    print("Įvestas vardas: ", vardas)
else :
    vardas = input("Įveskite vardą: ")

