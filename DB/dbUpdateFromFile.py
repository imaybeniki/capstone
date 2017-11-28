'''
Created on Nov 28, 2017

@author: christopher
'''

import csv
import psycopg2
from psycopg2._psycopg import IntegrityError

def updateFormatted(Filename):
    ifile=open(Filename)
    reader=csv.reader(ifile)
    
    database = psycopg2.connect (database = "ebdb", user="capstone", password="capstone123", host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")   
    cursor=database.cursor()
    for row in reader:
        address=row[0]
        city=row[1]
        state=row[2]
        intZip=float(row[3])
        lat=float(row[4])
        longe=float(row[5])
        cap=float(row[6])
        occ=float(row[7])
        weight=float(row[8])
        flag=row[9]
        
        
        try:
            statement= "INSERT INTO LOCATIONS( lOCATION_ADDRESS, LOCATION_CITY, lOCATION_STATE,LOCATION_ZIP,LOCATION_LAT,LOCATION_LONG,CAPACITY,OCCUPIED,WEIGHT,FLAG) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            data=(address,city,state,intZip,lat,longe,cap,occ,weight,flag) 
            cursor.execute(statement,data)
            print(address, "added to db")  
        except IntegrityError:
            print("location is not accepted or has already been used. skipping to next value")
        
    cursor.close()
    database.commit()
    database.close()
    ifile.close()
def main():
    redboxFile='/home/christopher/RedboxFormatted.csv'
    uhaulFile='/home/christopher/UhaulFormatted.csv'
    bikeshareFile='/home/christopher/BikeShareFormatted.csv'
    updateFormatted(redboxFile)
    
    
main()        
             