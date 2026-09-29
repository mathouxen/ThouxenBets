import sys
import csv


with open('data/premier_league_clean.csv', newline="") as csvfile:
    reader = csv.reader(csvfile)

    rows = list(reader)

# Checking to see whether the teams are actually present in the given epl season
def screen(home, away):
    home_team = False
    away_team = False
    for row in rows:
        if row[2].lower() == home.lower():
            home_team = True
        if row[2].lower() == away.lower():
            away_team = True
        
    if not home_team:
        sys.exit(f"{home} is not in the 24/25 Premier League season")
    if not away_team:
        sys.exit(f"{away} is not in the 24/25 Premier League season")

# Finding the exact fixture that we want of the season
def fixture(home, away):
    for i, row in reversed(list(enumerate(rows))):
        if row[2].lower() == home.lower() and row[3].lower() == away.lower():
            h_team = row[2]
            a_team = row[3]
            indexed = i
            print(indexed)
            return h_team, a_team, indexed
  