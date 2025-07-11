import json 
with open ("weather.json", "r") as f : 
    data = json.load(f)
h = 11
print(data['days'][0]['hours'][h]['windspeed'])