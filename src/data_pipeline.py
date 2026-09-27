url = "https://v3.football.api-sports.io/fixtures"

payload={}
headers = {
  'x-apisports-key': '8c5caa0c4b62bbcf9b7298292ba7e41e',
}

params = {
    'league': '39',
    'season': '2023'
}

response = requests.request("GET", url, headers=headers, params=params, data=payload)

print(response.text)