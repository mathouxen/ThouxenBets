import data_utils 

dat = data_utils

# Getting goals scored, goals conceded, recent form   

def stats(team, indexed):
    goals_scored = []
    goals_conceded = []
    recent_form = []
    

    for row in dat.rows[indexed - 2::-1]:
        if len(goals_scored) == 5:
            break

        if row[2] == team:
            if len(goals_scored) < 5:
                goals_scored.append(int(row[4]))
                goals_conceded.append(int(row[5]))

            if row[6] == "H":
                recent_form.append("W")
            elif row[6] == "D":
                recent_form.append("D")
            else:
                recent_form.append("L")
        if row[3] == team:
            if len(goals_scored) < 5:
                goals_scored.append(int(row[5]))
                goals_conceded.append(int(row[4]))

            if row[6] == "H":
                recent_form.append("L")
            elif row[6] == "D":
                recent_form.append("D")
            else:
                recent_form.append("W")

    return goals_scored, goals_conceded, recent_form

def stats3(team):
    goals_scored, goals_conceded, recent_form = [], [], []

    for row in dat.rows:
        if len(goals_scored) == 5:
            break

        if row[2] == team:
            if len(goals_scored) < 5:
                goals_scored.append(int(row[4]))
                goals_conceded.append(int(row[5]))

            if row[6] == "H":
                recent_form.append("W")
            elif row[6] == "D":
                recent_form.append("D")
            else:
                recent_form.append("L")
        if row[3] == team:
            if len(goals_scored) < 5:
                goals_scored.append(int(row[5]))
                goals_conceded.append(int(row[4]))

            if row[6] == "H":
                recent_form.append("L")
            elif row[6] == "D":
                recent_form.append("D")
            else:
                recent_form.append("W")
    return goals_scored, goals_conceded, recent_form

def computed_stats(goals_scored, goals_conceded):

    if len(goals_scored) != 0:
        avg_goals_scored = sum(goals_scored) / len(goals_scored)
    else:
        avg_goals_scored = 0

    if len(goals_conceded) != 0:
        avg_goals_conceded = sum(goals_conceded) / len(goals_conceded)
    else:
        avg_goals_conceded = 0

    return avg_goals_scored, avg_goals_conceded

def form_score(home_recent_form, away_recent_form):

    # Calculating the form score
    home_form_score = []
    away_form_score = []

    for result in home_recent_form:
        if result == "W":
            home_form_score.append(3)
        elif result == "D":
            home_form_score.append(1)

    for result in away_recent_form:
        
        if result == "W":
            away_form_score.append(3)
        elif result == "D":
            away_form_score.append(1)

    if len(home_form_score) == 0 and len(away_form_score) == 0:
        return 0, 0
    elif len(home_form_score) == 0:
        return 0, sum(away_form_score) / len(away_form_score)
    elif len(away_form_score) == 0:
        return sum(home_form_score) / len(home_form_score), 0
    else:
        return sum(home_form_score) / len(home_form_score), sum(away_form_score) / len(away_form_score)


# Team Strength = form + attack - defense + context


def teamStrength(form_score, avg_goals_scored, avg_goals_conceded):
   team_strength =  form_score + avg_goals_scored - avg_goals_conceded
   return team_strength

def match_score(home_team_strength, away_team_strength):
    return home_team_strength - away_team_strength

# Calculating the home team's recent home form and away team's recent away form
## Returns expected points to score using past results

def home_and_away(home, away, indexed, rows):
    home_score = 0
    away_score = 0
    home_instance = 0
    away_instance = 0
    home_form_list = []
    away_form_list = []
    for row in rows[indexed - 2::-1]:
        if home_instance == 5:
            break
        if row[2] == home:
            home_instance += 1
            if row[6] == "H":
                home_form_list.append(row[6])
                home_score += 3
            elif row[6] == "D":
                home_form_list.append(row[6])
                home_score += 1
            else:
                home_form_list.append("loss")
    for row in rows[indexed - 2::-1]:
        if away_instance == 5:
            break
        if row[3] == away:
            away_instance += 1
            if row[6] == "A":
                away_form_list.append(row[6])
                away_score += 3
            elif row[6] == "D":
                away_form_list.append(row[6])
                away_score += 1
            else:
                away_form_list.append("loss")

    home_expected_result = home_score / 5
    away_expected_result = away_score / 5
    print(home_form_list)
    print(away_form_list)

    return home_expected_result, away_expected_result

def home_away_run(home, away, indexed):
    home_home_results = {}
    away_away_results = {}
    home_listed = []
    away_listed = []
    matchday_a = 1
    matchday_h = 1
    for row in dat.rows[indexed - 2::-1]:
        if matchday_a == 5 and matchday_h == 5:
            break

        if row[2] == home:
            home_home_results["Home"] = row[2]
            home_home_results["Matchday"] = matchday_h
            home_home_results["Opponent"] = row[3]
            home_home_results["Goals Scored"] = row[4]
            home_home_results["Goals Conceded"] = row[5]
            home_home_results["Final Result"] = row[6]
            home_listed.append(home_home_results.copy())
            matchday_h += 1

        if row[3] == away:
            away_away_results["Away"] = row[3]
            away_away_results["Matchday"] = matchday_a
            away_away_results["Opponent"] = row[2]
            away_away_results["Goals Scored"] = row[5]
            away_away_results["Goals Conceded"] = row[4]
            away_away_results["Final Result"] = row[6]
            away_listed.append(away_away_results.copy())
            matchday_a += 1
    return home_listed, away_listed

        








