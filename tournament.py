# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000

def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    with open(sys.argv[1], 'r') as file:
        # read as dict
        reader = csv.DictReader(file)
        for team in reader:
            # make sure rating is an integer
            team["rating"] = int(team["rating"])
            # insert team dcts to teams
            teams.append(team)

    counts = {}

    # set each teams scores to 0
    for every_team in teams:
        team = every_team['team']
        counts[team] = 0
    # TODO: Simulate N tournaments and keep track of win counts
    for winner in range(N):
        winner = simulate_tournament(teams)
        # keep track of their win
        if winner in counts:
            counts[winner] += 1

    print(counts)
    
    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    winner = simulate_round(teams)
    # if the len not 1 keep simulate
    while len(winner) > 1:
        winner = simulate_round(winner)

    # get only the name of the winning team
    for every_winner in winner:
        name_winning_team = every_winner['team']    

    # return the final winning team
    return name_winning_team

if __name__ == "__main__":
    main()
