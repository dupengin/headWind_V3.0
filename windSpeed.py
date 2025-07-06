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
    wind_speed = []
    wind_bearing =[]


    if test_mode : #use test data and don't make api call
        wind_data = open(test_file, 'r')
 
        #wind dir in column 0 and wind speed in column 1
        with open('your_file.csv', newline='') as csvfile:         
            reader = csv.reader(csvfile)    
            
            for row in reader:
                wind_speed.append(row['wind_speed'])
                wind_bearing.append(row['wind_dir'])

        

   else:
    
