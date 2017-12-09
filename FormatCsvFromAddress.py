'''
Created on Nov 14, 2017

@author: christopher
'''
import string
from psycopg2._psycopg import IntegrityError
from time import sleep
'''
Created on Oct 30, 2017

@author: christopher
'''


import csv
import random
from geopy import geocoders
from Passwords import googlePassword
from geopy.geocoders import GoogleV3
import time



googlePw=googlePassword



geolocator= geocoders.GoogleV3(googlePw)



prevAddr=[]
values=[]

def importPastAddresses(PastAddressFile):
    """
    Adds already used addresses to prevAddr list.
    
    Parameters
    ----------
    PastAdressFile: str
        the file name in which the previous addressses are stored
        
    
    """
    
    print("reading past adresses from:",PastAddressFile)
    sleep(2)
    for i in prevAddr:
        del i 
    if(len(prevAddr)==0):
        print("empty list")    
    iFile=open(PastAddressFile)
    readerCSV=csv.reader(iFile,delimiter=",")
    for row in readerCSV:
        if row:
            usedAddress=row[0]
            prevAddr.append(usedAddress)
            print("used address: ",usedAddress)
        
    iFile.close()
    

#change to method
def updateAddress(ReadFile, WriteFile,rowNum):
    """
    Formats addresses from raw location data and writes to CSV file
    
    Parameters
    ----------
    ReadFile: str
        The file that contains the raw data. This will be read and reformatted
    WriteFile: str
        The file that will received the formatted data for later insertion into the databse
    rowNum: int
        the row number in the Readfile that contains the adress information for geocoding
    """
    with open(ReadFile) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        print("reading locations from:", ReadFile)
        sleep(2)
        #counter
        with open(WriteFile,'a') as csvWrite:
            writer=csv.writer(csvWrite,delimiter=",")
            print("Appending location data to:", WriteFile)
            sleep(2)
            k=1
            rowNumber=rowNum
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
                
                
                tempAddress=(row[rowNumber])

                
                tempAddress=str(tempAddress)
                adress=tempAddress.replace("\n", " ")
               
                adress=adress.replace("\r","")
                
                
                #print("replace:", adress)
                neededAddress=tempAddress.split('\n')
                neededAddress=neededAddress[0]
                finalAddress=neededAddress.split("\r")
                finalAddress=finalAddress[0]
                
                print("Needed address::" +neededAddress)
                
                
                if finalAddress in prevAddr:
                    print(finalAddress, "address already used, skipping value")
                    continue
                prevAddr.append(finalAddress)
                
               
            
                
                    
                location = geolocator.geocode(adress,timeout=10)

                sleep(2)
        
                 
                
                if not location:
                    print("null location. skipping value")
                    continue
                if location:
                    print("location:")
                    print(location)
                    longe = float(location.longitude)
                    lat=float(location.latitude)
                    print("latitude:",lat)
                    print("longitude",longe)
                    
                
                 
        
                 
                theAddr = location.address
                addCopy=theAddr
#                
                sp=addCopy.split(',')
                theLength=len(sp)-1
                city=sp[theLength-2]

                
                state=sp[theLength-1]
                stZip=state.split(" ")
                state=stZip[len(stZip)-2]
                zipCode=stZip[len(stZip)-1]
                intZip=int(zipCode)  
                
                
                 
                     
                 
                 
                     
                
                print("verification of final address:",finalAddress ) 
               
                print(k,finalAddress,city,state,intZip, lat, longe, occ, cap, weight, flag)
                k=k+1     
                 
                 

                writedata=(finalAddress,city,state,str(intZip),str(lat),str(longe),str(cap),str(occ),str(weight),flag)
                writer.writerow(writedata)

            
                






            

    

                
            

