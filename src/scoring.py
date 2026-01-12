import features

feat = features

# Using the functions from the features file to make some calculations

# Calculating the home ground advantage and the away disadvantage of each team
def home_away_advantage(home, away, indexed):
    home_home_form, away_away_form = feat.home_away_run(home, away, indexed)


    