#test 

from turtle import tracer


def convert_dms_to_dd(dms): 
    degree , minute , second = dms
    return (minute/60) + (second /60*60) + degree
     


#Longitude being one & Latitude being two 

paris_one = 48, 51, 23.81

paris_two = 2, 21, 7.999


print(convert_dms_to_dd(paris_one))

tracer
