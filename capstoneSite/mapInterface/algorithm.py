from math import radians, cos, sin, asin, sqrt, atan2
import psycopg2


# ------global variables-------------------#
n = 0  # size of the nxn matrix
nodes = []  # list to hold the nodes in the database
scaleDivision = 0  # size to scale the points by
scaleSubtraction = 100  # scale to normalize the data by
debug = True


# ------------------------------------------#


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


# This function pulls from the database and uses the DB values to intialize nodes
def pullFromDB():
    global n
    global nodes
    global debug

    debug = True

    if (debug):
        conn = psycopg2.connect(database="ebdb", user="capstone", password="capstone123",
                                host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")

    else:
        connectionString = "dbname='%(NAME)s' user='%(USER)s' host='%(HOST)s' password='%(PASSWORD)s'" % DATABASES[
            'default']
        conn = psycopg2.connect(connectionString)

    cursor = conn.cursor()
    cursor.execute("select LOCATION_NUMBER, LOCATION_LAT, LOCATION_LONG, WEIGHT from LOCATIONS")
    fetchedData = cursor.fetchall()

    n = len(fetchedData)

    nodeZero = Node(0, 0, 0, 0.0)
    nodes.append(nodeZero)
    for i in range(n):
        instance = Node(fetchedData[i][0], fetchedData[i][1], fetchedData[i][2], fetchedData[i][3])
        nodes.append(instance)

    if (debug):
        print("Data pulled")


# creates an array populated with points
# map[0] is the id number, map[i] corresponds with each node
# returns dictionary with ID # and point for selected node paths
def createArray(id):
    global n
    global debug

    print(n)

    id = int(id)
    points = []
    map = [0] * n

    for i in range(n):
        if i == 0:
            map[i] = id
        elif i == id:
            map[i] = -1
        else:
            calculation = calculate(nodes[id].lon, nodes[id].lat, nodes[i].lon, nodes[i].lat, nodes[id].weight,
                                    nodes[i].weight)
            map[i] = calculation

    points_data = {}
    for q in range(1, n):  # make n start at 1
        arrayPoint = {
            'id': q,
            'points': int(map[q])
        }
        points.append(arrayPoint)

    points_data['points'] = points
    if (debug):
        print(points_data)
    return points_data


# TODO: make a chart to check with
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

    if threshold_end >= 0.80:
        return 0

    elif threshold_begin <= 0.20:
        return 0

    elif threshold_end <= 0.30 and threshold_begin >= 0.70:
        pointA = distance * 2
        distance = getPoint(pointA)
        return distance

    else:
        pointA = distance
        distance = getPoint(pointA)
        return distance


# TODO: Fix the scale
# Returns the points gained for each location in the array
def getPoint(pointA):
    global n
    if n < 500:
        pointA = sqrt(pointA)
        pointA = pointA / 3
        if pointA > 9:
            pointA = 9
        return int (round(pointA))
    else:
        pointA = sqrt(pointA)
        pointA = pointA / 12
        if pointA > 9:
            pointA = 9
        return int (round(pointA))


# Method to call for receiving points value to each node
# Parameter is the ID of the node traveling from
# Returns a dictionary of node IDs and points
def talkToSite(id):
    global n
    global map
    global debug

    pullFromDB()
    result = createArray(id)

    if (debug):
        print(result)

    return result


talkToSite(17)

