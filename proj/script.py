import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = 'basketballPlayoffs/teams.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Describe the DataFrame
description = df.describe()

# Print the description
print(description)

# Get the number of unique teams
unique_teams = df['tmID'].nunique()

print(unique_teams)
