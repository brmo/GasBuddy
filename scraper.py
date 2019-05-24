# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".


import urllib2
import scraperwiki 
import time
# from time import strftime
from BeautifulSoup import BeautifulSoup

scraperwiki.sqlite.save(unique_keys, data, table_name="swdata", verbose=2)
CREATE TABLE `swdata` (`trend` text, `now` real, `cityName` text, `cityTableAveragePrice` text)
CREATE TABLE `swdata` (`trend` text, `now` real, `cityName` text, `cityTableAveragePrice` text)
        scraperwiki.sqlite.save(unique_keys=['country'], data=data)
def removeNL(x):

def removeNL(x):
    """cleans a string of new lines and spaces"""
    s = x.split('\n')
    s = [x.strip() for x in s]
    x = " ".join(s)
    return x.lstrip()


# Create/open a file for data storage
f = open('gasprices-hamilton.txt', 'w')


#timestamp for this scraping
now = time.time()


# Open gasbuddy url and load to Beautiful Soup
url = "http://www.hamiltongasprices.com/"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)


# Cityname
cityName = soup.findAll('table')[1].tr.th.string
if '\n' in cityName:
        cityName = removeNL(cityName)
cityName  = cityName.replace('  ',' ')


# Price trending as per Gas Buddy, these strings are part of the trend image src
trendUp = 'trend_up'
trendDown = 'trend_down'
trendFlat = 'flat'

cityTableTrendImg = soup.findAll('table')[1].findAll('tr')[1].findAll('td')[3].findAll('img')
cityTableTrendSRC = cityTableTrendImg[0]['src']

if trendUp in cityTableTrendSRC:
    trend = 'Rising'

if trendDown in cityTableTrendSRC:
    trend = 'Falling'

if trendFlat in cityTableTrendSRC:
    trend = 'Stable'


# cityTableRow = soup.findAll('table')[1].findAll('tr')[1]
cityTableAveragePrice = soup.findAll('table')[1].findAll('tr')[1].findAll('td')[1].find(text=True)
if '\n' in cityTableAveragePrice:
        cityTableAveragePrice = removeNL(cityTableAveragePrice)
cityTableAveragePrice  = cityTableAveragePrice.replace('  ',' ')


# prepare and save data to sqlite
scrapedata = { 'now': now, 'cityName': cityName, 'cityTableAveragePrice': cityTableAveragePrice, 'trend': trend }
# print scrapedata


scraperwiki.sqlite.save(unique_keys=['now'],data=scrapedata)






