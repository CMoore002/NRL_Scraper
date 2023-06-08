class CurrentRound:
    def __init__(self, season, round, venue, kickOffTime, homeTeam, awayTeam):
        self.season = season
        self.round = round
        self.venue = venue
        self.kickOffTime = kickOffTime
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
    
    def getSeason(self):
        return self.season
    
    def getRound(self):
        return self.round
    
    def getVenue(self):
        return self.venue
    
    def getKickOffTime(self):
        return self.kickOffTime
    
    def getHomeTeam(self):
        return self.homeTeam
    
    def getAwayTeam(self):
        return self.awayTeam
    
