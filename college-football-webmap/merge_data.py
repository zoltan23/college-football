import pandas as pd
import state_abbreviations
import re
import os
import requests
import json
from pandas.io.json import json_normalize

def mergeRosterWithGeoCoords(df, team):
    
    team_name = team

    # Import the datasets to be merged
    roster_df = df
    cities_df = pd.read_csv(os.getcwd() + '/datasets/' + "worldcities.csv")

    # Subset the data to only include the USA as retain only the necessary variables for WebMap
    cities_df = cities_df[cities_df['iso3'] == 'USA']
    cities_df = cities_df[['city', 'admin_name', 'lat', 'lng']]

    # In order to merge the two data sets, the states must both be abbrevatiated.  A custom function 
    # was created to abbreviate the states.  
    cities_df['admin_name'] = cities_df['admin_name'].apply(lambda x: state_abbreviations.abbreviateState(x))   

    # Merge the datasets by city
    new_df = pd.merge(cities_df, roster_df, left_on=  ['city', 'admin_name'],
                   right_on= ['home_city', 'home_state'], 
                   how = 'inner')

    # Drop the redudant variables home_city and home_state
    new_df.drop(['home_city', 'home_state'], axis = 1, inplace = True)
    
    # Export to csv
    new_df.to_csv(os.getcwd() + '/datasets/' + team_name + '_merged.csv')

# The following function concatenates all of the college football teams into one
# main dataset.
def createMasterDataset():
    frames = []
    for file in os.listdir(dir):
        df = pd.read_csv(dir + file, "*", header=0)
        frames.append(df)
    master_df = pd.concat(frames)    
    print(master_df)




