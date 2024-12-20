from bs4 import BeautifulSoup
from selenium import webdriver # naršyklės kontroleris
from selenium.webdriver.chrome.options import Options #Naršyklės

opcijos = Options()
# Incognito mode
opcijos.add_argument('--incognito')
# Nustatome, jog mums neatidarinėtų naršyklės:
opcijos.add_argument('--headless')

driver = webdriver.Chrome(options=opcijos)
url = "https://www.baldoras.lt/katalogas/valgomojo-stalai/"

driver.get(url) #puslapio atsisiuntimas

source = driver.page_source # pasiimam puslapio html kodą

bs = BeautifulSoup(source, 'html.parser') 

print(bs.select_one('h1').text)
