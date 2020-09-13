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
            teams.append(team['school'])
    index = teams.index('Texas A&M')
    teams[index] = "Texas%20A%26M"

def getRosterFromAPI(url):
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
        url = f"https://api.collegefootballdata.com/roster?team={team}&year={year}"
        df = getRosterFromAPI(url)
        merge_data.mergeRosterWithGeoCoords(df, team)
        



