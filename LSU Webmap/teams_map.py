import folium
import pandas as pd
import os


def createFilesList():
    dir = os.getcwd() + '/Data Sets/'
    return os.listdir(dir)

def createFeatureGroup(team, file, color):
    data = pd.read_csv(file)
    lat = list(data["lat"])
    lon = list(data["lng"])
    names = list(data["name"])

    fg = folium.FeatureGroup(name = f"{team}")

    for lt, ln, name in zip(lat, lon, names):
        fg.add_child(folium.Marker(location = [lt, ln], popup = str(name), icon = folium.Icon(color = f"{color}")))
    map.add_child(fg)


files = createFilesList()
map = folium.Map(location = [38.58, -99.89], zoom_start = 6, tiles = "Stamen Terrain")

createFeatureGroup("LSU", "lsu_merged.csv", "purple")
createFeatureGroup("OSU", "ohio-state_merged.csv", "red")

map.add_child(folium.LayerControl())
map.save("lsu_osu.html")