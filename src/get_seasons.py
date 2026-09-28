import urllib.request
import json
import csv

api_token = "51f818a6bcd74bce82059c102d117474"
url= "http://api.football-data.org/v4/competitions/PL/matches?season=2025"

# Construct request
request = urllib.request.Request(url)
request.add_header("X-Auth-Token", api_token)

# Send request and recieve response
response = urllib.request.urlopen(request)
data = json.loads(response.read().decode("utf-8"))

raw_api_file_path = "raw_api_data.json"

with open(raw_api_file_path, "w", encoding="utf-8") as raw_json_file:
    json.dump(data, raw_json_file, indent=4)


team_mapping = {
    "Wolverhampton": "Wolves",
    "Wolverhampton Wanderers FC": "Wolves",
    "Newcastle": "Newcastle",
    "Newcastle United FC": "Newcastle",
    "West Ham": "West Ham",
    "West Ham United FC": "West Ham",
    "Fulham": "Fulham",
    "Fulham FC": "Fulham",
    "Man United": "Man United",
    "Manchester United FC": "Man United",
    "Man City": "Man City",
    "Manchester City FC": "Man City",
    "Tottenham": "Tottenham",
    "Tottenham Hotspur FC": "Tottenham",
    "Nottingham": "Nott'm Forest",
    "Nottingham Forest FC": "Nott'm Forest",
    "Brighton Hove": "Brighton",
    "Brighton & Hove Albion FC": "Brighton",
    "Arsenal": "Arsenal",
    "Aston Villa": "Aston Villa",
    "Bournemouth": "Bournemouth",
    "Brentford": "Brentford",
    "Chelsea": "Chelsea",
    "Crystal Palace": "Crystal Palace",
    "Everton": "Everton",
    "Ipswich": "Ipswich",
    "Leicester": "Leicester",
    "Liverpool": "Liverpool",
    "Southampton": "Southampton"
}

with open(raw_api_file_path, "r", encoding="utf-8") as json_input:
    raw_data = json.load(json_input)

matches = raw_data.get("matches", [])

matches_added = 0

csv_file_path = "data/premier_league_clean.csv"

with open(csv_file_path, "a", newline="", encoding="utf-8") as csv_output:
    writer = csv.writer(csv_output)

    for match in matches:   
        utc_date = match.get("utcDate", "")
        date_str = ""
        time_str = ""
        if "T" in utc_date:
            parts = utc_date.split("T")
            ymd = parts[0].split("-")
            if len(ymd) == 3:
                date_str = ymd[2] + "/" + ymd[1] + "/" + ymd[0]
            time_str = parts[1][:5] 

        home_obj = match.get("homeTeam", {})
        raw_home = home_obj.get("shortName") or home_obj.get("name", "")
        home_team = team_mapping.get(raw_home, raw_home)

        away_obj = match.get("awayTeam", {})
        raw_away = away_obj.get("shortName") or away_obj.get("name", "")
        away_team = team_mapping.get(raw_away, raw_away)

        # Extract goals
        score = match.get("score", {})
        
        full_time = score.get("fullTime", {})
        fthg = full_time.get("home")
        ftag = full_time.get("away")

        half_time = score.get("halfTime", {})
        hthg = half_time.get("home")
        htag = half_time.get("away")

        # Skip fixtures that haven't been played yet
        if fthg is None or ftag is None:
            continue

        # Calculate Full-Time Result (FTR)
        ftr = ""
        if fthg > ftag:
            ftr = "H"
        elif ftag > fthg:
            ftr = "A"
        else:
            ftr = "D"

        # Calculate Half-Time Result (HTR)
        htr = ""
        if hthg is not None and htag is not None:
            if hthg > htag:
                htr = "H"
            elif htag > hthg:
                htr = "A"
            else:
                htr = "D"

        # Append row to CSV: Date,Time,HomeTeam,AwayTeam,FTHG,FTAG,FTR,HTHG,HTAG,HTR
        row = [date_str, time_str, home_team, away_team, fthg, ftag, ftr, hthg, htag, htr]
        writer.writerow(row)
        matches_added += 1



# import csv
# import json
# import urllib.request

# API_KEY = "8c5caa0c4b62bbcf9b7298292ba7e41e"
# LEAGUE_ID = "39"
# SEASONS_TO_FETCH = ["2024", "2025", "2026"]
# CSV_FILENAME = "data/premier_league_matches.csv"

# # Open file in append mode
# csv_file = open(CSV_FILENAME, mode="a", newline="", encoding="utf-8")
# writer = csv.writer(csv_file)

# for season in SEASONS_TO_FETCH:
#     url = (
#         "https://v3.football.api-sports.io/fixtures?league="
#         + LEAGUE_ID
#         + "&season="
#         + season
#     )

#     request = urllib.request.Request(url)
#     request.add_header("x-apisports-key", API_KEY)

#     try:
#         response = urllib.request.urlopen(request)
#         data = json.loads(response.read().decode("utf-8"))

#         # Check for API error messages
#         errors = data.get("errors", [])
#         if errors:
#             print("API Error for season " + season + ": " + str(errors))
#             continue

#         fixtures = data.get("response", [])
#         print("Fetched " + str(len(fixtures)) + " fixtures for season " + season)

#         for item in fixtures:
#             fixture_info = item.get("fixture", {})
#             teams_info = item.get("teams", {})
#             goals_info = item.get("goals", {})

#             date = fixture_info.get("date")
#             home_team = teams_info.get("home", {}).get("name")
#             away_team = teams_info.get("away", {}).get("name")
#             home_goals = goals_info.get("home")
#             away_goals = goals_info.get("away")
#             status = fixture_info.get("status", {}).get("short")

#             row = [season, date, home_team, away_team, home_goals, away_goals, status]
#             writer.writerow(row)

#     except Exception as e:
#         print("Failed to fetch season " + season + ": " + str(e))

# csv_file.close()
# print("CSV successfully updated!")



# import csv
# import json
# import urllib.request

# # Configuration
# API_KEY = "8c5caa0c4b62bbcf9b7298292ba7e41e"
# LEAGUE_ID = "39"  # Premier League in API-Football
# SEASONS_TO_FETCH = ["2024", "2025", "2026"]  # seasons needed
# CSV_FILENAME = "data/premier_league_matches.csv"


# csv_file = open(CSV_FILENAME, mode="a", newline="", encoding="utf-8")
# writer = csv.writer(csv_file)


# for season in SEASONS_TO_FETCH:
#     url = (
#         "https://v3.football.api-sports.io/fixtures?league="
#         + LEAGUE_ID
#         + "&season="
#         + season
#     )

#     request = urllib.request.Request(url)
#     request.add_header("x-apisports-key", API_KEY)

#     response = urllib.request.urlopen(request)
#     data = json.loads(response.read().decode("utf-8"))

#     fixtures = data.get("response", [])

#     for item in fixtures:
#         fixture_info = item.get("fixture", {})
#         league_info = item.get("league", {})
#         teams_info = item.get("teams", {})
#         goals_info = item.get("goals", {})

#         date = fixture_info.get("date")
#         home_team = teams_info.get("home", {}).get("name")
#         away_team = teams_info.get("away", {}).get("name")
#         home_goals = goals_info.get("home")
#         away_goals = goals_info.get("away")
#         status = fixture_info.get("status", {}).get("short")

#         # Order row to match the format of the csv file
#         row = [season, date, home_team, away_team, home_goals, away_goals, status]
#         writer.writerow(row)

# csv_file.close()
# print("CSV successfully updated!")


