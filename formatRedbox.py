'''
Created on Nov 14, 2017

@author: christopher
'''
import string
from psycopg2._psycopg import IntegrityError
from time import sleep
import FormatCsvFromAddress
from geocoder.api import google
'''
Created on Oct 30, 2017

@author: christopher
'''

import psycopg2
import csv
import random
from geopy import geocoders
from geopy.geocoders import GoogleV3
import time
from FormatCsvFromAddress import importPastAddresses
from FormatCsvFromAddress import updateAddress
from Passwords import googlePassword

gPassword=googlePassword

ifile=open('/home/christopher/googlePassword.txt')
googlePw=ifile.read()
ifile.close()

geolocator= geocoders.GoogleV3(gPassword)



            
                
def main():
    """
    Calls importPastAddresses and updateAdresses, then wrties to RedboxFormatted.CSV
    """
    readFile='/home/christopher/Downloads/Redbox.csv'
    writeFile='/home/christopher/RedboxFormatted.csv'
    pastAddresses='/home/christopher/RedboxFormatted.csv'
    importPastAddresses(pastAddresses)        
    updateAddress(readFile,writeFile,3)                





main()





            

    

                
            

