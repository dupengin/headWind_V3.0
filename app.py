""""
Inputs 
-GPX file
-File paths for GPX data, test wind data and saving output data

Outputs 
- CSV, data written to CSV. Keys used as headers
all_data = [{'time' : ..., 'date' : ... , 'longit': ... , 'lat' : ..., 'speed' : ..., 'bearing' : ..., 'wind_speed' : ..., 'wind_bearing' : ..., 'res : ... }]

"""



from gpxExtract_Process import speedCalc
from windSpeed import windSpeed
from relativeWindSpeed import relativeWindSpeed
import csv


gpxFile = ('testData/GPX.gpx') 
all_data = speedCalc(gpxFile)
#all_data = [{'time' : ..., 'date' : ... , 'longit': ... , 'lat' : ..., 'speed' : ..., 'bearing' : ...}]

test_mode = False #True for test mode
test_wind_file = ('testData/wind_0deg_0ms.csv') #if test_mode true which test data to be used
all_data = windSpeed(all_data,test_mode, test_wind_file) # call wind speed module
#all_data = [{'time' : ..., 'date' : ... , 'longit': ... , 'lat' : ..., 'speed' : ..., 'bearing' : ..., 'wind_speed' : ..., 'wind_bearing' : ...}]


all_data = relativeWindSpeed(all_data)
#all_data = [{'time' : ..., 'date' : ... , 'longit': ... , 'lat' : ..., 'speed' : ..., 'bearing' : ..., 'wind_speed' : ..., 'wind_bearing' : ..., 'res : ... }]

out_file_name = "data_out" #Data Out - CSV 

with open(out_file_name, mode='w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=all_data[0].keys())
    writer.writeheader()
    writer.writerows(all_data)


