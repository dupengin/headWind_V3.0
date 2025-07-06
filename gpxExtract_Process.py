""" 
This code is to extract data from a GPX file, parse to a dictionary
Parsing to be done using the https://pypi.org/project/gpxpy/ library - pre req is to install the gpxpy library

Methodology
- Parse data to an array 
- Use the difference between i and i + 1 to calculate bearing and speed
- Save bearing and speed in a dictionary 
- the time and date of the gpx points needs to be retained to allign with the wind speed data
- it is assumed that rate of change in altitude is so small between points that it does not effect distance
Units 
- Speed kmh
- distance km

The ArcGIS Python library will be used
GeoPy to be used instead of ArcPy

Unit testing 
- Sample gpx files will be generated to test the data
- GPX inputs are known, these can be compared to the outputed speed and bearing data

Inputs
gpx file

Outputs
Dictionary containing speed, bearing, time and date of the gpx points



"""

import geopy.distance


def speedCalc(gpxFile):
    import gpxpy # for gpx parse
    import geopy # for distance calcs
    from datetime import datetime

    gpx_file = open(gpxFile, 'r') # open the gpx file in  read mode
    gpx_file_parse = gpxpy.parse(gpx_file)
    
    gpx_data = [] # array to store extracted data

    #loop tp extract data and write to arry
    for tracks in gpx_file_parse.tracks:
        for seg in tracks.segments:
            for point in seg.points:
                time = point.time.strftime("%H:%M:%S")
                date = point.time.strftime("%Y-%m-%d")
                longit = point.longitude
                lat = point.latitude

                gpx_data.append({'time':time, 'date':date, 'longit':longit, 'lat':lat})
    
    #distance calcs
    speed = []
    for i in range(len(gpx_data) - 1):
        point1 = (gpx_data[i]['lat'], gpx_data[i]['longit'])
        point2 = (gpx_data[i+1]['lat'], gpx_data[i+1]['longit'])
        
        dist = ( geopy.distance.distance(point1,point2).km) 

        
        fmt = "%H:%M:%S"
        t1 = datetime.strptime(gpx_data[i]['time'], fmt)
        t2 = datetime.strptime(gpx_data[i+1]['time'], fmt)

        # Calculate the time difference
        time_diff = t2 - t1
        time_diff_hrs = time_diff.total_seconds()/3600 

        speed.append(dist/time_diff_hrs) 

gpxFile = ('testData/Cycling.gpx')


speedCalc(gpxFile)
