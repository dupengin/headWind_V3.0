"""This module calculates the relative wind speed to the gpx file data

Relative wind speed 

Methodogy 
- Find the relative angle between bearing of the gpx coordinates and the wind
- Calculate the tangential component of the wind - this plus speed is realtive wind speed

"""

def relativeWindSpeed(data_in):
    import math


    for i in range(len(data_in)): #loop through all the gpx bearings and associated wind speeds
               
        #calculate the angle of the wind relative to the gpx bearing
        rel_bearing_rad = math.radians(data_in[i]['wind_bearing'] - data_in[i]['bearing'])
        head_wind = data_in[i]['wind_speed'] * math.cos(rel_bearing_rad)
        rel_head_wind = data_in[i]['speed'] + head_wind
             

        data_in[i]['res'] = rel_head_wind # store data
    
    
    return data_in

#Unit testing the file
#test_data = [{'time' : 0, 'date' : 0 , 'longit': 0, 'lat' : 0, 'speed' : 25, 'bearing' : 0, 'wind_speed' : 1, 'wind_bearing' : 90 }]
       
#relativeWindSpeed(test_data)