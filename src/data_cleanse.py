import csv
import os

raw_file = "data/E0.csv"
cleaned_file = "data/premier_league_clean.csv"

columns = [
    "Date", "Time", "HomeTeam", "AwayTeam",
    "FTHG", "FTAG", "FTR", "HTHG", "HTAG", "HTR"
]

clean_rows = []

if os.path.exists(raw_file):
    with open(raw_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            clean_row = {}
            for col in columns:
                clean_row[col] = row.get(col, "")
            clean_rows.append(clean_row)

    with open(cleaned_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(clean_rows)

