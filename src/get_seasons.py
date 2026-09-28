import urllib.request
import json

api_token = "51f818a6bcd74bce82059c102d117474"
url= "http://api.football-data.org/v4/competitions/PL/matches?season=2025"

# Construct request
request = urllib.request.Request(url)
request.add_header("X-Auth-Token", api_token)

# Send request and recieve response
response = urllib.request.urlopen(request)
data = json.loads(response.read().decode("utf-8"))

print(json.dumps(data, indent=4))




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


