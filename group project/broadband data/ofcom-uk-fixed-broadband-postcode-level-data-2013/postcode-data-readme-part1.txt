16 October 2013

Key to file: ofcom-part1-fixed-broadband-postcode-level-data-2013.csv

NOTES

This file is based on a snap shot of data provided by the largest fixed broadband providers in the UK for the period of June to July 2013. Due to variations in broadband performance over time, the file should not be regarded as a defintive and fixed view of the UK's fixed broadband infrastructure. However, the information provided in this file may be useful in identifying variations in broadband performance by geography and the impact of superfast broadband on overall broadband performance. The file should be viewed in conjunction with the Infrastructure Report published by Ofcom in October 2013, which details how each of the metrics is defined.

Note this file lists the postcode details regarding all the postcodes which are from AB10 1AA in Aberdeen to M33 0DD in Manchester.  There is a second file for postcodes in the second half of the alphabet.

Column headers are as follows:

Postcode - white spaces removed

Postcode Data Status - This field contains one of five options.
 i) No premises - There are no residential or small business delivery points in the postcode as listed from the 2012 file held by europa. There may be large business premises and new built connections in these postcodes more recently than our premises count focuses upon.
 ii) Insufficient Premises -  This status means there are less than three residential or small business premises in the postcode. To protect anonymity broadband data has not been provided for these postcodes.
 iii) Insufficient Data - This status means that we hold data on less than three broadband connections in the postcode. To protect anonymity broadband data has not been provided for these postcodes. 
 iv) No data - We do not hold data on broadband connections in the postcode. This may be because consumers in the postcode have chosen not to subscribe to broadband, or that information was not included in the data provided by the largest ISPs, or that broadband is not available in the postcode.
 v) OK - This means that there are at least three residential or small business premises and that we hold data on at least three broadband connections in the postcode, only the amount of connections is this case.

 When applying the different status values the order of precedence (highest to lowest) is as follows:
 No premises
 No data
 Insufficient Premises
 Insufficient Data
 OK

Information on average sync speed, mean sync speed and sub 2Mbit/s connections is only provided for postcodes with a status of 'OK'

Lines < 2Mbps(Y/N) - A 'Y' indicates whether there are one or more broadband connections with a modem sync speed less than 2.2Mbit/s (for fibre and copper connections) or 2.0 Mbit/s for cable customers. A 'N' indicates there are no lines operating at below 2Mbit/s. 

Average speed/Mbps - This field takes the values of mean modem sync speed of connections in the postcode to 1 decimal place.  If over or equal to 30 Mbit/s, a >= 30 is shown.

Median speed/Mbps - This field picks out the middle modem sync speed in each postcode as if they were all ordered from smallest to highest and the middle one is selected (or average of middle two values if there is an even number of values). If over or equal to 30 Mbit/s, a >= 30 is shown.

Maximum Speed/Mbps - This field calculates the highest modem speed in each postcode in Mbit/s. If over or equal to 30 Mbit/s, a >= 30 is shown.

Superfast Broadband Available(Y/N) - This field indicates whether Virgin Media or Openreach are able to provide superfast broadband services to one or more premises in the postcode. Note, not all premises will necessarily be able to order the service and, for fibre to the cabinet technologies, not all connections will necessarily be able to achieve superfast speeds.

Number of connections - This field lists the amount of active broadband connections within the postcode.  The amount of connections are listed regardless of there being insufficient data to publish any further values.