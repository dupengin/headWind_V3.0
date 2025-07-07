"""
This code is to request weather data for the time noted in the GPX file 
It also includes a test mode for using test data to reduce the number of API calls 

OpenWeatherMap is the API used 

"""

def windSpeed(gpx_data, test_mode, test_file):
    from dotenv import load_dotenv
    import os
    import csv

    api_key = os.getenv("API_KEY")
    wind_csv = []
    


    if test_mode : #use test data and don't make api call
        #wind_data = open(test_file, 'r')
 
        #wind dir in column 0 and wind speed in column 1
        with open(test_file) as f:         
            reader = csv.reader(f)    
            next(reader)
            for row in reader:
               wind_bearing = row[0]
               wind_speed = row[1]
               

        for i in range(len(gpx_data)):
            gpx_data[i]["wind_speed"] = wind_speed
            gpx_data[i]["wind_bearing"] = wind_bearing
        
        all_data = gpx_data
            
        

    else: #make api call to get weather data
        print('api call')

    return all_data
