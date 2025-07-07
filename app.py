
from gpxExtract_Process import speedCalc
from windSpeed import windSpeed

gpxFile = ('testData/east_25kmh.gpx')
all_data = speedCalc(gpxFile)

test_mode = True
test_wind_file = ('testData/wind_0deg_0ms.csv')
windSpeed(all_data,test_mode, test_wind_file)
