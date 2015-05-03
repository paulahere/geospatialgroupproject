# author paula white
# 18th April 2015
# import basic data - long, lat, key and name
# just enough to build node.js service and start hocking in visualisation
# additional work needd to load city table further later
#
# import libraries, and set pd as the pandas alias
#TO DO - change birmingham load to name of just birmingham - not (west midlands)
#change cities sample to tech city report cities







import pandas as pd
# import the SQLAlchemy libraries
from sqlalchemy import create_engine

pdCities = pd.read_csv('N:/Documents/group project/worldcities.csv')

#/Users/freudenthal/Documents/occupationload/worldcities.csv
dfCities = pd.DataFrame(data = pdCities, columns =['CityCode','Country', 'CityName', 'Longitude','Latitude','pop2015'])

#debug code
print dfCities



engine = create_engine('mysql://ucfnpwf:pisexopuce@128.40.150.34:3306/ucfnpwf', echo=True)

conn = engine.raw_connection()
cursor = conn.cursor()

#these are medium and large sized cities a defined by ONS, 
# large cities are 250+, medium 50- 250K
# the excell spreadsheat with global cities in is for  Urban Agglomerations of 300,000 or more
# SO smoe inportant cities were missing that feel between 250-300 e.g Leeds
#so these have been added with their own SQl statmenets after the import
# we may decide to reine list again once we look at teh data but thsi initial list seems like a resonable starting point
# some names extended to match data e.g. Birmingham and portsmouth

medium_large_cities = set(['newcastle', 'liverpool','hull', 'sheffield', 'birmingham', 'cambridge', 'norwich', 'london', 'brighton', 'birmingham', 'bournemouth', 'cardiff', 'edinburgh', 'belfast', 'manchester', 'bristol'])





#'Exeter','Manchester','Liverpool','Sheffield','Newcastle','Birmingham', 'Leeds','Leicester', \
                                   #'Bristol','Southhamton/Portsmouth (South Hampshire)','Cardiff','Cambridge','Stevenage','Lincoln','Worcester','Gravesham', \
                                   #'Wrexham','Belfast','Derby', 'Aberdeen', 'Edinburgh','Glasgow','Bradford', 'London'])
                                   
# cities that are in the global spreadsheet  'London',  'Manchester',  'Birmingham (West Midlands)',  'West Yorkshire', 'Glasgow',  'Southampton/Portsmouth (South Hampshire)'
# 'Liverpool',   'Newcastle upon Tyne', 'Nottingham',  'Sheffield',  'Bristol',  'Belfast',  'Leicester',  'Brighton-Worthing-Littlehampton' 'Edinburgh',  
# 'Bournemouth/Poole', 'Cardiff',  'Teeside (Middlesbrough)',  'Stoke-on-Trent (The Potteries)',  'Coventry-Bedworth',  'Sunderland', 'Birkenhead', 
# 'Reading-Wokingham',  'Preston',  'Kingston upon Hull',  'Newport',  'Swansea',   'Southend-On-Sea',
# - as you can see there are some extras in here too at some stage we may wish to add back in 


for i in range(0, len(dfCities)):
#for i in range(0, 50):
    
    if dfCities['Country'][i] == 'United Kingdom':
        if (dfCities['CityName'][i] in medium_large_cities):
            
            #convert city name to lower case so consitent comparisons can be made
            city = []
            city = dfCities['CityName'][i]
            city = city.lower()
            
            sqlstatement = 'INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (' + str(dfCities['CityCode'][i]) +','  \
                                                                     + "'"+  city +"'" + ',' + str(dfCities['Longitude'][i]) + ',' \
                                                                     + str(dfCities['Latitude'][i]) +')' 
                                                              #       + str(dfCities['pop2015'][i]) +')' 
                                                                     
  
            print "sql= " , sqlstatement                                 
            result = cursor.execute(sqlstatement)
        
        
# add important cities not in data set -Leeds, Exeter, Cambridge, Aberdeen, Bradford, Borunemoth, Reading, Brighton,Liverpool
# these ones although offically medium tbut hink probabaly not worth adding Stevenage,Lincoln, Worcester, Gravesham, Wrexham, Derby, 

# following are in tech city but are called Bournemouth, Reading, Brighton
# add 'Bournemouth/Poole' ,'Reading-Wokingham', 'Liverpool','Brighton-Worthing-Littlehampton' ??

#sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (23055,'leeds',-1.5492, 53.7997)"
#result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (23022,'newcastle',-1.6129165, 54.9778404)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (24077,'liverpool', -3.0000, 53.400)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (24077,'hull', -0.3324433, 53.7443412)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (23055,'sheffield',-1.4647953, 53.3830548)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (25088,'birmingham', -1.8936, 52.4836)"
result = cursor.execute(sql_statement)  

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (23022,'cambridge',-0.1190, 53.7997)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (23022,'norwich',:1.2993494, 52.6281014)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (23022,'london',:-0.1262362, 51.5001524)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (24088,'brighton', -0.1313, 50.8492)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (24055,'bournemouth', -1.8800, 50.720)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (24055,'cardiff', -1.8800, 50.720)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (24055,'edinburgh', -3.1875359, 55.9501755)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (23055,'belfast',-5.9301088, 54.5972686)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (24088,'manchester', -2.2343765, 53.4807125)"
result = cursor.execute(sql_statement)

sql_statement = "INSERT INTO City(CITY_NO,NAME,LONGITUDE,LATITUDE) VALUES (24088,'bristol', -2.5919023, 51.4553129)"
result = cursor.execute(sql_statement)

conn.close()
