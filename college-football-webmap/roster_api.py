import pandas as pd
import re
import os
import requests
import json
from pandas.io.json import json_normalize
import merge_data

# This script fetches all of the rosters for all of the teams and years specified in the lists
# teams and years.

def getTeamsList():
    response = requests.get('https://api.collegefootballdata.com/teams/fbs')
    data = response.json()
    for team in data:
        if(team['conference'] == 'SEC'):
            teams.append([team['school'], team['color'], team['conference']])
    val = [index for index in teams if 'Texas A&M' in index] 
    val[0][0] = "Texas%20A%26M"
    return data

def queryAPI(url):
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame.from_dict(data)
    return df

teams = []
years = ["2019"]
getTeamsList()

# Get the rosters for all of the teams and given years and then merge them with worldcities csv to the 
# data sets contains the latitude and longitude for mapping.
for team in teams:
    for year in years:
        url = f"https://api.collegefootballdata.com/roster?team={team[0]}&year={year}"
        roster_df = queryAPI(url)
        roster_df['team'] = team[0]
        roster_df['color'] = team[1]
        roster_df['conference'] = team[2]
        merge_data.mergeRosterWithGeoCoords(roster_df, team[0])
        
#Get the recruiting data for all years
for year in years:
    url = f"https://api.collegefootballdata.com/recruiting/players?year={year}&classification=HighSchool"
    recruiting_df = queryAPI(url)
    recruiting_df.to_csv(os.getcwd() + '/datasets/recruiting/recruiting' + year + '.csv')

