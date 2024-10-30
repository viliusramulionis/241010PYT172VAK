skaicius = 0

try :
    # tikriname ar ivyks klaida
    skaicius = int(input("Iveskite skaiciu"))

    skaicius.is_integer(0)

except ValueError as err :
    print("Ivyko klaida", err)

# try :
#     # Duomenu saugojimas
#     # Duomenu redagavimas

# except :
#     print("Ivyko klaida")

try :
    skaicius1 = int(input("Įveskite pirmą skaičių"))
    veiksmas = input("Įveskite veiksmą")
    skaicius2 = int(input("Įveskite antrą skaičių"))
except :
    print("Įvesta bloga reikšmė")


try :
    if veiksmas == "+" :
        print(skaicius1 + skaicius2)

    if veiksmas == "-" :
        print(skaicius1 - skaicius2)

    if veiksmas == "*" :
        print(skaicius1 * skaicius2)

    if veiksmas == "/" :
        print(skaicius1 / skaicius2)
except ZeroDivisionError as err: 
    print("Dalyba iš nulio negalima")

print("Sekantys veiksmai")