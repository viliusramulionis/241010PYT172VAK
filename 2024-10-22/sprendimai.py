# Liepkite vartotojui suvesti savo amžių. Patikrinkite ar amžius
# yra didesnis arba lygus 18-ai, jei taip - išveskite “jūs galite
# balsuoti”


# amzius = int(input("Suveskite savo amžių: "))

# if amzius >= 18 :
#     print("Jūs galite balsuoti")  
# else :
#     print("Susitikite per kitus rinkimus")


# Leiskite vartotojui suvesti norimą kiekį pažymių (pavyzdžiui,
# jūs nusimatote 3-is kintamuosius, tai leidžiate padaryti 3
# įvedimus). Raskite šių pažymių vidurkį. Patikrinkite ar
# vidurkis teigiamas (daugiau arba lygu 5-iems), jei taip -
# išveskite 'vidurkis teigiamas'.

pirmas = int(input("Įveskite pirmajį pažymį: "))
antras = int(input("Įveskite antrajį pažymį: "))
trecias = int(input("Įveskite trečiajį pažymį: "))

print("Vidurkis yra:", (pirmas + antras + trecias) / 3)