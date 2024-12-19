from bs4 import BeautifulSoup
from selenium import webdriver # naršyklės kontroleris
from selenium.webdriver.chrome.options import Options #Naršyklės
from time import sleep
from selenium.webdriver.common.by import By

opcijos = Options()
# Incognito mode
opcijos.add_argument('--incognito')
# Nustatome, jog mums neatidarinėtų naršyklės:
# opcijos.add_argument('--headless')

driver = webdriver.Chrome(options=opcijos)
url = "https://elenta.lt/1077241/dacia-duster-1-0-l-suv-2021-12500-euro-alytuje"

driver.get(url) #puslapio atsisiuntimas

sleep(1)
# print(driver.find_element(By.CSS_SELECTOR, '.fc-cta-consent').text)

# Paspaudimo registravimas:
driver.find_element(By.CSS_SELECTOR, '.fc-cta-consent').click()

driver.find_element(By.ID, 'show-phone-number-link').click()

sleep(1)

print(driver.find_element(By.ID, 'show-phone-number-link').text)

driver.find_element(By.CSS_SELECTOR, '[title="Prisijungti prie eLenta.lt"]').click()

sleep(1) 

# Ivedamas prisijungimo vardas
driver.find_element(By.ID, 'UserName').send_keys('vardas')
# Ivedamas slaptazodis
driver.find_element(By.ID, 'Password').send_keys('slaptazodis')
# Paspaudziame ant mygtuko
driver.find_element(By.CSS_SELECTOR, '[value="Prisijungti"]').click()


sleep(30)