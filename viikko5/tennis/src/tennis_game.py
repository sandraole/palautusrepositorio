class TennisGame:

    scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._get_tied_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self._get_winning_score()
        else:
            return self._get_inaction_score()

    def _get_tied_score(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        return "Deuce"

    def _get_winning_score(self):
        score_different = self.player1_score - self.player2_score
        if score_different == 1:
            return f"Advantage {self.player1_name}"
        elif score_different == -1:
            return f"Advantage {self.player2_name}"
        elif score_different >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _get_inaction_score(self):
        return f"{self.scores[self.player1_score]}-{self.scores[self.player2_score]}"
