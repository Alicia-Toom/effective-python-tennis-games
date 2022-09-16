class TennisGame1:
    """
    Represent a tennis game with two players keeping track
    of the score of a single game.
    """

    def __init__(self, player1Name, player2Name):
        """Initialize with player name and starting score"""
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        """Add one point to the score of the playerName argument"""
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1
    
    def score(self):
        """Count the current score and return the result"""
        result = ""
        tempScore=0
        # Handle case when both players have the same score
        if (self.p1points==self.p2points):
            result = {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(self.p1points, "Deuce")
        # Handle case when at least one player has reached the score of 40 
        elif (self.p1points>=4 or self.p2points>=4):
            minusResult = self.p1points-self.p2points
            if (minusResult==1):
                result ="Advantage " + self.player1Name
            elif (minusResult ==-1):
                result ="Advantage " + self.player2Name
            elif (minusResult>=2):
                result = "Win for " + self.player1Name
            else:
                result ="Win for " + self.player2Name
        # Handle case when game is still unfinished
        else:
            # Use a foor-loop to iterate both players to create the result
            for i in range(1,3):
                if (i==1):
                    tempScore = self.p1points
                else:
                    result+="-"
                    tempScore = self.p2points
                result += {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }[tempScore]
        return result