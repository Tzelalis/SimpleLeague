class League:
    def __init__(self, date, winner, looser, players):
        self.date = date
        self.winner = winner
        self.looser = looser
        self.players = players
        self.id = id

    def to_string(self):
        print("""
No: {4} Date: {0} Players: {1}
Winner: {2} Looser: {3}""".format(self.date, self.players, self.winner, self.looser, self.id))
