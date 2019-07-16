import sqlite3
import datetime


class Database:
    def __init__(self):
        con = sqlite3.connect('database.sqlite')
        cur = con.cursor()
        # create database if isn't exist
        try:
            query = """CREATE TABLE players (
        username VARCHAR NOT NULL,
        firstname VARCHAR,
        lastname VARCHAR,
        gender VARCHAR,
        wins INT,
        defeats INT,
        PRIMARY KEY(username))"""
            cur.execute(query)
            con.commit()
        except:
            pass

        try:
            query = 'CREATE TABLE leagues (date DATE, winner VARCHAR, looser VARCHAR, playersnumber INT)'
            cur.execute(query)
            con.commit()
        except:
            pass

        con.close()

    def add_player(self, username, firstname, lastname, gender):
        con = sqlite3.connect('database.sqlite')
        cur = con.cursor()
        try:
            query = "INSERT INTO players VALUES ('{0}', '{1}', '{2}', '{3}', 0, 0)".format(username, firstname,                                                                                         lastname, gender)
            cur.execute(query)
            con.commit()
            print("Player added.")
        except Exception as e:  # catch all errors, if error is that username exists print msg
            if str(e) == 'UNIQUE constraint failed: players.username':
                print("Username '{0}' is already taken.".format(username))
            else:
                print("Error! Try again.")
        finally:
            con.close()

    def get_players(self):
        con = sqlite3.connect("database.sqlite")
        cur = con.cursor()

        try:
            query = "SELECT * FROM players"
            cur.execute(query)
            players = cur.fetchall()
            return players
        except:
            print("Error! Try again later.")
        finally:
            con.close()

    # function to show all leagues
    def get_leagues(self):
        con = sqlite3.connect("database.sqlite")
        cur = con.cursor()

        try:
            query = "SELECT * FROM leagues"
            cur.execute(query)
            leagues = cur.fetchall()
            return leagues
        except:
            print("Error! Try again later.")
        finally:
            con.close()

    # function to add a league
    def add_league(self, winner, looser, players):
        con = sqlite3.connect('database.sqlite')
        cur = con.cursor()
        try:
            date = datetime.datetime.now().strftime("%x")
            query = "INSERT INTO leagues VALUES ('{0}', '{1}', '{2}', '{3}')".format(date, winner, looser, players)
            cur.execute(query)
            con.commit()
            print("League added.")
        except Exception as e:
            print(e)
        finally:
            con.close()

    # to update player wins by 1
    def update_player_wins(self, winner):
        con = sqlite3.connect('database.sqlite')
        cur = con.cursor()
        try:
            query = """
UPDATE Players
SET wins = wins + 1
WHERE username = '{}'""".format(winner)
            cur.execute(query)
            con.commit()
            print("Player updated!")
        except Exception as e:
            print(e)
        finally:
            con.close()

    # function to update player defeats by 1
    def update_player_defeats(self, looser):
        con = sqlite3.connect('database.sqlite')
        cur = con.cursor()
        try:
            query = """
        UPDATE players
        SET defeats = defeats + 1
        WHERE username = '{}'""".format(looser)
            cur.execute(query)
            con.commit()
            print("Player updated!")
        except Exception as e:
            print(e)

        finally:
            con.close()
