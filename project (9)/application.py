import constants
import copy
import sys

teams_copy = copy.deepcopy(constants.TEAMS)
players_copy = copy.deepcopy(constants.PLAYERS)
teams_filled = dict()


def clean_data():
    for player in players_copy:
        player_height = player["height"].split()
        player_height.remove("inches")
        player_height = (map(int, player_height))
        False if player["experience"] == 'No' else True
    for guardian in players_copy:
        guardians_list = guardian["guardians"].split()


def greeting_screen():
    print("\nBASKETBALL STATS DATABASE\n")
    print("CHOICES: \n")
    print("1. Display Stats")
    print("2. Quit\n")


def balance_teams():
    for team in teams_copy:
        teams_filled[team] = list()

    team_count = 0
    for player in players_copy:
        if((len(teams_filled[teams_copy[team_count]])) == (len(players_copy)/len(teams_copy))):
            team_count += 1
        present_team = teams_filled[teams_copy[team_count]]
        present_team.append(player)

    while True:
        try:
            user_choice = int(input("Enter an option('1' to display stats or '2' to quit): "))
            if (user_choice == 1):
                print("\n --Teams--\n")

                for index, team in enumerate(teams_copy, 1):
                    print(f'{index}. {team}')

                while True:
                    try:
                        team_choice = int(input("\nChoose a team --> "))
                        if team_choice < 1 or team_choice > 3:
                            print("That is not a valid entry. Please enter a valid number")
                            continue
                        print("\nTeam: %s " % (teams_copy[team_choice - 1]))
                        print(" ".join(["No. of Players: ", str(len(teams_filled[teams_copy[0]]))]))
                        print("\nPlayers: ")
                        players_on_team = []
                        for player in teams_filled[teams_copy[team_choice - 1]]:
                            players_on_team.append(player['name'])
                        print(*players_on_team, sep=", ")
                        print("\nGuardians: ")
                        guardians_list = []
                        for guardian in teams_filled[teams_copy[team_choice - 1]]:
                            guardians_list.append(guardian["guardians"])
                        print(*guardians_list, sep=", ")
                        print()
                        break
                    except ValueError:
                        print("That is not a valid entry. Please enter a valid number")
                    break
            elif user_choice == 2:
                print("Thank you! You have exited the program.")
                sys.exit()
            else:
                print("That is not a valid entry. Please enter a valid number")
        except ValueError:
            print("That is not a valid entry. Please enter a valid number")


if __name__ == "__main__":
    clean_data()
    greeting_screen()
    balance_teams()
