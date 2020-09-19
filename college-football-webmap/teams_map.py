import folium
import pandas as pd
import os
import colors_dict

def createFilesList():
    dir = os.getcwd() + '/datasets/merged/'
    return os.listdir(dir)

def createFeatureGroup(file):
    data = pd.read_csv(file)
    lat = list(data["lat"])
    lon = list(data["lng"])
    names = list(data["last_name"])
    team = data['team'][0]
    color = colors_dict.colors.get(team)
    fg = folium.FeatureGroup(name = f"{team}")

    for lt, ln, name in zip(lat, lon, names):
        fg.add_child(folium.Marker(location = [lt, ln], popup = str(name), icon = folium.Icon(color = f"{color}")))
    map.add_child(fg)

map = folium.Map(location = [38.58, -99.89], zoom_start = 6, tiles = "Stamen Terrain")

files = createFilesList()
for file in files:
    print(file)
    createFeatureGroup(os.getcwd() + '/datasets/merged/' + file)

map.add_child(folium.LayerControl())
map.save("college_map.html")