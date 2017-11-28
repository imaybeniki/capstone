from math import radians, cos, sin, asin, sqrt, atan2
import psycopg2
from capstoneSite.settings import DATABASES

#----------globals--------------------------------------------
n = 0  # size of the matrix (how many points pulled from Chris)
nodes = []
scale = 0
#--------------------------------------------------------------


# This class defines a node and all its attributes
class Node(object):
    id = 0
    lat = 0.0
    lon = 0.0
    weight = 0.0
    
    # initializes the nodes attributes
    def __init__(self, id, lat, lon, weight):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.weight = weight


#Make fake data
def makeFakeData(n):
    rows = []
    long = 34.7
    lat = 34.7
    weight = 0.5
    add = 0.2
    
    for x in range(n):
        row = [n, long + n * 0.1, lat + n * 0.1, weight + add]
        add = add * -1
        rows.append(row)
    
    return rows

        
# This function pulls from the database and uses the DB values to intialize nodes
def pullFromDB():
    connectionString = "dbname='%(NAME)s' user='%(USER)s' host='%(HOST)s' password='%(PASSWORD)s'" % DATABASES['default']
    conn = psycopg2.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute("select LOCATION_NUMBER, LOCATION_LAT, LOCATION_LONG, WEIGHT from LOCATIONS")
    fetchedData = cursor.fetchall()
    #fetchedData = makeFakeData(2500)
    
    global n
    global nodes
    
    n = len(fetchedData)
    print("N is: ", n)
    
    #print(fetchedData)
    
#     print(fetchedData[0][0])
#     print(fetchedData[0][1])
#     print(fetchedData[0][2])
#     print(fetchedData[0][3])
#     
    for i in range(n):
        instance = Node(fetchedData[i][0], fetchedData[i][1], fetchedData[i][2], fetchedData[i][3])
        nodes.append(instance)   
        
    print("pulled") 
    
#Creates dictionary to find id and values


# This function populates and array where row[0] and col[0] are the identifiers
# Look up table from id to id in row -> col
def createArray(id):
    global n
    global nodes
    global scale

    id = int(id)
    
    points = []
    map = [[0 for i in range(n+1)] for j in range(n+1)]
    
    for j in range(n):
        map[0][0] = 0
        map[0][j+1] = nodes[j].id 
        map[j+1][0] = nodes[j].id
        # print(nodes[j].id)
        for i in range(n):
            if(map[i][j] == 0):
                if(i == j):
                    map[i][j] = -1
                else:    
                    calculation = calculate(nodes[j].lat, nodes[j].lon, nodes[i].lat, nodes[i].lon, nodes[j].weight, nodes[i].weight)
                    if(calculation > scale):
                        scale = calculation
                    map[i][j] = calculation
                    
    #for q in range(n):
    #    print()
    #    for p in range(n):
    #        sys.stdout.write(str(map[q][p]) + "  ")
    points_data = {}
    for q in range(n):
        arrayPoint = {
            'id':q+1,
            'points':map[id][q]
        }
        
        points.append(arrayPoint)
        
    points_data['points'] = points
    print(points_data)
    return points_data

            
# Calculates the point between each node in the array
def calculate(orig_lng, orig_lat, dest_lng, dest_lat, threshold_begin, threshold_end):
    
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
    
    if(threshold_end > 0.75):
        return 0
    
    if(threshold_end < 0.25 and threshold_begin > 0.75):
        pointA = distance * 2
        distance = getPoint(pointA)
        return distance
    
    if(threshold_begin < 0.50 and threshold_end > 0.50):
        pointA = distance / 2
        distance = getPoint(pointA)
        return distance
    
    if(threshold_begin > 0.50 and threshold_end < 0.50):
        pointA = distance
        distance = getPoint(pointA)
        return distance;
    
    else:   
        pointA = distance * 2
        distance = getPoint(pointA)
        return distance
    
# Returns the points gained for each location in the array   
def getPoint(pointA):
    global scale
    
    if (pointA > 21):
        return 9
    if (pointA < 3):
        return 0
    else:
        pointA = pointA / 3
        pointB = round(pointA)
        return int(pointB)

def talkToSite(id):
    global n
    global map
    
    pullFromDB()
    result = createArray(id)
    
    #print(result)
    return result
        
#Main function            
def main():
    talkToSite(5)  
    
    
    
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

#print time.asctime( time.localtime(time.time()) )
#main()
#print time.asctime( time.localtime(time.time()) )
