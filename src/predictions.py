import features
import data_utils
import scoring

sc = scoring
feat = features
dat = data_utils

listed = []
correct = []
incorrect = []
draw = []

for fixture in dat.rows[50::]:
    # Making a list that will have the stats of each team in the fixture
    home_team = ["Home"]
    away_team = ["Away"]
    home, away, indexed = dat.fixture(fixture[3], fixture[4])
    # Adding names to the list of each team in the fixture
    home_team.append(home)
    away_team.append(away)

    # Calculating some stats on the teams, that will add to the list


    # Home team stats
    (
        home_goals_scored,
        home_goals_conceded,
        home_recent_form,
    ) = feat.stats(home, indexed)

    # Away team stats
    (
        away_goals_scored,
        away_goals_conceded,
        away_recent_form
    ) = feat.stats(away, indexed)

    # Home team average stats
    (
        home_avg_goals_scored,
        home_avg_goals_conceded,  
    ) = feat.computed_stats(
        home_goals_scored,
        home_goals_conceded,
    )

    # Away team average stats
    (
        away_avg_goals_scored,
        away_avg_goals_conceded,  
    ) = feat.computed_stats(
        away_goals_scored,
        away_goals_conceded,
    )

    # Adding some calculated stats

    home_team.extend(["Average Goals Scored:", home_avg_goals_scored])
    away_team.extend(["Average Goals Scored:", away_avg_goals_scored])

    home_form_score, away_form_score = feat.form_score(home_recent_form, away_recent_form)

    home_team.extend(["Form Score:", home_form_score])
    away_team.extend(["Form Score:", away_form_score])

    # The team strength of the home team
    home_team_strength = feat.teamStrength(
        home_form_score,
        home_avg_goals_scored,
        home_avg_goals_conceded
    )

    # The team strength of the away team
    away_team_strength = feat.teamStrength(
        away_form_score,
        away_avg_goals_scored,
        away_avg_goals_conceded,
    )

    match_score = abs(feat.match_score(home_team_strength, away_team_strength))
    delta = feat.match_score(home_team_strength, away_team_strength)


    home_team.extend(["Team Strength:", home_team_strength, "Match Score:", match_score])
    away_team.extend(["Team Strength:", away_team_strength,"Match Score:", match_score])

    

    # Adding the results to each list

    difference = int()
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

    # Adding both lists to the "listed" list.
    listed.extend([home_team, away_team])

    # Checking to see how accurate predictions for each fixture would've been using the match score only, 
    # and adding correct and incorrect predictions to their respective lists

    if delta < 0:
        # This means that the home team is weaker per team strength
        if fixture[5] > fixture[6]: # This means that the home team won even though the team strenth difference favoured the away
            incorrect.append(["Difference", delta, "Match Score", match_score, "Score", f"{fixture[5]} - {fixture[6]}", "home"])
        elif fixture[5] < fixture[6]: # This means that the away team away team won, meaning the delta got it right
            correct.append(["Difference", delta, "Match Score", match_score, "Score", f"{fixture[5]} - {fixture[6]}", "away"])
        # else:
            # incorrect.append(["Difference", delta, "Match Score", match_score, "Score", f"{fixture[5]} - {fixture[6]}", "draw"])

    if delta > 0:
        # This means that the home team is stronger per team strength
        if fixture[5] > fixture[6]: # This means that the home team won like the team strength suggested
            correct.append(["Difference", delta, "Match Score", match_score, "Score", f"{fixture[5]} - {fixture[6]}", "home"])
        elif fixture[5] < fixture[6]: # This means that the home team lost, even though the team strength suggested otherwise
            incorrect.append(["Difference", delta, "Match Score", match_score, "Score", f"{fixture[5]} - {fixture[6]}", "away"])
        # else:
            # incorrect.append(["Difference", delta, "Match Score", match_score, "Score", f"{fixture[5]} - {fixture[6]}", "draw"])        

    if delta == 0:
        # This means that the home and away team are evenly matched per the team strength metric
        if fixture[5] > fixture[6]: #This means that the home team managed to win even though the team Strenght metric favoured a draw
            incorrect.append(["Difference", delta, "Match Score", match_score, "Score", f"{fixture[5]} - {fixture[6]}", "home"])
        elif fixture[5] < fixture[6]: # This means that the away team won even though the team strength metric favoured a draw
            incorrect.append(["Difference", delta, "Match Score", match_score, "Score", f"{fixture[5]} - {fixture[6]}", "away"])
        # else:
            # correct.append(["Difference", delta, "Match Score", match_score, "Score", f"{fixture[5]} - {fixture[6]}", "draw"])

counter = 0
# for team in listed:
#     counter += 1
#     print(team)
#     if team[0] == "Away":
#         print()

for this in incorrect:
    if this[-1] == "home":
        counter += 1
    
incorrect_home_percentage = (counter / len(incorrect)) * 100

correct_percentage = (len(correct) / (len(correct) + len(incorrect))) * 100
incorrect_percentage = (len(incorrect) / (len(correct) + len(incorrect))) * 100

print(f"Correct percentage {correct_percentage:.2f} %")
print(f"Incorrect percentage {incorrect_percentage:.2f} %")
print(f"Incorrect home percentage: {incorrect_home_percentage:.2f}%")




print("                               HOME                            AWAY")
print(f"                             {home}                         {away}")
print(f"Last Five Matches: {home_recent_form}          {away_recent_form}")
print(f"Goals Scored:            {home_goals_scored}                    {away_goals_scored}")
print(f"Goals Conceded:          {home_goals_conceded}                    {away_goals_conceded}")
print(f"Average goals scored:          {home_avg_goals_scored}                               {away_avg_goals_scored}")
print(f"Average goals conceded:        {home_avg_goals_conceded}                               {away_avg_goals_conceded}")
print(f"Form Score:                     {home_form_score}                                 {away_form_score}")
print(f"Match Score:                                     {match_score:.2f}")