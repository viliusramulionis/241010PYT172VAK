import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = "https://elenta.lt"

next_url = "/skelbimai/nt/butai"

def get_data(base, next) :  
    response = []

    data = requests.get(base + next)

    html = BeautifulSoup(data.text, "html.parser")

    # response.append(html.select_one('title').text)
    # INFOMRACIJOS PAĖMIMAS
    
    # Naudojant find ir find_all metodus
    # data = html.find('ul', { "class": "units-list"})

    # data = data.find_all('li')

    # for listing in data :
    #     print(listing)


    data = html.select('.units-list li')
    
    for listing in data :
        title = listing.select_one('a.ad-hyperlink')
        title = title.text if title else ""

        image = listing.select_one('img')
        image = image.attrs['src'] if image else ""

        price = listing.select_one('.price-box')
        # if price :
        #     price = price.text 
        # else :
        #     price = 0

        price = price.text if price else "0"

        address = listing.select_one(".location-box")
        address = address.attrs["title"].replace("adresas", "").replace("vieta", "").strip() if address else "Nenurodyta"


        description = listing.select_one("p")
        description = description.text if description else ""

        response.append({
            "title" : title,
            "image": image,
            "price" : price,
            "address": address,
            "description": description
        })

    next = html.select_one('[rel="next"]')

    # Vykdo palaukimą sekundžių tikslumu 
    sleep(1)

    if next :
        next = html.select_one('[rel="next"]').attrs['href']
        response += get_data(base, next)

    return response


f = open("data.csv", "w", encoding="utf8")

data = get_data(base_url, next_url)

for listing in data :
    # print(";".join(listing.values()))
    f.write(";".join(listing.values()) + "\n")