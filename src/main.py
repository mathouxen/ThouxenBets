import argparse
import features
import data_utils
import csv
import scoring

sc = scoring
feat = features
dat = data_utils

arguments = argparse.ArgumentParser(description=f"program that interprets the outcome of a match")

arguments.add_argument("--home", type=str, required=True)
arguments.add_argument("--away", type=str, required=True)

args = arguments.parse_args()
    
dat.screen(args.home, args.away)

home, away, indexed = dat.fixture(args.home, args.away)
(
    home_goals_scored,
    home_goals_conceded,
    home_recent_form
) = feat.stats(home, indexed)

(
    away_goals_scored,
    away_goals_conceded,
    away_recent_form,
) = feat.stats(away, indexed)

(
    away_avg_goals_scored,
    away_avg_goals_conceded,
) = feat.computed_stats(
    away_goals_scored,
    away_goals_conceded,
)

(
    home_avg_goals_scored,
    home_avg_goals_conceded,
) = feat.computed_stats(
    home_goals_scored,
    home_goals_conceded,
)

home_form_score, away_form_score = feat.form_score(home_recent_form, away_recent_form)

home_team_strength = feat.teamStrength(
    home_form_score,
    home_avg_goals_scored,
    home_avg_goals_conceded
)

away_team_strength = feat.teamStrength(
    away_form_score,
    away_avg_goals_scored,
    away_avg_goals_conceded,
)

match_score = feat.match_score(home_team_strength, away_team_strength)

home_home_form, away_away_form = feat.home_away_run(home, away, indexed)

for match in home_home_form:
    print(match)

print()
print()
print()
for match in away_away_form:
    print(match)

# print("                               HOME                            AWAY")
# print(f"                             {home}                         {away}")
# print(f"Last Five Matches: {home_recent_form}          {away_recent_form}")
# print(f"Goals Scored:            {home_goals_scored}                    {away_goals_scored}")
# print(f"Goals Conceded:          {home_goals_conceded}                    {away_goals_conceded}")
# print(f"Average goals scored:          {home_avg_goals_scored}                               {away_avg_goals_scored}")
# print(f"Average goals conceded:        {home_avg_goals_conceded}                               {away_avg_goals_conceded}")
# print(f"Form Score:                     {home_form_score}                                 {away_form_score}")
# print(f"Match Score:                                     {match_score:.2f}")