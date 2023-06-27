from JSONParse import JSONParse
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


def main():
    ##User enters the season that they want results from
    userSeason = input("Enter Season: ")
    round = 1
    headers = ['Season', 'Round', 'Venue', 'Kick_Off_Time', 
               'Home_Team', 'Home_Score', 'Home_Completion', 'Home_Tackle',
               'Away_Team', 'Away_Score', 'Away_Completion', 'Away_Tackle']
    dataframe = pd.DataFrame(columns=headers)

    while True:
        ##Getting website HTML and converting the jsonData to json to be able to use it as a dictionary
        website = "https://www.nrl.com/draw/?competition=111&round={}&season={}".format(round, int(userSeason))
        page = requests.get(website)
        soup = BeautifulSoup(page.text, 'html.parser')
        jsonData = soup.find(class_="u-spacing-mt-24")['q-data']
        siteJson = json.loads(jsonData)

        ##siteJson['fixtures'] contains all the fixtures in the round. Looping through each one gives the details for each match
        for jsonFixtures in siteJson['fixtures']:
            fixtureData = JSONParse(jsonFixtures).getPreviousRound()
            print("test")
            ##appending the data to the dataframe
            data = [fixtureData.getSeason(), ##getting season
                    fixtureData.getRound(), ##getting round
                    fixtureData.getVenue(), ##getting venue
                    fixtureData.getKickOffTime(), ##getting kick off time
                    fixtureData.getHomeTeam(), ##getting home team
                    fixtureData.getHomeScore(), ##getting home score
                    fixtureData.getHomeCompletion(), ##getting home completion
                    fixtureData.getHomeTacklePercentage(), ##getting home tackle percentage
                    fixtureData.getAwayTeam(), ##getting away team
                    fixtureData.getAwayScore(), ##getting away score
                    fixtureData.getAwayCompletion(), ##getting away completion
                    fixtureData.getAwayTacklePercentage() ##getting away tackle percentage
                    ]
            dataframe.loc[len(dataframe)] = data
            lastRound = fixtureData.getRound()

        ##No more matches after the grand final, so we finish and return
        if lastRound == 'Grand Final':
            ##exporting data to csv
            dataframe.to_csv('{}_SEASON_NRL_DATA_v1.1'.format(userSeason))
            return
        round += 1


if __name__ == '__main__':
    main()