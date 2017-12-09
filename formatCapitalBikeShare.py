'''
Created on Dec 1, 2017

@author: christopher
'''
import _csv
from psycopg2._psycopg import IntegrityError
from time import sleep
import psycopg2
import csv
import random
from geopy import geocoders
import time

from geopy.geocoders import GoogleV3
from FormatCsvFromAddress import updateAddress

from FormatCsvFromAddress import importPastAddresses


def main():
    """
    Calls importPastAddresses and updateAdresses, then wrties to bikeShareGoogleFormatted.CSV
    """
    pastAdresses="/home/christopher/bikeShareGoogleFormatted.csv"
    write="/home/christopher/bikeShareGoogleFormatted.csv"
    read="/home/christopher/Downloads/Capital_Bike_Share_Locations.csv"
    
    importPastAddresses(pastAdresses)
    updateAddress(read, write,2)
    
main()
