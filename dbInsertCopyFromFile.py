'''
Created on Dec 4, 2017

@author: christopher
'''

import csv
import psycopg2
from psycopg2._psycopg import IntegrityError
from psycopg2._psycopg import InternalError
from query import printQuery
from Passwords import databasePassword
from dbCreate import createDB


def updateDBFromFile(updateFile):
    """
    Insertion of data into locations table from formatted CSV file.
    
    Parameters:
    -----------
    updateFile: str
        File name of formatted data. This data will be read and inserted into the locations table of the database.
    """
    dbPassword=databasePassword
#     
    with open(updateFile,'r') as file:
    
        
        database = psycopg2.connect (database = "ebdb", user="capstone", password=dbPassword, host="aa1immzi54ninca.cyeyzuoh6sjb.us-east-1.rds.amazonaws.com", port="5432")   
        
        cursor=database.cursor()
        cursor.execute("""Delete from locations""")
        print("previous data deleted")
    
        
        cursor.copy_from(file,'locations',sep =',',columns=('location_address','location_city','location_state','location_zip','location_lat','location_long','capacity','occupied','weight','flag'))
        
    
        
        
        database.commit()
        print("data committed")
        database.close()
    

def main():
    
    redBoxFile='/home/christopher/RedboxFormatted.csv'
    UhaulFile='/home/christopher/UhaulFormatted.csv'
    bikeShareFile='/home/christopher/bikeShareGoogleFormattedOne.csv'
    createDB()
    updateDBFromFile(bikeShareFile)
    printQuery()
    
    
    
    
main()