from bs4 import BeautifulSoup
from urllib2 import urlopen

class Kanji:
	"""
	The Kanji class contains a character plus metadata about that character
	"""

	def __init__(self, character):
		self.character      = character
		self.dictionary_url = self.get_dictionary_url_for_character(character)
		self.jlpt_level     = ""
		self.definition     = ""
		self.examples       = ""

	def get_dictionary_url_for_character(self, character):
		return "http://jisho.org/search/" + character + "%20%23kanji"

	def as_csv(self):
		""" 
		Convert object to csv
		"""
		return ",".join([self.character, 
						 self.dictionary_url, 
						 self.jlpt_level, 
						 self.definition, 
						 self.examples]).encode('utf-8')

def get_characters(): 
	"""
	Gets a list of all joyo kanji characters from wikipedia
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
				characters.append(cells[1].a.contents[0])
	
	return characters

# get all the joyo characters from wikipedia
characters = get_characters()

# write them as a csv file
f = open("kanji.csv", "w")
for c in characters:
	print >> f, Kanji(c).as_csv()

