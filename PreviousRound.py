from CurrentRound import CurrentRound

class PreviousRound(CurrentRound):
    """
    :param season: the season in which the match was played
    :param round: the round in which the match was played
    :param venue: the venue that the match was played at
    :param kickOffTime: the kick off time of the match
    :param homeTeam: the home team
    :param homeScore: how many points the home team scored
    :param homeCompletionPercent: the home teams completion rate in percentage
    :param homeTacklePercent: the home teams successful tackle rate in percentage
    :param awayTeam: the away team
    :param awayScore: how many points the away team scored
    :param awayCompletionPercent: the away teams completion rate in percentage
    :param awayTacklePercent: the away teams successful tackle rate in percentage
    """
    def __init__(self, season, round, venue, kickOffTime, homeTeam, homeScore, homeCompletionPercent, homeTacklePercent, awayTeam, awayScore, awayCompletionPercent, awayTacklePercent):
        super().__init__(season, round, venue, kickOffTime, homeTeam, awayTeam)
        self.homeScore = homeScore
        self.homeCompletionPercent = homeCompletionPercent
        self.homeTacklePercent = homeTacklePercent
        self.awayScore = awayScore
        self.awayCompletionPercent = awayCompletionPercent
        self.awayTacklePercent = awayTacklePercent

    """
    :returns: the amount of points the home team scored
    """
    def getHomeScore(self):
        return self.homeScore

    """
    :returns: the home teams completion percentage
    """
    def getHomeCompletion(self):
        return self.homeCompletionPercent

    """
    :returns: the home teams tackling percentage
    """
    def getHomeTacklePercentage(self):
        return self.homeTacklePercent
    
    """
    :returns: the amount of points the away team scored
    """
    def getAwayScore(self):
        return self.awayScore
    
    """
    :returns: the away teams completion percentage
    """
    def getAwayCompletion(self):
        return self.awayCompletionPercent

    """
    :returns: the away teams tackling percentage
    """
    def getAwayTacklePercentage(self):
        return self.awayTacklePercent
    
