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

pdOrgs = pd.read_csv('e:\data\paula\geospatial\dataload\company\organizationsas.csv')
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
                                   



                    
print" company updates"    
           
for j in range(0, len(dfOrgs)):
    if dfOrgs['primary_role'][j] == 'company':
        
        orgName = str(dfOrgs['name'][j]).upper()            
        print "name" , orgName
        
        print "website", str(dfOrgs['homepage_url'][j])
        print "image", str(dfOrgs['profile_image_url'][j])
        print "desc" ,str(dfOrgs['short_description'][j])
        
        
        #add update statment here with additional data
        sqlstatement = 'UPDATE COMPANY SET WEBSITE_URI =' + "'" + str(dfOrgs['homepage_url'][j]) + "'"+ ',' \
                                                    + 'SET DESCRIPTION =' + "'" + str(dfOrgs['short_description'][j]) + "'"+ ',' \
                                                    + 'SET IMAGE_FILENAME ='+ "'" + str(dfOrgs['profile_image_url'][j]) + "'" + ',' \
                                                  + 'WHERE NAME=' + "'" + "LIKE " + orgName + "%" 
                                                 
    print "sql =", sqlstatement
    cursor.execute(sqlstatement)
                                                    
                   
                                                        
      
      
                                                             
conn.close()
