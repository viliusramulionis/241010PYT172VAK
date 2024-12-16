import requests
from bs4 import BeautifulSoup
from time import sleep

# Pirmas puslapis: https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai
# Antras puslapis: https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai/2
# Trecias puslapis: https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai/3

base_url = "https://elenta.lt"

next_url = "/skelbimai/nt/butai"

while True :
    data = requests.get(base_url + next_url)

    html = BeautifulSoup(data.text, "html.parser")

    print(html.select_one('title').text)

    next = html.select_one('[rel="next"]')
    
    if next :
        next_url = html.select_one('[rel="next"]').attrs['href']
    else :
        break
    
    # Vykdo palaukimą sekundžių tikslumu 
    sleep(2)




