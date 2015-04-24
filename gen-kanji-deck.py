from bs4 import BeautifulSoup
from urllib2 import urlopen

def get_joyo_kanji(): 
	"""
	Gets a list of all joyo kanji from wikipedia
	For information on joyo kanji see: http://en.wikipedia.org/wiki/J%C5%8Dy%C5%8D_kanji
	"""

	joyo_kanji_url = "http://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji"
	soup = BeautifulSoup(urlopen(joyo_kanji_url), 'html.parser')

	characters = []
	# the kanji are in the 2nd column of this table
	for row in soup.findAll('table')[2].findAll('tr'):
		cells = row.findAll('td')
		if len(cells) > 0: # i.e., ignore the header
			if cells[1].a.contents:
				print cells[1].a.contents[0]
				characters.append(cells[1].a.contents[0])
	
	return characters

def get_url_from_kanji(kanji):
	#return something like this for each kanji
	#http://jisho.org/search/%E4%B8%80%20%23kanji
	return

def get_jlpt_level_from_page(page):
	return

def get_definitions_from_page(page):
	return

def get_common_words_from_kanji(kanji):
	# no idea where to get this from
	return

def generate_card_from_data(data):
	return

kanji = get_joyo_kanji()
for k in kanji:#
	print k

print len(kanji)