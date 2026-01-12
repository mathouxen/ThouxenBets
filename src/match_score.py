import argparse
import features
import data_utils
import csv
import scoring

sc = scoring
feat = features
dat = data_utils

# arguments = argparse.ArgumentParser(description=f"program that interprets the outcome of a match")

# arguments.add_argument("--home", type=str, required=True)
# arguments.add_argument("--away", type=str, required=True)

# args = arguments.parse_args()
    
# dat.screen(args.home, args.away)
listed = []

for fixture in dat.rows[50::]:
    home_team = ["Home"]
    away_team = ["Away"]
    home, away, indexed = dat.fixture(fixture[3], fixture[4])
    home_team.append(home)
    away_team.append(away)

    (
        home_goals_scored,
        away_goals_scored,
        home_goals_conceded,
        away_goals_conceded,
        home_recent_form,
        away_recent_form,
    ) = feat.stats3(home, away)

    (
        home_avg_goals_scored,
        away_avg_goals_scored,
        home_avg_goals_conceded,
        away_avg_goals_conceded,
    ) = feat.stats2(
        home_goals_scored,
        away_goals_scored,
        home_goals_conceded,
        away_goals_conceded,
    )

    home_team.extend(["Average Goals Scored:", home_avg_goals_scored])
    away_team.extend(["Average Goals Scored:", away_avg_goals_scored])

    home_form_score, away_form_score = feat.form_score(home_recent_form, away_recent_form)

    home_team.extend(["Form Score:", home_form_score])
    away_team.extend(["Form Score:", away_form_score])

    match_score, home_strength, away_strength, delta = sc.teamStrength2(
        home_form_score,
        home_avg_goals_scored,
        home_avg_goals_conceded,
        away_form_score,
        away_avg_goals_scored,
        away_avg_goals_conceded,
    )

    home_team.extend(["Team Strength:", home_strength, "Match Score:", match_score])
    away_team.extend(["Team Strength:", away_strength,"Match Score:", match_score])

    if fixture[5] > fixture[6]:
        difference = int(fixture[5]) - int(fixture[6])
        home_team.extend([f"Won by {difference}"])
        away_team.extend([f"Lost by {difference}"])
    elif fixture[5] < fixture[6]:
        difference = int(fixture[6]) - int(fixture[5])
        home_team.append(f"Lost by {difference}")
        away_team.append(f"Won by {difference}")
    else:
        home_team.append(f"Both teams scored {fixture[5]}")
        away_team.append(f"Both teams scored {fixture[5]}")

    listed.extend([home_team, away_team])

for team in listed:
    print(team)
    if team[0] == "Away":
        print()



# print("                               HOME                            AWAY")
# print(f"                             {home}                         {away}")
# print(f"Last Five Matches: {home_recent_form}          {away_recent_form}")
# print(f"Goals Scored:            {home_goals_scored}                    {away_goals_scored}")
# print(f"Goals Conceded:          {home_goals_conceded}                    {away_goals_conceded}")
# print(f"Average goals scored:          {home_avg_goals_scored}                               {away_avg_goals_scored}")
# print(f"Average goals conceded:        {home_avg_goals_conceded}                               {away_avg_goals_conceded}")
# print(f"Form Score:                     {home_form_score}                                 {away_form_score}")
# print(f"Match Score:                                     {match_score:.2f}")