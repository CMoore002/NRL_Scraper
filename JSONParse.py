from CurrentRound import CurrentRound
from PreviousRound import PreviousRound

class JSONParse:
    def __init__(self, jsonData):
        self.jsonData = jsonData

    def getCurrentRound(self):
        season = self.jsonData['clock']['kickOffTimeLong'].split('-')[0]
        round = self.jsonData['roundTitle']
        venue = self.jsonData['venue']
        kickOffTime = self.jsonData['clock']['kickOffTimeLong'].split('T')[0]
        homeTeam = self.jsonData['homeTeam']['nickName']
        awayTeam = self.jsonData['awayTeam']['nickName']
        return CurrentRound(season, round, venue, kickOffTime, homeTeam, awayTeam)
    
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
        