""" TODO """

from typing import Dict

# pylint: disable=too-few-public-methods
class Player():
    """ TODO """

    def __init__(self, name):
        self.name = name

class TennisGame():
    """ TODO """

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.score_card: Dict[Player, int] = {player1: 0, player2: 0}

    def add_point_to_player(self, player: Player):
        """Add one point to the score of the player argument"""
        self.score_card[player] = self.score_card[player] + 1

    def get_current_score(self):
        """Count the current score and return the result"""
        result = ""
        player1_score = self.score_card[self.player1]
        player2_score = self.score_card[self.player2]
        score_terms: Dict[int, str] = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Fourty"}

        if player1_score == player2_score:
            if player1_score >= 4:
                result = "Deuce"
            else:
                result = f"{score_terms[player1_score]} - All"
        else:
            if player1_score >= 4 and (player1_score - player2_score == 1):
                result = f"Advantage for {self.player1.name}"
            elif player2_score >= 4 and (player2_score - player1_score == 1):
                result = f"Advantage for {self.player2.name}"
            if player1_score >= 4 and (player1_score - player2_score >= 2):
                result = f"Win for {self.player1.name}"
            elif player2_score >= 4 and (player2_score - player1_score >= 2):
                result = f"Win for {self.player2.name}"
            else:
                result = f"{score_terms[player1_score]} - {score_terms[player2_score]}"

        return result

if __name__ == "__main__":
    player_alicia = Player("Alicia")
    player_federer = Player("Federer")
    # Create new game between Alicia and Nadal
    game = TennisGame(player_alicia, player_federer)

    # Love all as a start
    print(game.get_current_score())

    # Fifteen - Love
    game.add_point_to_player(player_alicia)
    print(game.get_current_score())

    # Thirty - Love
    game.add_point_to_player(player_alicia)
    print(game.get_current_score())

    # Thirty - Fifteen
    game.add_point_to_player(player_federer)
    print(game.get_current_score())

    # Forty - Fifteen
    game.add_point_to_player(player_alicia)
    print(game.get_current_score())

    # Alicia Winner
    game.add_point_to_player(player_alicia)
    print(game.get_current_score())
