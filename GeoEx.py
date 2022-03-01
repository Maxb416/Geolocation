#test 



from fnmatch import translate
import math
from re import X


def convert_dms_to_dd(dms): 
    degree , minute , second = dms
    return (minute/60) + (second/(60*60)) + degree
     

#Longitude being one & Latitude being two 

paris_one = 48, 51, 23.81
paris_two = 2, 21, 7.999

latitude_paris = convert_dms_to_dd(paris_one)
longitude_paris = convert_dms_to_dd(paris_two)


#PoleNorth 86, 172 Degree 
PoleNort_lon = 172
PoleNort_lat = 86


#function for distance 
def distance(x, a, y, b): 
    
    num = math.sqrt((x - a)**2 + (y - b)**2)
    return num 

#callback function 
print((distance(PoleNort_lon, longitude_paris, PoleNort_lat, latitude_paris)))
