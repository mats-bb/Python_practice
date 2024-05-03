# Write your code here.

def get_number_of_teams():
    while True:
        try:
            num_teams = int(input("Enter the number of teams in the tournament: "))
        except ValueError:
            print("The number of teams must be an integer, try again.")
        else:

            if num_teams < 2:
                print("The minimum number of teams is 2, try again.")
                continue
            elif not num_teams % 2 == 0:
                print("The number of teams must be even, try again.")

            return num_teams


def get_team_names(num_teams):
    team_names = []

    for i in range(num_teams):
        while True:
            team_name = input(f"Enter the name for team #{i + 1}: ")
            if len(team_name.split(" ")) > 2:
                print("The names may have at most two words, try again.")
                continue
            elif len(team_name.split(" ")) == 1 and len(team_name.split(" ")[0]) < 2:
                print("The names must have at least two characters, try again.")
                continue
            else:
                break

        team_names.append(team_name)

    return team_names


def get_number_of_games_played(num_teams):
    while True:
        num_games_played = input("Enter the number of games played by each team: ")
        try:
            num_games_played = int(num_games_played)
        except ValueError:
            print("The number of games played must be an integer, try again.")
        else:
            if num_games_played < num_teams - 1:
                print("Invalid number of games. Each team plays each other at least once in the regular season. Try again.")
                continue
            
        return num_games_played


def get_team_wins(team_names, games_played):
    team_wins = {}
    for team_name in team_names:
        while True:
            num_wins = input(f"Enter the number of wins Team {team_name} had: ")
            try:
                num_wins = int(num_wins)
            except ValueError:
                print("The number of wins must be an integer, try again.")
            else:
                if num_wins > games_played:
                    print(f"The maximum number of wins is {games_played}, try again.")
                    continue
                elif num_wins < 0:
                    print("The minimum number of wins is 0, try again.")
                    continue
                else:
                    break
                
            team_wins[team_name] = num_wins
                    
    return team_wins

def get_teams_ordered(team_wins):
    ordered_team_names = []

    for team in dict(sorted(team_wins.items(), key=lambda item: item[1], reverse=True)):
        ordered_team_names.append(team)

    return ordered_team_names

def get_tournament_matchups(ordered_team_names):
    
    for i in range(len(ordered_team_names) // 2):
        away = ordered_team_names[i]
        home = ordered_team_names[-(i + 1)]
        print(f"Home: {home} VS Away: {away}")


# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, num_teams)
ordered_teams = get_teams_ordered(team_wins)

print("Generating the games to be played in the first round of the tournament...")

get_tournament_matchups(ordered_teams)
