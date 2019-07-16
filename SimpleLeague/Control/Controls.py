from Model.Player import Player
from Model.League import League
from Control.Database import Database

db = Database()  # create database object


# return all players from database to list of Players
def get_players():
    players = []
    players_fetchall = db.get_players()  # call method to get a list with all players from database
    for row in players_fetchall:
        # username, firstname, lastname, gender, wins, defeats
        players.append(Player(row[0], row[1], row[2], row[3], row[4]))

    return players


# return all leagues from database to list of Leagues
def get_leagues():
    leagues = []
    leagues_fetchall = db.get_leagues()  # call method to get a list with all leagues from database

    for row in leagues_fetchall:
        #date, players, winner, looser
        leagues.append(League(row[0], row[1], row[2], row[3]))

    return leagues


def sort_players(player):
    return player.wins
