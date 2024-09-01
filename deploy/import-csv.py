import csv
import json

# get the csv data from the path
with open('static/data/data.csv', 'r') as file:
    csv_data = file.read()

# Parse CSV data
csv_reader = csv.DictReader(csv_data.splitlines())

# Convert to list of dictionaries
data = [row for row in csv_reader]

# Write to JSON file
with open('static/data/data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
