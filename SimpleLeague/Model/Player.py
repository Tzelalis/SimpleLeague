from Model.Person import Person


class Player(Person):
    def __init__(self, username, firstname, lastname, gender, wins=0, defeats=0):
        Person.__init__(self, lastname, firstname, gender)
        self.wins = wins
        self.defeats = defeats
        self.username = username

    def to_string(self):
        print("""
Username: {0}
Fullname: {1} {2}
Wins: {3}
Defeats: {4}""".format(self.username, self.firstname, self.lastname, self.wins, self.defeats))
    print("")
