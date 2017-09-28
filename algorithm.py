#Connects to server, waits for JSON object
def connect():

#Reads in a JSON object and stores the data
#Parse JSON object 
def readJSON(object):

#Store key, value pairs
#Read in from DynamoDB to get values of each loc.
#Returns a multiplier based on the location given
def findMultiplier(location):

#Creates and populates the 2D array
#Reads in from DynamoDB to fill row/col 0 with locations
#Calls calculatePoints() to determine innards of array
def makeTable():
  #this int will come from the number of entries given by the data base (row and col will be equal)
  int matrix = 0;
  #x = [[int for i in range(10)] for j in range(10)]

#Determines points for each location
#Parameters are tuples of (latitude, longitude) which is the key in the key/value pair
def calculatePoints(to, from):
  #find the value for the corresponding to key
  #multiply the key by the distance between the two points
  #using a map API? lat, long differences?

#Calls the functions, returns to UI
def main():
  #poll every 10 seconds to calculate points
  #populate the table accordingly
  #read in from server for JSON object
  #find the multiplier between the distances
  #calculate the points and return to the UI
