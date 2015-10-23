from bs4 import BeautifulSoup
import urllib2

sites = {
    "deer":"http://www.dgif.virginia.gov/hunting/regulations/deer.asp":"",
    "bear":"http://www.dgif.virginia.gov/hunting/regulations/bear.asp",
    "elk":"http://www.dgif.virginia.gov/hunting/regulations/elk.asp",
    "turkey":"http://www.dgif.virginia.gov/hunting/regulations/turkey.asp",
    "springturkey": "http://www.dgif.virginia.gov/hunting/regulations/turkey.asp#spring"
    "crow":"http://www.dgif.virginia.gov/hunting/regulations/smallgame.asp#crow",
    "groundhog":"http://www.dgif.virginia.gov/hunting/regulations/smallgame.asp#groundhog",
    "grouse":"",
    "quailandpheasants":"",
    "rabbit":"",
    "squirrel":"",
    }

data = {}

for animal,url in sites.iteritems():
    f = urllib2.urlopen(url)
    soup = BeautifulSoup(f, 'html.parser')
    data[animal] = soup.get_text()
    print(soup.get_text())
