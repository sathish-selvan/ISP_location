import folium
import requests
import json
import webbrowser

# {'ip': '255.0.0.10',
#  'city': 'your city',
#  'region': 'State',
#  'country': 'IN', 
#  'loc': '13.0878,80.2785', 
#  'org': 'AS55836 Reliance Jio Infocomm Limited',  (ISP provider)
#  'postal': '600001',
#  'timezone': 'Asia/Kolkata',
#  'readme': 'https://ipinfo.io/missingauth'}

res = requests.get("https://ipinfo.io/")
data = res.json()

location=data['loc'].split(",")
lat = float(location[0])
log = float(location[1])
fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open("india_states.json",'r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[lat,log],popup="this is ur nearby location"))

map=folium.Map(location=[lat,log],zoom_start=7)
map.add_child(fg)
map.save("1.html")
url = "1.html"
webbrowser.open(url,new=2)