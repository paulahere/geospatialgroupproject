# import libraries, and set pd as the pandas alias
import pandas as pd

# run this command too - just to allow more data to be displayed than default
pd.set_option('display.max_rows', 300)
# REPLACE THE DIRECTORY BELOW WITH THE LOCATION OF YOUR FILE!

# this command loads your csv data and sets up the 'smog' dataframe, using the Pandas (pd) libraries
# subset of data starting with JE-JEC
company = pd.read_csv('E:\data\paula\geospatial\dataload\company\BasicCompanyDataPartJE.csv')
# read subset orgs


print "company load" ,company.count()

company_active = company[company.CompanyStatus == 'Active']

print  "company active", company_active.count()

uk_company_active = company[company.CountryOfOrigin == 'United Kingdom']

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

#see what's ben added
created_data = pd.read_sql('Select * from NewCompany', conn)
print "created data",  created_data
