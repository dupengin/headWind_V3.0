"""This module calculates the relative wind speed to the gpx file data

Relative wind speed 

Methodogy 
- Calculate the North South component and East West components for wind and gpx data
- Find resultant in N/S and E/W by summing 
- Use trig to find resultant wind speed 

"""

def relativeWindSpeed(data_in):
    import math


    for i in range(len(data_in)):
        #calculate the eastern and northern component to the wind and gpx speed
        #wind speed is mulitplied by -1 as the bearing is the direction the wind is coming from where as the gpx bearing is moving in that direction 
        
        #calculate the angle of the wind relative to the gpx bearing

        rel_bearing_rad = math.radians(data_in[i]['wind_bearing'] - data_in[i]['bearing'])
        
        head_wind = data_in[i]['wind_speed'] * math.cos(rel_bearing_rad)
        rel_head_wind = data_in[i]['speed'] + head_wind
        #wind_bearing_deg =math.radians(data_in[i]['wind_bearing'])
        #gpx_bearing_deg = math.radians(data_in[i]['bearing'] )
        #wind_east = data_in[i]['wind_speed'] * math.cos(wind_bearing_deg ) * (-1)
        #wind_north = data_in[i]['wind_speed'] * math.sin(wind_bearing_deg ) * (-1) 
        #gpx_east = data_in[i]['speed'] * math.cos(gpx_bearing_deg )
        #gpx_north = data_in[i]['speed'] * math.sin(gpx_bearing_deg )

       # res_east = wind_east - gpx_east
       # res_north = wind_north - gpx_north

        #res_speed = math.sqrt((res_east**2) + (res_north**2))

        data_in[i]['res'] = rel_head_wind
    
    
    return data_in

test_data = [{'time' : 0, 'date' : 0 , 'longit': 0, 'lat' : 0, 'speed' : 25, 'bearing' : 0, 'wind_speed' : 1, 'wind_bearing' : 90 }]
        
relativeWindSpeed(test_data)