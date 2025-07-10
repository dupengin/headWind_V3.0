"""
This code is to request weather data for the time noted in the GPX file 
It also includes a test mode for using test data to reduce the number of API calls 

OpenWeatherMap is the API used 

"""

def windSpeed(gpx_data, test_mode, test_file):
    from dotenv import load_dotenv
    import os
    import csv
    from datetime import datetime
    import requests
    import json 
    import time as time_mod
    load_dotenv()
    api_key = os.getenv("API_KEY")
    json_file = False
    json_path =  "weather.json"
    write_to_json = True
    
    


    if test_mode : #use test data and don't make api call
        #wind_data = open(test_file, 'r')
        print ("in test mode")
 
        #wind dir in column 0 and wind speed in column 1
        with open(test_file) as f:         
            reader = csv.reader(f)    
            next(reader)
            for row in reader:
               wind_bearing = row[0]
               wind_speed = row[1]
               

        for i in range(len(gpx_data)):
            gpx_data[i]["wind_speed"] = int(wind_speed)
            gpx_data[i]["wind_bearing"] = int(wind_bearing)
        
        
            
        
    elif json_file :
        
        with open (json_path, "r") as f : 
            weather_data = json.load(f)
            for i in range (len(gpx_data)):
                time = gpx_data[i]['time'] 
                h = (datetime.strptime(time, "%H:%M:%S")).hour
                gpx_data[i]['wind_speed'] = weather_data['days'][0]['hours'][h]['windspeed']
                gpx_data[i]['wind_bearing'] = weather_data['days'][0]['hours'][h]['winddir']

    else: #make api call to get weather data
             
        #limit the number of API calls to 10 max
        if len(gpx_data) > 10:
            i_increment = len(gpx_data) // 10
            
        else : 
            i_increment = 1
        
        for i in range (0, len(gpx_data), i_increment):
            
            lat = gpx_data[i]['lat'] 
            lon = gpx_data[i]['longit'] 
            time = gpx_data[i]['time'] 
            date = gpx_data[i]['date']
            h = (datetime.strptime(time, "%H:%M:%S")).hour

            #time_mod.sleep(1)

            try:
                
                response = requests.get((f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}/{date}T{time}?key={api_key}"),
                timeout=10)
                
                weather_data = response.json()
                response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)
                

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err} - Status code: {response.status_code}")
            except requests.exceptions.ConnectionError:
                print("Error connecting to the API.")
            except requests.exceptions.Timeout:
                print("The request timed out.")
            except requests.exceptions.RequestException as err:
                print(f"An error occurred: {err}")
            

            #as the api requests are limited we need to populate the gps data with the appropiate wind speeds 
            for i in range (i, i + i_increment):
                gpx_data[i]['wind_speed'] = weather_data['days'][0]['hours'][h]['windspeed']
                gpx_data[i]['wind_bearing'] = weather_data['days'][0]['hours'][h]['winddir']

            
            def is_json_serializable(json_file):
                try:
                    json.dumps(json_file)
                    return True
                except (TypeError, OverflowError):
                    return False

            
            if write_to_json and is_json_serializable(weather_data):
                with open ("weather.json", "w") as f:
                    json.dump(weather_data, f )
            
                





    return gpx_data
