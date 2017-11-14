import googlemaps
import math
from math import radians, cos, sin, asin, sqrt, atan2

#----------globals------------------------------
n = 10;  # size of the matrix (how many points pulled from Chris)
map = [[0 for i in range(n)] for j in range(n)]
data = [0.0 for i in range(3 * n)]
#-------------------------------------------------


class Node(object):
    id = 0
    lat = 0
    lon = 0
    weight = "Full"
    
    def __init__(self, id, lat, lon, weight):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.weight = weight


 # when calling create node in main, data is pulled from Chris
def createNode(id, lat, lon, weight):
    node = Node(id, lat, lon, weight)
    return node
        
    
def createArray():
    print("Creating Array")
    for j in range(n):
        map[0][j] = nodes[j].id 
        map[j][0] = nodes[j].id
        t = t + 1
        for i in range(n):
            if(map[i][j] == 0):
                if(i == j):
                    map[i][j] = -1
                else:    
                    calculation = 3  # calcGoogleBike(transportation)
                    map[i][j] = calculation
                    map[j][i] = calculation

          
def calculate(orig_lng, orig_lat, dest_lng, dest_lat, threshold):
    if(threshold == "Full"):
        return 0
    
    if(threshold == "Empty"):
        R = 6373.0
        lat1 = radians(orig_lat)
        lon1 = radians(orig_lng)
        lat2 = radians(dest_lat)
        lon2 = radians(dest_lng)
        dlon = lon2 - lon1
        dlat = lat2 - lat1 
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        
        distance = R * c
        
        pointA = distance * 2
        
        print(distance)
        return distance
    
    if(threshold == "Medium"):
        R = 6373.0
        lat1 = radians(orig_lat)
        lon1 = radians(orig_lng)
        lat2 = radians(dest_lat)
        lon2 = radians(dest_lng)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        
        pointB = distance
        
        distance = R * c
        return distance
    
    else:
        return 0  
    
    
def getPoint(pointA):
    if (pointA > 25):
        return 9
    else:
        #TODO
        return 8
    
    
def calcGoogleBike(orig_lng, orig_lat, dest_lng, dest_lat, threshold):
    if(threshold == "Full"):
        return 0
    else:
        orig_coord = orig_lat, orig_lng
        dest_coord = dest_lat, dest_lng
        if(transportation == "Bicycle"):
            urlBike = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=bicycling&language=en-EN&sensor=false".format(str(orig_coord), str(dest_coord))
            resultBike = simplejson.load(urllib.urlopen(urlBike))
            biking_time = result['rows'][0]['elements'][0]['duration']['value']
        if(transportation == "Car"):
            urlDrive = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord), str(dest_coord))
            resultDrive = simplejson.load(urllib.urlopen(urlDrive))
            driving_time = result['rows'][0]['elements'][0]['duration']['value']

            
def main():
    createArray()
    
    print("hello")
    orig_lat = 37.0646
    orig_lng = 76.4944
    dest_lat = 36.8856
    dest_lng = 76.3068
    
    for i in range (100):
        calculate(orig_lng, orig_lat, dest_lng, dest_lat, "Empty")
        orig_lat = orig_lat + 0.0001
        orig_lng = orig_lng + 0.0001
        dest_lat = dest_lat + 0.0001
        dest_lng = dest_lng + 0.0001
    
#     i = 0
#     for j in range(n):
#         nodes[j] = createNode(i, data[j], data[j+1], data[j+2])
#         i = i + 1
#         j = j + 3
#     
#     createArray()
#     
#     for j in range(n):
#         for i in range(n):
#             print map[i][j],
#             print('\n')


main()
