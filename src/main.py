import sys
import argparse
import csv

arguments = argparse.ArgumentParser(description=f"program that interprets the outcome of a match")

arguments.add_argument("--home", type=str, required=True)
arguments.add_argument("--away", type=str, required=True)

args = arguments.parse_args()

with open('data/E0.csv', newline="") as csvfile:
    reader = csv.reader(csvfile, )

    rows = list(reader)
    print(rows[1:10])

# Checking to see whether the teams are actually present in the given epl season

home_team = False
away_team = False
for row in rows:
    print(row[3])
    if row[3].lower() == args.home.lower():
        home_team = True
    if row[3].lower() == args.away.lower():
        away_team = True
    
if not home_team:
    sys.exit(f"{args.home} is not in the 24/25 Premier League season")
if not away_team:
    sys.exit(f"{args.away} is not in the 24/25 Premier League season")

# Finding the exact fixture that we want of the season

for i, row in enumerate(rows):
    if row[3].lower() == args.home.lower() and row[4].lower() == args.away.lower():
        home_team = row[3]
        away_team = row[4]
        print(f"Home: {row[3]}")
        print(f"Away: {row[4]}")
        indexed = i
        break
        
    
# Getting the goals scored, conceded, recent form of each team  

home_goals_scored = []
home_goals_conceded = []
away_goals_scored = []
away_goals_conceded = []
home_recent_form = []
away_recent_form = []

for row in rows[indexed - 1::-1]:
    if len(home_goals_scored) == 5 and len(away_goals_scored) == 5:
        break

    if row[3] == home_team:
        if len(home_goals_scored) < 5:
            home_goals_scored.append(int(row[5]))
            home_goals_conceded.append(int(row[6]))

        if row[7] == "H":
            home_recent_form.append("W")
        elif row[7] == "D":
            home_recent_form.append("D")
        else:
            home_recent_form.append("L")
    if row[4] == home_team:
        if len(home_goals_scored) < 5:
            home_goals_scored.append(int(row[6]))
            home_goals_conceded.append(int(row[5]))

        if row[7] == "H":
            home_recent_form.append("L")
        elif row[7] == "D":
            home_recent_form.append("D")
        else:
            home_recent_form.append("W")

    if row[3] == away_team:
        if len(away_goals_scored) < 5:
            away_goals_scored.append(int(row[5]))
            away_goals_conceded.append(int(row[6]))

            if row[7] == "H":
                away_recent_form.append("W")
            elif row[7] == "D":
                away_recent_form.append("D")
            else:
                away_recent_form.append("L")

    if row[4] == away_team:
        if len(away_goals_scored) < 5:
            away_goals_scored.append(int(row[6]))
            away_goals_conceded.append(int(row[5]))

        if row[7] == "H":
            away_recent_form.append("L")
        elif row[7] == "D":
            away_recent_form.append("D")
        else:
            away_recent_form.append("W")

if len(home_goals_scored) != 0:
    home_avg_goals_scored = sum(home_goals_scored) / len(home_goals_scored)
else:
    home_avg_goals_scored = 0

if len(away_goals_scored) != 0:
    away_avg_goals_scored = sum(away_goals_scored) / len(away_goals_scored)
else: 
    away_avg_goals_scored = 0

if len(home_goals_conceded) != 0:
    home_avg_goals_conceded = sum(home_goals_conceded) / len(home_goals_conceded)
else:
    home_avg_goals_conceded = 0

if len(away_goals_conceded) != 0:
    away_avg_goals_conceded = sum(away_goals_conceded) / len(away_goals_conceded)
else:
    away_avg_goals_conceded = 0


# Calculating the form score
home_form_score = 0
away_form_score = 0

for result in home_recent_form:
    if result == "W":
        home_form_score = home_form_score + 3
    elif result == "D":
        home_form_score = home_form_score + 1

for result in away_recent_form:
    
    if result == "W":
        away_form_score = away_form_score + 3
    elif result == "D":
        away_form_score = away_form_score + 1
    


print("                               HOME                            AWAY")
print(f"                             {home_team}                         {away_team}")
print(f"Last Five Matches: {home_recent_form}          {away_recent_form}")
print(f"Goals Scored:            {home_goals_scored}                    {away_goals_scored}")
print(f"Goals Conceded:          {home_goals_conceded}                    {away_goals_conceded}")
print(f"Average goals scored:          {home_avg_goals_scored}                              {away_avg_goals_scored}")
print(f"Average goals conceded:        {home_avg_goals_conceded}                              {away_avg_goals_conceded}")
print(f"Form Score:                         {home_form_score}              {away_form_score}")