import urllib2
import json, re, csv
from bs4 import BeautifulSoup, Tag,SoupStrainer

# load the page mon
page = urllib2.urlopen("http://espn.go.com/nhl/standings/_/group/1")
masterPage = BeautifulSoup(page)
table=masterPage.find("table")

rows = table.findAll('tr', {'class':['evenrow', 'oddrow']})

master_list = {}

for tr in rows:
    cols = tr.findAll('td')
    team = cols[0].text[0:-1]
    goalDiff= cols[13].text
    master_list[team] = goalDiff

json.dump(master_list, open('goalDiff_data.json', 'wb'))