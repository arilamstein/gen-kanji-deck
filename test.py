from bs4 import BeautifulSoup
from urllib2 import urlopen

url = "http://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji"
#soup = BeautifulSoup(urlopen(url))
soup = BeautifulSoup(urlopen(url), 'html.parser')

print soup.prettify()
