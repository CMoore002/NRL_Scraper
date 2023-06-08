class CurrentRound:
    """
    :param season: the season in which the match was played
    :param round: the round in which the match was played
    :param venue: the venue that the match was played at
    :param kickOffTime: the kick off time of the match
    :param homeTeam: the home team
    :param awayTeam: the away team
    """
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
    
