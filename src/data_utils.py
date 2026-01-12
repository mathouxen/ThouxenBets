import sys
import csv


with open('../data/E0.csv', newline="") as csvfile:
    reader = csv.reader(csvfile, )

    rows = list(reader)

# Checking to see whether the teams are actually present in the given epl season

def screen(home, away):
    home_team = False
    away_team = False
    for row in rows:
        if row[3].lower() == home.lower():
            home_team = True
        if row[3].lower() == away.lower():
            away_team = True
        
    if not home_team:
        sys.exit(f"{home} is not in the 24/25 Premier League season")
    if not away_team:
        sys.exit(f"{away} is not in the 24/25 Premier League season")

# Finding the exact fixture that we want of the season

# h_team = str()
# a_team = str()
def fixture(home, away):
    for i, row in enumerate(rows):
        if row[3].lower() == home.lower() and row[4].lower() == away.lower():
            h_team = row[3]
            a_team = row[4]
            # print(f"Home: {row[3]}")
            # print(f"Away: {row[4]}")
            indexed = i
            return h_team, a_team, indexed
        

# print(rows[:5])