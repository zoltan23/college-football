import pandas as pd
import re
import os
import requests
import json
from pandas.io.json import json_normalize

# This script fetches all of the rosters for all of the teams and years specified in the lists
# teams and years.

teams = ["Alabama", "Arkansas", "Auburn", "Florida", "Georgia", "Kentucky", "LSU", "Miss. State", "Missouri", "Ole Miss", "South Carolina", "Tennessee", "Texas A&M", "Vanderbilt"]
years = ["2019"]

def queryAPI(url):
    response = requests.get(url)
    data = response.json()
    print(data)

    df = pd.DataFrame.from_dict(data)
    #df.to_csv('college.csv')
    print(df)

for team in teams:
    for year in years:
        url = f"https://api.collegefootballdata.com/roster?team={team}&year={year}"
        queryAPI(url)
        print(url)

#queryAPI('https://api.collegefootballdata.com/roster?team=LSUAA&year=2019')

