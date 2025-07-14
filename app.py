""""



all_data = [{'time' : ..., 'date' : ... , 'longit': ... , 'lat' : ..., 'speed' : ..., 'bearing' : ..., 'wind_speed' : ..., 'wind_bearing' : ... }]

"""



from gpxExtract_Process import speedCalc
from windSpeed import windSpeed
from relativeWindSpeed import relativeWindSpeed
import csv


gpxFile = ('testData/GPX_2.gpx')
all_data = speedCalc(gpxFile)

test_mode = False
test_wind_file = ('testData/wind_0deg_0ms.csv')
all_data = windSpeed(all_data,test_mode, test_wind_file)


all_data = relativeWindSpeed(all_data)



with open("data_out", mode='w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=all_data[0].keys())
    writer.writeheader()
    writer.writerows(all_data)


