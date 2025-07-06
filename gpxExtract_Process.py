""" 
This code is to extract data from a GPX file, parse to a dictionary
Parsing to be done using the https://pypi.org/project/gpxpy/ library - pre req is to install the gpxpy library

Methodology
- Parse data to an array 
- Use the difference between i and i + 1 to calculate bearing and speed
- Save bearing and speed in a dictionary 
- the time and date of the gpx points needs to be retained to allign with the wind speed data
Units 
- Speed kmh
- distance km

The ArcGIS Python library will be used
As coords are in deg, this will need to be converted to KM to give the correct speed

Unit testing 
- Sample gpx files will be generated to test the data
- GPX inputs are known, these can be compared to the outputed speed and bearing data

Inputs
gpx file

Outputs
Dictionary containing speed, bearing, time and date of the gpx points



"""

def speedCalc(gpxFile):
    import gpxpy # for gpx parse
    import arcpy # for distance calcs

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
    
# Define spatial reference
    sr_wgs84 = arcpy.SpatialReference(4326)  #WGS84 Degrees
    sr_web_merc = arcpy.SpatialReference(3857)   #Web Mercator to convert to meters

    for i in range(len(gpx_data) - 1):
        point1 = arcpy.PointGeometry(arcpy.Point(gpx_data[i+1]['longit'], gpx_data[i+1]['lat']), sr_wgs84)
        point2 = arcpy.PointGeometry(arcpy.Point(gpx_data[i+1]['longit'], gpx_data[i+1]['lat']), sr_wgs84)
        
        point1_km = (point1.projectAs(sr_web_merc))/1000 #convert deg to km
        point2_km = (point2.projectAs(sr_web_merc))/1000 #convert deg to km


gpxFile = ('testData/north_1kmh.gpx')


speedCalc(gpxFile)
