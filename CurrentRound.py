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

    """
    :returns: the season in which the match was played
    """
    def getSeason(self):
        return self.season

    """
    :returns: the round in which the match was played
    """ 
    def getRound(self):
        return self.round

    """
    :returns: the venue that the match was played at
    """ 
    def getVenue(self):
        return self.venue
    
    """
    :returns: the time of kick off of the match
    """    
    def getKickOffTime(self):
        return self.kickOffTime
    
    """
    :returns: the home team that played in the match
    """ 
    def getHomeTeam(self):
        return self.homeTeam
    
    """
    :returns: the away team that played in the match
    """ 
    def getAwayTeam(self):
        return self.awayTeam
    
