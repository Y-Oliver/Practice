import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time

page = ("https://forecast.weather.gov/MapClick.php?CityName=Germantown&state=MD&site=LWX&lat=39.1782&lon=-77.2607")

webs = requests.get(page).text

soup = BeautifulSoup(webs,'lxml')

#print(soup.prettify())


#My_table = soup.find_all("div", id="current_conditions-summary")
article_text = ''
weather = soup.find("div", {"id":"current_conditions-summary"}).findAll('p',limit=2)
#weather = My_table.findAll('p').getText()

while True:
    time.sleep(10)
    for info in weather:
        info = info.getText()
    print("Current Temperature Outside:",info)
