from JSONParse import JSONParse
import requests
from bs4 import BeautifulSoup
import json


def main():
    ##User enters the season that they want results from
    userSeason = input("Enter Season: ")
    round = 1
    while True:
        website = "https://www.nrl.com/draw/?competition=111&round={}&season={}".format(round, int(userSeason))
        page = requests.get(website)
        soup = BeautifulSoup(page.text, 'html.parser')
        jsonData = soup.find(class_="u-spacing-mt-24")['q-data']
        siteJson = json.loads(jsonData)
        for jsonFixtures in siteJson['fixtures']:
            fixtureData = JSONParse(jsonFixtures).getPreviousRound()
            print(fixtureData.getRound(), fixtureData.getHomeTeam(), fixtureData.getHomeScore(), fixtureData.getAwayTeam(), fixtureData.getAwayScore())
            lastRound = fixtureData.getRound()
        if lastRound == 'Grand Final':
            return
        round += 1


if __name__ == '__main__':
    main()