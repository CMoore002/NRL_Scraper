from CurrentRound import CurrentRound
from PreviousRound import PreviousRound
import requests
from bs4 import BeautifulSoup
import json


class JSONParse:
    """
    :param jsonData: the jsonData that contains the fixtures and data required for processing the results
    """ 
    def __init__(self, jsonData):
        self.jsonData = jsonData

    """
    This function processes the data from jsonData and creates an object for the current round
    :returns: a CurrentRound object that contains all the information of a match in the current round
    """ 
    def getCurrentRound(self):
        season = self.jsonData['clock']['kickOffTimeLong'].split('-')[0]
        round = self.jsonData['roundTitle']
        venue = self.jsonData['venue']
        kickOffTime = self.jsonData['clock']['kickOffTimeLong'].split('T')[0]
        homeTeam = self.jsonData['homeTeam']['nickName']
        awayTeam = self.jsonData['awayTeam']['nickName']
        return CurrentRound(season, round, venue, kickOffTime, homeTeam, awayTeam)

    """
    This function processes the data from jsonData and creates an object for a previous round
    :returns: a CurrentRound object that contains all the information of a match in a previous round
    """ 
    def getPreviousRound(self):
        season = self.jsonData['clock']['kickOffTimeLong'].split('-')[0]
        round = self.jsonData['roundTitle']
        venue = self.jsonData['venue']
        kickOffTime = self.jsonData['clock']['kickOffTimeLong'].split('T')[0]
        homeTeam = self.jsonData['homeTeam']['nickName']
        homeScore = self.jsonData['homeTeam']['score']
        awayTeam = self.jsonData['awayTeam']['nickName']
        awayScore = self.jsonData['awayTeam']['score']

        ##Getting completion and tackle percentage
        newSite = self.jsonData['secondaryCallToAction']['url'].split("#")[0]
        newPage = requests.get(newSite)
        newSoup = BeautifulSoup(newPage.text, 'html.parser')
        newJsonData = newSoup.find(class_="l-content pre-quench", id="vue-match-centre")['q-data']
        newSiteJson = json.loads(newJsonData)
        homeCompletionPercent, awayCompletionPercent, homeTacklePercent, awayTacklePercent = -1, -1, -1, -1
        for match in newSiteJson['match']['stats']['groups']:
            for stat in match['stats']:
                if stat['title'] == 'Completion Rate':
                    homeCompletionPercent = stat['homeValue']['value']
                    awayCompletionPercent = stat['awayValue']['value']
                
                if stat['title'] == 'Effective Tackle %':
                    homeTacklePercent = stat['homeValue']['value']
                    awayTacklePercent = stat['awayValue']['value'] 

    

        return PreviousRound(season, round, venue, kickOffTime, homeTeam, homeScore, homeCompletionPercent, homeTacklePercent, awayTeam, awayScore, awayCompletionPercent, awayTacklePercent)
        