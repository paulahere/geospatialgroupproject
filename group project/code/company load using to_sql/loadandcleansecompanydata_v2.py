#NOTE DON@T RUN THIS AS DATABASE CAN@T COPE WITH VOLUMNE OF DATA
#BUT MIGHT BE USEFUL JUST TO SEE APPROCAH FOR MERGING CSV AS DOES SEEMS TO WORK
# import libraries, and set pd as the pandas alias
import pandas as pd

# run this command too - just to allow more data to be displayed than default
pd.set_option('display.max_rows', 300)
# REPLACE THE DIRECTORY BELOW WITH THE LOCATION OF YOUR FILE!

# this command loads your csv data and sets up the 'smog' dataframe, using the Pandas (pd) libraries
# subset of data starting with JE-JEC
#note these are all

#company = pd.read_csv('E:\data\paula\geospatial\dataload\company\BasicCompanyDataPartJE.csv')
dfCompany1 = pd.read_csv('E:\data\paula\geospatial\dataload\company\BasicCompanyDataPart1.csv')
dfCompany2 = pd.read_csv('E:\data\paula\geospatial\dataload\company\BasicCompanyDataPart2.csv')

dfAllCompanies = pd.concat([dfCompany1, dfCompany2])

# read subset orgs

# note these are startup only
org = pd.read_csv('E:\data\paula\geospatial\dataload\company\organizations.csv')

print "-----------------------------------------------------"
print "organisations load" , org.count()
print "-----------------------------------------------------"
print "all companies load" , dfAllCompanies.count()
print "-----------------------------------------------------"

company_active = dfAllCompanies[dfAllCompanies.CompanyStatus == 'Active']

print  "company active", company_active.count()

uk_company_active = dfAllCompanies[dfAllCompanies.CountryOfOrigin == 'United Kingdom']

print  "uk company active", uk_company_active.count()

# the lsuffix and rsuffix parameters specify how we handle the matching column names
#smog_join = smog_pivot.join(smog_rat, lsuffix='_val', rsuffix='_ratified')


# import the SQLAlchemy libraries
from sqlalchemy import create_engine

# create the connection string to the MySQL database
# replace USERNAME and PASSWORD with your own credentials 
engine = create_engine('mysql://ucfnpwh:kufefopuno@128.40.150.34:3306/ucfnpwh', echo=True)

# make the connection to the database
conn = engine.raw_connection()

# change TABLENAME for the name of your newly created table
# don't worry about the warning if you get it 
uk_company_active.to_sql('NewCompany', conn, flavor='mysql')


