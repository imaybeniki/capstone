# Capstone
Redistribution Algorithm and User Interface  
algorithm.py:  
Connects to instances in AWS. This program reads in a JSON object from the DB and UI, it populates a 2D array according to the information given. The points that the user will earn is calculated and returned to the DB and UI.  
  
capstoneSite:  
The django framework that is deployed to the AWS Elastic Beanstalk environment. The main website page information can be found in /capstoneSite/mapInterface and /capstoneSite/mapInterface/templates in views.py and index.html.  

database:
files: dbCreate.py,dbInsertCopyFromFile.py, FormatCsvFromAdress.py, formatCapitalBikeShare.py,formatRedBox.py, 
formatUhaul.py

dbCreate.py: Creates the locations table for database.
FormatCsvFromAdress.py: Writes formatted table values to CSV file.
formatRedbox.py: Formats redbox data, writes to CSV file.
formatUhaul.py: Formats uhaul for GPS coordinates, writes to file.
formatCapitalBikeShare.py: Formats capital bike share address, writes to CSV file.
dbInsertCopyFromFile.py: takes formatted CSV and adds dataset to Database


