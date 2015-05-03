# KNOWN ISSUES currently low match rate from companies house onto crunch base - so data not helping that much :-(
# currently incorporation date missing fro most companies
# import libraries, and set pd as the pandas alias
import pandas as pd

# run this command too - just to allow more data to be displayed than default
pd.set_option('display.max_rows', 300)
# REPLACE THE DIRECTORY BELOW WITH THE LOCATION OF YOUR FILE!

# this command loads your csv data and sets up the 'smog' dataframe, using the Pandas (pd) libraries
# subset of data starting with JE-JEC
#note these are all

#company = pd.read_csv('E:\data\paula\geospatial\dataload\company\BasicCompanyDataPartJE.csv')
dfCmpny1 = pd.read_csv('E:\data\paula\geospatial\dataload\company\BasicCompanyDataPart1.csv')
dfCmpny2 = pd.read_csv('E:\data\paula\geospatial\dataload\company\BasicCompanyDataPart2A.csv')

#nottaion to drop columns
#dfCompnay1 = dfCmpny1.drop('column_name', 1)

dfCompany1 = pd.DataFrame(data=dfCmpny1, columns=['CompanyName', 'CompanyNumber','PostCode', 'PostTown', 'CompanyStatus','CountryOfOrigin','IncorporationDate'])
dfCompany2 = pd.DataFrame(data=dfCmpny2, columns=['CompanyName', 'CompanyNumber','PostCode', 'PostTown', 'CompanyStatus','CountryOfOrigin','IncorporationDate'])


dfAllCompanies = pd.concat([dfCompany1, dfCompany2])

# read subset orgs

# note these are startup only
dfOrg = pd.read_csv('E:\data\paula\geospatial\dataload\company\organizations.csv')

dfOrg = pd.DataFrame(data=dfOrg, columns=['primary_role','name','homepage_url','facebook_url','twitter_url','linkedin_url','stock_symbol','location_city','location_country_code','short_description'])

print "-----------------------------------------------------"
print "organisations load" , dfOrg.count()
print "-----------------------------------------------------"
print "all companies load" , dfAllCompanies.count()
print "-----------------------------------------------------"

dfUKCompanyActive = dfAllCompanies[(dfAllCompanies.CompanyStatus == 'Active') & (dfAllCompanies.CountryOfOrigin == 'United Kingdom')]

print  "company uk active", dfUKCompanyActive.count()

#dfUkCompanyActive = dfCompanyActive[dfCompanyActive.CountryOfOrigin == 'United Kingdom']

#print  "uk company active", dfUkCompanyActive.count()

print  "orgs", dfOrg.count()

dfUKOrg = dfOrg[dfOrg.location_country_code =='GBR']
print "-----------------------------------------------------"
print  "uk orgs", dfUKOrg.count()


print "-----------------------------------------------------"
print "org company names b4", dfUKOrg['name']
# make case consistent and strip off anything that might make strings not match
dfUKOrg['name'] = dfUKOrg['name'].str.lower();
dfUKOrg['name'] = dfUKOrg['name'].str.strip('limited')
dfUKOrg['name'] = dfUKOrg['name'].str.strip('ltd')
dfUKOrg['name'] = dfUKOrg['name'].str.strip('(uk)')
dfUKOrg['name'] = dfUKOrg['name'].str.strip('(london)')
dfUKOrg['name'] = dfUKOrg['name'].str.strip('"')
print "-----------------------------------------------------"
print "org company names after", dfUKOrg['name']
print "-----------------------------------------------------"
print " company names b4", dfUKCompanyActive['CompanyName']
# make case consistent and strip off anything that might make strings not match
dfUKCompanyActive['CompanyName'] = dfUKCompanyActive['CompanyName'].str.lower()
dfUKCompanyActive['CompanyName'] = dfUKCompanyActive['CompanyName'].str.strip('limited')
dfUKCompanyActive['CompanyName'] = dfUKCompanyActive['CompanyName'].str.strip('ltd')
dfUKCompanyActive['CompanyName'] = dfUKCompanyActive['CompanyName'].str.strip('(uk)')
dfUKCompanyActive['CompanyName'] = dfUKCompanyActive['CompanyName'].str.strip('(london)')
dfUKCompanyActive['CompanyName'] = dfUKCompanyActive['CompanyName'].str.strip('"')
print " company CompanyNames after", dfUKCompanyActive['CompanyName']
print "-----------------------------------------------------"


# only merges if found in crunch base
dfNewCompanies = pd.merge ( dfUKOrg, dfUKCompanyActive, how='left', left_on='name', right_on='CompanyName')





#import the SQLAlchemy libraries
from sqlalchemy import create_engine

# create the connection string to the MySQL database
# replace USERNAME and PASSWORD with your own credentials 
engine = create_engine('mysql://ucfnpwh:kufefopuno@128.40.150.34:3306/ucfnpwh', echo=True)

# make the connection to the database
conn = engine.raw_connection()

# change TABLENAME for the name of your newly created table
# don't worry about the warning if you get it 
dfNewCompanies.to_sql('NewCompany', conn, flavor='mysql')
#

