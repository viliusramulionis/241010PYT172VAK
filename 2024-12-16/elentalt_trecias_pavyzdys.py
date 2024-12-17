import requests
from bs4 import BeautifulSoup
from time import sleep

# Pirmas puslapis: https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai
# Antras puslapis: https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai/2
# Trecias puslapis: https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai/3

base_url = "https://elenta.lt"

next_url = "/skelbimai/nt/butai"

def get_data(base, next) :  
    response = []

    data = requests.get(base + next)

    html = BeautifulSoup(data.text, "html.parser")

    response.append(html.select_one('title').text)

    next = html.select_one('[rel="next"]')

    # Vykdo palaukimą sekundžių tikslumu 
    sleep(1)

    if next :
        next = html.select_one('[rel="next"]').attrs['href']
        response += get_data(base, next)

    return response


print(get_data(base_url, next_url))


# Surinkite šią informaciją ir patalpinkite ją duomenų bazėje:
# https://elenta.lt/skelbimai/nt/butai

# *Nuotraukos adresas
# *Pavadinimas
# *Kaina
# *Adresas
# *Aprašymas