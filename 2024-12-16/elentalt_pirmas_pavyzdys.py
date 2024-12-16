import requests
from bs4 import BeautifulSoup
from time import sleep

# Pirmas puslapis: https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai
# Antras puslapis: https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai/2
# Trecias puslapis: https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai/3

for page in range(1, 5) :
    data = requests.get('https://elenta.lt/skelbimai/buitis-laisvalaikis/baldai/' + str(page))

    html = BeautifulSoup(data.text, "html.parser")

    print(html.select_one('title').text)

    # Vykdo palaukimą sekundžių tikslumu 
    sleep(2)