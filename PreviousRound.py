from CurrentRound import CurrentRound

class PreviousRound(CurrentRound):
    """
    :param season: the season in which the match was played
    :param round: the round in which the match was played
    :param venue: the venue that the match was played at
    :param kickOffTime: the kick off time of the match
    :param homeTeam: the home team
    :param homeScore: how many points the home team scored
    :param awayTeam: the away team
    :param awayScore: how many points the away team scored
    """
    def __init__(self, season, round, venue, kickOffTime, homeTeam, homeScore, awayTeam, awayScore):
        super().__init__(season, round, venue, kickOffTime, homeTeam, awayTeam)
        self.homeScore = homeScore
        self.awayScore = awayScore

    """
    :returns: the amount of points the home team scored
    """
    def getHomeScore(self):
        return self.homeScore
    
    """
    :returns: the amount of points the away team scored
    """
    def getAwayScore(self):
        return self.awayScore
