# vardas1 = "Asta"
# vardas2 = "Tomas"
# vardas3 = "Arūnas"
# vardas4 = "Žydrūnas"

# List pavyzdys (array - masyvas)
# Sarase esancios reiksmes gali buti vadinamos elementais 
sarasas = [
    "Asta", #Indeksas: 0 
    "Tomas", #Indeksas: 1
    "Arūnas", #Indeksas: 2
    "Žydrūnas", #Indeksas: 3
    12345 #Indeksas: 4
]

# Visų reikšmių atspausdinimas
print(sarasas)

# Pirmos reikšmės atspausdinimas
print(sarasas[0])

# Pirmu indeksu pažymėto elemento paėmimas
print(sarasas[1])

# Sąrašo ilgio susigrąžinimas:
# len(sarasas)
print(len(sarasas))

# Sarasu metodai modifikuoja originalu masyva!

# Norint pridėti naują elementą į sąrašo pabaigą
sarasas.append("Šarūnas")

print(sarasas)

# Norint pridėti naują elementą į norimą sąrašo poziciją
sarasas.insert(0, "Miglė")

print(sarasas)

# Norint pasalinti elementą iš sąrašo nurdant indeksą:
sarasas.pop(5)

print(sarasas)

# Skaičiuojame kiek kartų vardas Arūnas paminėtas sąraše

sarasas.append('Arūnas')

print(sarasas.count('Arūnas'))

# Norint išvalyti sąrašą:
sarasas.clear()

print(sarasas)

sarasas.append('Tomas')

print(sarasas)

# Naujo saraso priskyrimas prie kitamojo
sarasas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Norint ištraukti saraso elementus pagal nurodytas pozicijas (nuo - iki)
print(sarasas[2:5])

# Norint pasirinkti kas antrą elementą iš sąrašo:
print(sarasas[::2])

# Norint konvertuoti stringą į sąrašą
tekstas = "Nepatogūs klausimai su Rolandu Mackevičiumi. Svečiuose – Džordana Butkutė"

# tekstas.split() metodas išskaido stringą į sąrašą (pagal nutylėjimą per kiekvieną tarpelį)
# tekstas.split('.') - išskaidytų tekstą į dvi dalis

zodziai = tekstas.split()

# Pirmo žodžio susigrąžinimas:
print(zodziai[0])  

# Sujungia list'ą į vieną stringą
print(' '.join(zodziai))

# Funkcija input()
skaicius = input("Įveskite skaičių:")
print("Įvestas skaičius:", skaicius)

skaicius = input("Įveskite skaičių:")
print("Įvestas skaičius:", skaicius)