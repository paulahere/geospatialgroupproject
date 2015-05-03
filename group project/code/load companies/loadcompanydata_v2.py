# author paula white
# 18th April 2015
# 
#
# import libraries, and set pd as the pandas alias
# note colunm for CompanyNumber is actually a string and need reformatting in excell
# there is alse a change to the data model to chnage type for company_no

import pandas as pd
# import the SQLAlchemy libraries 
from sqlalchemy import create_engine

pdOrgs = pd.read_csv('e:\data\paula\geospatial\dataload\company\organizationspartas.csv')
pdCompanies = pd.read_csv('e:\data\paula\geospatial\dataload\company\BasicCompanyDataPartAs.csv')
#pdCompanies = pd.read_csv('e:\data\paula\geospatial\dataload\company\BasicCompanyDataPart1.csv')
#pdCompanies = pd.read_csv('e:\data\paula\geospatial\dataload\company\BasicCompanyDataPart1.csv')


dfOrgs = pd.DataFrame(data = pdOrgs, columns =['primary_role','name', 'homepage_url', 'profile_image_url', \
'facebook_url','twitter_url','linkedin_url','location_city','location_country_code','short_description'])

dfCompanies = pd.DataFrame(data = pdCompanies, columns =['CompanyName','CompanyNumber', 'PostTown', 'CompanyStatus', \
'CountryOfOrigin','IncorporationDate'])

print dfCompanies

engine = create_engine('mysql://ucfnpwh:kufefopuno@128.40.150.34:3306/ucfnpwh', echo=True)
    
conn = engine.raw_connection()
cursor = conn.cursor()

city_list = set(['EXETER','MANCHESTER','LIVERPOOL','SHEFFIELD', 'BIRMINGHAM', 'LEEDS','LEICESTER', \
                                   'BRISTOL','CARDIFF','CAMBRIDGE', \
                                   'BELFAST', 'ABERDEEN', 'EDINBURGH','GLASGOW','BRADFORD', 'LONDON' , \
                                   'BOURNEMOUTH', 'BRIGHTON', 'LIVERPOOL', 'READING'])
                                   


#for i in range(0, len(dfCompanies)):
for i in range(0, 300):
    #print "companies found"
    #ukCountry = 'United Kingdom'
    #testCountrty = []
    #testCountry = str(dfCompanies['CountryOfOrigin'][i])
    #if  testCountry.find(ukCountry):
    #    print"uk companies found"
    #    
    #    testCompany= []
    #    tsetCompany = str
    #    
    #print "city" , dfCompanies['PostTown'][i]
    #print "status" , dfCompanies['CompanyStatus'][i]
        
    if dfCompanies['CountryOfOrigin'][i] == 'United Kingdom':
        if (dfCompanies['PostTown'][i] in city_list):
            if dfCompanies['CompanyStatus'][i] =='Active':
    
           
                print " our cites found"
                # #convert city name to lower case so consitent comparisons can be made
                city = []
                city = dfCompanies['PostTown'][i]
                city = city.lower()
            
                #find city foreight key
                sqlstatement = 'SELECT CITY_NO FROM City WHERE Name ='+ "'"  + city +"'" 
                #print "sql =", sqlstatement
                cursor.execute(sqlstatement)
                row = cursor.fetchone()
                
               
                # need to do some checks that  key not null              
                cityForeignKey = row[0]
             
                #print "foreign key" , cityForeignKey
                
                companyName =dfCompanies['CompanyName'][i]
                
                # get ride of names with one single quote a the begining as SQL won't work - reple with a space
                if "'" in companyName:
                    companyName = companyName.replace("'", " " )
                
                print "compacny number" ,str(dfCompanies['CompanyNumber'][i])
                # might need to domsomething else here - for now don't insert ones with null for primary key    
                if str(dfCompanies['CompanyNumber'][i]) != 'nan':
                    
                           
                    date_sql = []
                    date_sql ='STR_TO_DATE(' +  "'"+ str(dfCompanies['IncorporationDate'][i]) +"'"  + "," +  "'"+'%d/%m/%Y'+"'"  +')' 
                    #print "datesql" , date_sql 
            
                    sqlstatement = 'INSERT INTO COMPANY(COMPANY_NO,NAME,FOUNDED, CITY_NO) VALUES (' + "'" + str(dfCompanies['CompanyNumber'][i]) +"'" + ','  \
                                                                     + "'"+ companyName +"'"+ ',' \
                                                                     + date_sql + ',' \
                                                                     + str(cityForeignKey) +")"
                                                            
                                                                     
                    print "sql" , sqlstatement                                 
                    result = cursor.execute(sqlstatement)
                    
#print" company updates"    
           
#for j in range(0, len(dfOrgs)):
#    if dfOrgs['primary_role'][j] == 'company':
        
#        print "name" , str(dfOrgs['name'][j])
#        print "website", str(dfOrgs['homepage_url'][j])
#        print "image", str(dfOrgs['profile_image_url'][j])
#        print "desc" ,str(dfOrgs['short_description'][j])
            
#        #add update statment here with additional data
#        sqlstatement = 'UPDATE COMPANY SET WEBSITE_URI =' + "'" + str(dfOrgs['homepage_url'][j]) + "'"+ ',' \
#                                                    + 'SET DESCRIPTION =' + "'" + str(dfOrgs['short_description'][j]) + "'"+ ',' \
#                                                    + 'SET IMAGE_FILENAME ='+ "'" + str(dfOrgs['profile_image_url'][j]) + "'" + ',' \
#                                                  + 'WHERE NAME=' + "'" + str(dfOrgs['name'][j]) +"'"
#                                                 
#    print "sql =", sqlstatement
#    cursor.execute(sqlstatement)
                                                    
                   
                                                        
      
      
                                                             
conn.close()
