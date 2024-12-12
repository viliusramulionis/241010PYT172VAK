import requests
from bs4 import BeautifulSoup

# Adreso priskyrimas
url = "https://www.1551.lt/automobiliu-atsargines-dalys-reikmenys/"

# Pateikiame užklausą
data = requests.get(url)

if data.status_code != 200 :
    print("Nepavyko gauti duomenų")
else :
    # Paimame iš atsakymo gautą html kodą
    data = data.text

    # print(data)

    # # Konvertuojame HTML kodą į objektą
    html = BeautifulSoup(data, "html.parser")

    # select_one() metodas suranda vieną patį pirmą elementą pagal css selektorių
    # print(html.select_one(".uk-panel-title a span").text)

    # select() metodas grąžina visus elementus pagal pateiktą selektorių
    # for title in html.select(".uk-panel-title a span") :
    #     print(title.text)

    for box in html.select(".tm-result") :
        print(box.select_one(".uk-panel-title a span").text)
        print(box.select_one(".uk-margin").text)

    # Duomenų bazės lentelė:
    # id (INT)
    # title (VARCHAR)
    # description (TEXT)
    # address (VARCHAR)
    # phone (VARCHAR)