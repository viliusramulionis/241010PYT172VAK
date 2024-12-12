# https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita
# https:// - protokolas kuriuo jungames (http, ftp, mysql ...)
# www - subdomenas (pvz s2.15min.lt, subdomenas yra s2)
# thecoktaildb.com - 172.67.152.227 - domenas
# /api/json/v1/1/ - parametrai
# search.php - failo pavadinimas
# ?s=margarita - query parametras

# jusu kompiuterio adresas butu localhost (127.0.0.1)
# 127.0.0.1:5050 - portas 

import requests

url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=lim"

response = requests.get(url)

# Grąžina tekstinę informaciją:
# print(response.text)

# JSON stringo konvertavimas: 
# print(response.json())

data = response.json()

# Pačio pirmo gėrimo pavadinimo susigrąžinimas
# print(data["drinks"][0]["strDrink"])

for drink in data["drinks"] :
    print(f"Pavadinimas: {drink["strDrink"]}, Tipas: {drink["strAlcoholic"]}")
