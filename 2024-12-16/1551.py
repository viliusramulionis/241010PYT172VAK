import requests
from bs4 import BeautifulSoup
import mysql.connector

try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="skelbimai")
    
    # Kursoriaus sukūrimas
    cur = cnx.cursor()

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
            pavadinimas = box.select_one(".uk-panel-title a span").text
            adresas = box.select_one(".uk-margin-right").text
            telefonas = box.select_one(".uk-text-right").text.replace('\n')
            aprasymas = box.select_one(".uk-width-medium-4-5 > .uk-margin").text
            
            cur.execute(f"INSERT INTO skelbimai (title, description, address, phone) VALUES ('{pavadinimas}', '{aprasymas}', '{adresas}', '{telefonas}')")
            
            cnx.commit()

        # Duomenų bazės lentelė:
        # id (INT)
        # title (VARCHAR)
        # description (TEXT)
        # address (VARCHAR)
        # phone (VARCHAR)

    cnx.close()
except :
    # print(e)
    print("Prisijungimo klaida")

