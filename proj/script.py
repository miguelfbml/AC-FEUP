import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = 'winners/playoffs_10.csv'

csv11 = 'year11/teams.csv'

# Read the CSV file
playoffs10 = pd.read_csv(csv_file_path)

playoffs11 = pd.read_csv(csv11)


# Get the unique tmID values from both DataFrames
teams10 = set(playoffs10['tmID'].unique())
teams11 = set(playoffs11['tmID'].unique())


listaDeles = ["IND","NYL","ATL","WAS","PHO","LAS","SEA","SAS"]

bestP = ["ATL","CON","IND","LAS","PHO","SAS","SEA","WAS"]

listaDeles = set(listaDeles)

# Find the intersection of tmID values in both sets
common_teams = teams10.intersection(bestP)



# Print the common teams
print("Teams that appear in both playoffs10 and playoffs11:")
print(list(common_teams))







