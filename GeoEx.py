#test

from fnmatch import translate
import math
from re import X


def convert_dms_to_dd(dms): 
    degree , minute , second = dms
    return (minute/60) + (second/(60*60)) + degree
     
#Latitude being one & longitude being two 

paris_one = 48, 51, 23.81
paris_two = 2, 21, 7.999

latitude_paris = convert_dms_to_dd(paris_one)
longitude_paris = convert_dms_to_dd(paris_two)

#PoleNorth 86, 172 Degree 
PoleNorth_longitude = 172
PoleNorth_latitude = 86

#function for distance 
def distance(dd1, dd2, dd3, dd4): 
    
    num = math.sqrt((dd1 - dd2)**2 + (dd3 - dd4)**2)
    return num 

#callback function 
print((distance(PoleNorth_longitude, longitude_paris, PoleNorth_latitude, latitude_paris)))