# Susikurkite tris kintamuosius skaičiams saugoti. Į juos
# įrašykite norimus skaičius. Raskite šių skaičių suma,
# skirtumą, sandaugą ir dalmenį. Atsakymus išveskite kartu su
# atliekamu veiksmu (pvz 8 + 2 + 4 = 14).

pirmas = 30
antras = 5
trecias = 2

rezultatas = pirmas + antras + trecias

print(str(pirmas) + " + " + str(antras) + " + " + str(trecias) + " = " + str(rezultatas))

rezultatas = pirmas - antras - trecias

# + sudeda skaičius arba du stringus į vieną
# - atima vieną skaičių iš kito

print(str(pirmas) + " - " + str(antras) + " - " + str(trecias) + " = " + str(rezultatas))

rezultatas = pirmas * antras * trecias

print(str(pirmas) + " * " + str(antras) + " * " + str(trecias) + " = " + str(rezultatas))

rezultatas = pirmas / antras / trecias

print(str(pirmas) + " / " + str(antras) + " / " + str(trecias) + " = " + str(rezultatas))

# Susikurkite du kintamuosius skaičiams saugoti. Į juos
# įrašykite norimus skaičius. Pirmąjį kintamąjį padidinkite
# 5-iais. Antrajį padidinkite 2 kartus. Išveskite visus atsakymus
# (pradines reikšmes ir pakeistas reikšmes).

pirmas = 2
antras = 5

pirmasRezultatas = "Pradidnė reikšmė " + str(pirmas)
antrasRezultatas = "Rezultatas: " + str(pirmas ** 5)

print(pirmasRezultatas, antrasRezultatas)

pirmasRezultatas = "Pradidnė reikšmė " + str(antras)
antrasRezultatas = "Rezultatas: " + str(antras ** 2)

print(pirmasRezultatas, antrasRezultatas)


#STRINGAI

# Stringus galime žymėti "" arba '' kabutėmis

pirmasZodis = "Labas"
antrasZodis = 'Pasauli'

# pavadinimas = "UAB \"Gera Parduotuve\""
pavadinimas = 'UAB "Gera Parduotuve"'

print(pirmasZodis + " " + antrasZodis)


tekstas = "Vilija Blinkevičiūtė"
# len() funkcija grąžina stringo ilgį
# tarpeliai kaip ir visi kiti simboliau yra įskaičiuojami į bendrą stringo ilgį
print(len(tekstas))

# metodas zymimas objektas.metodoPavadinimas()
# metodas nekeičia originalios kintamojo reikšmės

tekstas = tekstas.upper()
print(tekstas.upper())

# metodas lower() pakeičia stringo raides į mažąsias
print(tekstas.lower())

# metodas replace(KA_KEICIAM, KUOM_KEICIAM) - pakeičia pasirinktą stringo dalį į kažkurį kitą stringą
# DIDŽIOSIOS IR MAŽOSIOS RAIDĖS TURI SKIRIASI

tekstas = "Vilija Blinkevičiūtė"
print(tekstas.replace('Vilija', 'Ramūnas'))

tekstas = "Geri vyrai geroj girioj gerą girą geria"

print(tekstas.replace("g", "l"))

print(
    "Geri vyrai geroj girioj gerą girą geria"
      .replace("g", "l")
      .replace("G", "L")
      .upper()
)

# Norint pakartoti stringą kelis kartus
print("Labas " * 10)

tekstas = "Labas"

print(len(tekstas))

# Norint paimti pirmą simbolį iš stringo
# Indeksas - nurodo simbolio poziciją stringe
print(tekstas[0])
print(tekstas[1])
print(tekstas[2])
print(tekstas[3])
print(tekstas[4])

print("SLICE PAVYZDYS")

tekstas = "Geri vyrai geroj girioj gerą girą geria"
# print(len(tekstas))

print(tekstas[len(tekstas) - 1])

# Pirmo žodžio paėmimas
print(tekstas[0:4])

# Antro žodžio paėmimas
print(tekstas[5:10])