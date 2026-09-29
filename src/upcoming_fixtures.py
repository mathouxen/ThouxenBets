import json
import urllib.request

API_KEY = "YOUR_FOOTBALL_DATA_KEY"
ENDPOINT = "https://api.football-data.org/v4/competitions/PL/matches"

# Team map to ensure team names match your CSV dataset exactly
TEAM_NAME_MAP = {
    "Manchester United FC": "Man United",
    "Tottenham Hotspur FC": "Tottenham",
    "Nottingham Forest FC": "Nott'm Forest",
    "West Ham United FC": "West Ham",
    "Leeds United FC": "Leeds United",
    "Newcastle United FC": "Newcastle",
    "Wolverhampton Wanderers FC": "Wolves",
    "Arsenal FC": "Arsenal",
    "Chelsea FC": "Chelsea",
    "Everton FC": "Everton",
    "Liverpool FC": "Liverpool",
    "Manchester City FC": "Man City",
    "Aston Villa FC": "Aston Villa",
    "AFC Bournemouth": "Bournemouth",
    "Brentford FC": "Brentford",
    "Brighton & Hove Albion FC": "Brighton",
    "Crystal Palace FC": "Crystal Palace",
    "Fulham FC": "Fulham",
    "Leicester City FC": "Leicester",
    "Southampton FC": "Southampton",
    "Ipswich Town FC": "Ipswich",
    "Burnley FC": "Burnley",
    "Sunderland AFC": "Sunderland"
}


# Checks to see if the name of the pulled teams is present in the name map, 
# changes it should it have a shortened version and returns that or returns
# the one from the api should it not exist
def normalize_team(name):
    return TEAM_NAME_MAP.get(name, name)

def get_upcoming_fixtures():
    req = urllib.request.Request(ENDPOINT)
    req.add_header("X-Auth-Token", API_KEY)
    
    try:
        with urllib.request.urlopen(req) as response:
            payload = json.loads(response.read().decode("utf-8"))
            matches = payload.get("matches", [])
            
            upcoming_rows = []
            
            for match in matches:
                # API gives UTC ISO string: "2026-10-02T19:00:00Z"
                raw_utc = match["utcDate"]
                
                # Convert YYYY-MM-DD to DD/MM/YYYY to match your CSV
                date_parts = raw_utc[:10].split("-")
                formatted_date = f"{date_parts[2]}/{date_parts[1]}/{date_parts[0]}"
                
                formatted_time = raw_utc[11:16]
                
                home_team = normalize_team(match["homeTeam"]["name"])
                away_team = normalize_team(match["awayTeam"]["name"])
                
                # Aligning with CSV schema:
                # [Date, Time, HomeTeam, AwayTeam, FTHG, FTAG, FTR, HTHG, HTAG, HTR]
                row = [
                    formatted_date,
                    formatted_time,
                    home_team,
                    away_team,
                    None, None, None, None, None, None
                ]
                upcoming_rows.append(row)
                
            return upcoming_rows

    except Exception as e:
        print(f"Error fetching fixtures from football-data.org: {e}")
        return []

if __name__ == "__main__":
    fixtures = get_upcoming_fixtures()
    print(f"Retrieved {len(fixtures)} upcoming scheduled fixtures:\n")
    
    for row in fixtures[:5]:  # Display top 5 matches
        print(f"{row[0]} {row[1]} | {row[2]} vs {row[3]}")