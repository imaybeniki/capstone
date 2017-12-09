'''
Created on Nov 13, 2017

@author: christopher
'''


import csv
import random
from time import sleep
from geopy import geocoders
from geopy.geocoders import GoogleV3
from Passwords import googlePassword

pwGoogle=googlePassword


geolocator= geocoders.GoogleV3(pwGoogle)


prevLocations=[]

def importPastCoordinates(importFile):
    """
    Import past geocoded GPS coordinates from CSV file 
    to add to prevLocations list
    
    Parameters
    ---------
    importFile : str
        File to read string values from
    """
    iFile=open(importFile)
    readerCSV=csv.reader(iFile,delimiter=",")
    for row in readerCSV:
        if row:
            usedCoordinate=row[0]+","+row[1]
            prevLocations.append(usedCoordinate)
            print("Past coordinate: ",usedCoordinate)
        
    iFile.close()

#change to method
def updateUhaulCSV(readfileName,writeFileName,prevFile, theLat, theLong):
    """
    Updates formatted CSV Uhaul file
    
    This function reads the latitude and longitude row information from the readFileName file, correctly
    formats it, and writes it to the writeFile name, while tracking and adding used coordinates to the prevFile so that 
    previous coordinates will not be checked again.
    
    Parameters
    ----------
    readFileName: str
        File name of file that holds raw location information.
    writeFileName: str
        File name of file that will be written to with formatted location data.
    prevFile: str
    File name of CSV file that holds previous addresses. Used address will be written to this file so that
    transactions do not need to be rerun on them in the future.
    theLat: int
        Row number in readFileName file that contains the lattitude information.
    theLong: int
        Row number in the readFileName file that contains the longitude information.
    
    
    
    """
    
    with open(readfileName) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        with open(writeFileName,'a') as csvWrite:
            writer=csv.writer(csvWrite,delimiter=",")
            with open(prevFile,'a') as coordinateWrite:
                coordWriter=csv.writer(coordinateWrite,delimiter=",")                
                

                
                
                #row nhmbers of latitude and longitude
                rowLat=theLat
                rowLong=theLong
                
                for row in readCSV:
                    
                    # occupied spaces
                    occ = random.randrange(0, 11)
                    # capacity of bikerack
                    cap = 10.0
                    # percentage of bike rack full
                    weight = occ / cap
                    
                    flag = "N/A"
                    if(weight <= .20):
                        flag = 'G'
                    if((weight > .20) & (weight < .80)):
                        flag = 'Y'
                    if((weight >=.80) & (weight <= 1.00)):
                        flag = 'R'
                    if(weight > 1.0):
                        print("value not less than or equal to 10")
                    
                    lat=row[rowLat]
                    longe=row[rowLong]
                    
                    latVal=str(lat)
                    longVal=str(longe)
                    
                    coordinate=(latVal+","+longVal)
                    
                    print(coordinate)
                    tableCoord=(lat,longe)
                    coordWriter.writerow(tableCoord)
                    print(coordinate, "added to coordinate csv")
                    
                    #Skip insertion of coordinate into tables if values already exist
                    if(prevLocations.__contains__(coordinate)):
                        print("Location already used. Skipping to next value")
                        continue
                    
                    
                    prevLocations.append(coordinate)
                    
                        
                    location=geolocator.reverse(coordinate,timeout=10)
                    location=location[0];
                    sleep(1)
                    if location:
                    
        #                 print(location.address)
                        fullAddress=location.address
                        fullAddress=fullAddress.split(",")
                        retAddress=fullAddress[0]
                        city=fullAddress[len(fullAddress)-3]
  
                        stateAndZip=fullAddress[len(fullAddress)-2]

                        stateAndZip=stateAndZip.split(" ")
                        state=stateAndZip[1]
                        zipCode=stateAndZip[2]

                        longe=location.longitude
                        lat=location.latitude
                        print ("INSERT INTO LOCATIONS( lOCATION_ADDRESS, LOCATION_CITY, lOCATION_STATE,LOCATION_ZIP,LOCATION_LAT,LOCATION_LONG,CAPACITY,OCCUPIED,WEIGHT,FLAG) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
                        print(retAddress,city,state,zipCode,lat,longe,cap,occ,weight,flag)                 
                        
                        #write formatted date to csv file
                        writedata=(retAddress,city,state,str(zipCode),str(lat),str(longe),str(cap),str(occ),str(weight),flag)
                        writer.writerow(writedata)
                        print(retAddress, "added to csv")       
                        
                    
                   
                    if not location:#((location.address is None) or (location.longitude is None) or (location.latitude is  None)):
                        print("null location. skipping value")
                        continue
        
        
def main():
    importPastCoordinates('/home/christopher/uhaulprevcoordinate.csv')
    updateUhaulCSV("/home/christopher/Downloads/UHAUL.csv",'/home/christopher/UhaulFormatted.csv','/home/christopher/uhaulprevcoordinate.csv',1,0)        
        


main()       
        