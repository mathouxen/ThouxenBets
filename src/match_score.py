import argparse
import csv
import data_utils
import features
import scoring

sc = scoring
feat = features
dat = data_utils

listed = []

for fixture in dat.rows[50::]:
    home_team = ["Home"]
    away_team = ["Away"]
    home, away, indexed = dat.fixture(fixture[2], fixture[3])
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

    home_form_score, away_form_score = feat.form_score(
        home_recent_form, away_recent_form
    )

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

    home_team.extend(
        ["Team Strength:", home_strength, "Match Score:", match_score]
    )
    away_team.extend(
        ["Team Strength:", away_strength, "Match Score:", match_score]
    )

    if fixture[4] > fixture[5]:
        difference = int(fixture[4]) - int(fixture[5])
        home_team.extend([f"Won by {difference}"])
        away_team.extend([f"Lost by {difference}"])
    elif fixture[4] < fixture[5]:
        difference = int(fixture[5]) - int(fixture[4])
        home_team.append(f"Lost by {difference}")
        away_team.append(f"Won by {difference}")
    else:
        home_team.append(f"Both teams scored {fixture[4]}")
        away_team.append(f"Both teams scored {fixture[4]}")

    listed.extend([home_team, away_team])

for team in listed:
    print(team)
    if team[0] == "Away":
        print()

