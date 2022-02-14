#to create  the map you need this library, pandas was used to visualize the data
import folium
import pandas 

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#creating your function
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
#creating the map object
map = folium.Map(location=[38.58,-99.05], zoom_start= 6, tiles= "Stamen Terrain")

#creaing a feature group
fgv = folium.FeatureGroup(name="volcanoes")

fgp = folium.FeatureGroup(name="Population")
#Adding more points to the map
for lt, ln, el in zip(lat, lon,elev):
    #Adding points to the map
    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el) + " m", parse_html=True), icon=folium.Icon(color=color_producer(el))))
    #fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(str(el) + " m", fill_collor= color_producer(el), color= 'grey', fill_opacity=0.7)) 

#adding a GEOJson polygon Layer 

fgp.add_child(folium.GeoJson(data=open('world.json', 'r',  encoding='utf-8-sig').read()))

#adding layer control panel

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl)
map.save("Map1.html")