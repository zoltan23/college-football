import folium
import pandas as pd

data = pd.read_csv("lsu_merged.csv")
lat = list(data["lat"])
lon = list(data["lng"])
names = list(data["name"])

map = folium.Map(location = [38.58, -99.89], zoom_start = 6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")

for lt, ln, name in zip(lat, lon, names):
    fg.add_child(folium.Marker(location = [lt, ln], popup = str(name), icon=folium.Icon(color="purple")))
map.add_child(fg)

map.save("lsu_map.html")