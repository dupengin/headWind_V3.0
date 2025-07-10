"""
This code is to request weather data for the time noted in the GPX file 
It also includes a test mode for using test data to reduce the number of API calls 

OpenWeatherMap is the API used 

"""

def windSpeed(gpx_data, test_mode, test_file):
    from dotenv import load_dotenv
    import os
    import csv
    import datetime
    import requests

    api_key = os.getenv("API_KEY")
    wind_csv = []
    


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
        
        all_data = gpx_data
            
        

    else: #make api call to get weather data
        
        for i in range (len(gpx_data)):
            lat = gpx_data[i]['lat'] 
            lon = gpx_data[i]['longit'] 
            time = gpx_data[i]['time'] #convert to UNIX time
            date = gpx_data[i]['date']
            dt = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")
            unix_t = int(dt.replace(tzinfo=datetime.timezone.utc).timestamp())

            try:
                response = requests.get((f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK/2024-12-15T13:00:00?key=KWRSQR9EWW93RWEUXGXED6WSL"),
                timeout=10)
                
                response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)

                
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err} - Status code: {response.status_code}")
            except requests.exceptions.ConnectionError:
                print("Error connecting to the API.")
            except requests.exceptions.Timeout:
                print("The request timed out.")
            except requests.exceptions.RequestException as err:
                print(f"An error occurred: {err}")


    return all_data
