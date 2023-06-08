from CurrentRound import CurrentRound
from PreviousRound import PreviousRound

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
        return PreviousRound(season, round, venue, kickOffTime, homeTeam, homeScore, awayTeam, awayScore)
        