from JSONParse import JSONParse
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

round = 1
userSeason = 2018
website = "https://www.nrl.com/draw/?competition=111&round={}&season={}".format(round, int(userSeason))
page = requests.get(website)
soup = BeautifulSoup(page.text, 'html.parser')
jsonData = soup.find(class_="u-spacing-mt-24")['q-data']
siteJson = json.loads(jsonData)

for x in siteJson['fixtures']:
    newSite = x['secondaryCallToAction']['url'].split("#")[0]
    newPage = requests.get(newSite)
    newSoup = BeautifulSoup(newPage.text, 'html.parser')
    newJsonData = newSoup.find(class_="l-content pre-quench", id="vue-match-centre")['q-data']
    newSiteJson = json.loads(newJsonData)
    for match in newSiteJson['match']['stats']['groups']:
        for x in match['stats']:
            if x['title'] == 'Completion Rate':
                print(x['homeValue']['value'], x['awayValue']['value'])
            if x['title'] == 'Effective Tackle %':
                print(x['homeValue']['value'], x['awayValue']['value'])
                


    