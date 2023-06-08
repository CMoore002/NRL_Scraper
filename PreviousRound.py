from CurrentRound import CurrentRound

class PreviousRound(CurrentRound):
    def __init__(self, season, round, venue, kickOffTime, homeTeam, homeScore, awayTeam, awayScore):
        super().__init__(season, round, venue, kickOffTime, homeTeam, awayTeam)
        self.homeScore = homeScore
        self.awayScore = awayScore

    def getHomeScore(self):
        return self.homeScore
    
    def getAwayScore(self):
        return self.awayScore
