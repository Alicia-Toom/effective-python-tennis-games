
class TennisGame2:
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
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        """Count the current score and return the result"""
        result = ""
        # Handle case when both players have the same score before reaching fourty
        if (self.p1points == self.p2points and self.p1points < 3):
            if (self.p1points==0):
                result = "Love"
            if (self.p1points==1):
                result = "Fifteen"
            if (self.p1points==2):
                result = "Thirty"
            result += "-All"
        # Handle case when both players have the same score at fourty
        if (self.p1points==self.p2points and self.p1points>2):
            result = "Deuce"
        P1res = ""
        P2res = ""
        # Handle case when player 1 start getting the score than 0, but the players 2 has 0
        if (self.p1points > 0 and self.p2points==0):
            if (self.p1points==1):
                P1res = "Fifteen"
            if (self.p1points==2):
                P1res = "Thirty"
            if (self.p1points==3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        # Handle case when player 2 start getting the score than 0, but the players 1 has 0
        if (self.p2points > 0 and self.p1points==0):
            if (self.p2points==1):
                P2res = "Fifteen"
            if (self.p2points==2):
                P2res = "Thirty"
            if (self.p2points==3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res
        # Handle case when player 1 has higher score than player 2
        if (self.p1points>self.p2points and self.p1points < 4):
            if (self.p1points==2):
                P1res="Thirty"
            if (self.p1points==3):
                P1res="Forty"
            if (self.p2points==1):
                P2res="Fifteen"
            if (self.p2points==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        # Handle case when player 2 has higher than player 1
        if (self.p2points>self.p1points and self.p2points < 4):
            if (self.p2points==2):
                P2res="Thirty"
            if (self.p2points==3):
                P2res="Forty"
            if (self.p1points==1):
                P1res="Fifteen"
            if (self.p1points==2):
                P1res="Thirty"
            result = P1res + "-" + P2res
        # Handle case when duece and player 1 has higher score than player 2
        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name
         # Handle case when duece and player 2 has higher score than player 1
        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name
         # Handle case when player 1 has more than 2 points than player 2
        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            result = "Win for " + self.player1Name
         # Handle case when player 2 has more than 2 points than player 1
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        """Calculate the score for player 1"""
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        """Calculate the score for player 2"""
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        """Increase the score by 1 point for player 1"""
        self.p1points +=1

    def P2Score(self):
        """Increase the score by 1 point for player 2"""
        self.p2points +=1