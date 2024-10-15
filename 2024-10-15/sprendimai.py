# Suskaičiuoti, kiek simbolių yra jūsų varde, pavardėje.
print("PIRMA UZDUOTIS")
vardas = 'Vilius'
pavarde = 'Ramulionis'

print("Varde yra " + str(len(vardas)) + " simboliai")
print("Pavardeje yra " + str(len(pavarde)) + " simboliai")

# Suskaičiuoti, kiek simbolių yra pačio pirmojo delfi.lt straipsnio antraštėje
print("ANTRA UZDUOTIS")

tekstas = "Į Seimą – gerai žinomi sporto, sveikatos, etiketo ir ekonomikos profesionalai: kas jie?"
print("Pavadinime yra: " + str(len(tekstas)) + " simboliai")

# Pakeisti visas raides į mažąsias jūsų varde. Ir į didžiąsias ;)
print("TREČIA UZDUOTIS")
print(vardas.upper())
print(vardas.lower())

# Iš delfi antraštės atrinkite pirmus 10 simbolių; paskutinius 10; kas antrą; iškirpkite tekstą nuo 10-to iki 20-to simbolių;
print("Pirmi dešimt simbolių:", tekstas[0:10])
print("Paskutiniai dešimt simbolių:", tekstas[-10:])
print("Kas antras simbolis:", tekstas[::2])
print("Nuo 10 iki 20:", tekstas[10:20])

# Kiek delfi antraštėje yra "a" simbolių? Kurioje pozicijoje yra pirmąkart sutinkamas šis simbolis?
# https://www.w3schools.com/python/ref_string_count.asp

print("Raidė a panaudota: ", tekstas.count('a'))
print("Pirma pozicija: ", tekstas.find('a'))

# Iš teksto txt="Labas rytas!" išveskite tekstą be pirmo simbolio; be paskutinio; be pirmo ir be paskutinio;
txt = "Labas rytas!"

# print(txt[1:len(txt)])
print("Be pirmos raidės:", txt[1:])

# print("Be paskutinės raidės:", txt.replace('!', ''))
print("Be paskutinės raidės:", txt[:-1])

print("Be pirmo ir be paskutinio", txt[1:-1])

