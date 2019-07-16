from Control.Controls import *


# main menu
def show_menu():
    # set global vars
    global list_of_players
    global list_of_leagues

    print("""-------------------------------
1. Show Leagues
2. Add League
3. Show Players
4. Add Player
0. Exit
-------------------------------""")
    print("Select Menu (0-4):")

    # check if input is right
    x = input()
    if x.isdigit():
        x = int(x)

    # while until input is valid number
    while x != 1 and x != 2 and x != 3 and x != 4 and x != 0:
        print("Wrong input. Select Menu (0-4):")
        x = input()
        if x.isdigit():
            x = int(x)
        else:
            x = -1

    if x == 1:  # show leagues
        for l in list_of_leagues:
            l.to_string()

        show_menu()
    elif x == 2:  # add league
        # input fields
        print("Winner: ")
        winner = input()
        print("Looser: ")
        looser = input()
        print("Number of players: ")
        players = input()

        db.update_player_wins(winner)
        db.update_player_defeats(looser)
        db.add_league(winner, looser, players)
        list_of_leagues = get_leagues()

        show_menu()
    elif x == 3:    # show players
        # sort players with wins
        list_of_players.sort(reverse=True, key=sort_players)

        for p in list_of_players:
            p.to_string()

        show_menu()
    elif x == 4:  # add new player
        # input fields
        print("Username: ")
        username = input()
        print("Firstname: ")
        firstname = input()
        print("LastName: ")
        lastname = input()
        print("Gender: ")
        gender = input()

        db.add_player(username, firstname, lastname, gender)  # call method to add player to database
        list_of_players = get_players()  # call method to get new players from database
        show_menu()
    elif x == 0:    # end program
        pass


# start program
if __name__ == "__main__":
    db = Database()     # create object database
    list_of_players = get_players()   # call method to get players from database
    list_of_leagues = get_leagues()   # call method to get leagues from database

    show_menu()  # call method to show the main menu
