import urllib2
from bs4 import BeautifulSoup

url = raw_input("Enter URL: ")
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

names = []

while count > 0:
    print "retrieving: {0}".format(url)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    anchors = soup('a')
    name = anchors[position-1].string
    names.append(name)
    url = anchors[position-1]['href']
    count -= 1

print names[-1]