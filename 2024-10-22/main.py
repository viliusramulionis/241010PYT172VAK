if "a" in "abc" :
    print("Simbolis a yra stringe abc")

# Didžiosios ir mažosios raidės skiriasi

if "A" in "abc" :
    print("Simbolis a yra stringe abc")

# Norint ieškoti simbolio nepaisant to ar raidė yra iš didžiosios ar mažosios raidės
tekstas = input("Įveskite tekstą: ")
ieskomas = input("Įveskite ieškomą frazę: ")

if ieskomas.lower() in tekstas.lower() :
    print("Radome tokį tekstą")

sarasas = ["Vilnius", "Kaunas", "Klaipėda"]

if "Vil".lower() in sarasas[0].lower() :
    print("Yra")

if "Vil" in sarasas[1] :
    print("Yra")

if "Vil" in sarasas[2] :
    print("Yra")

# Needle in haystack