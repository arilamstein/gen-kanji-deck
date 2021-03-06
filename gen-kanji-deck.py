from bs4 import BeautifulSoup
from urllib2 import urlopen

class Kanji:
	"""
	The Kanji class contains a character plus metadata about that character
	"""

	def __init__(self, character, grade):
		self.character      = character
		self.grade          = grade
		self.dictionary_url = "http://jisho.org/search/" + self.character + "%20%23kanji"

	def get_jlpt_level(self, soup):
		el = soup.find(attrs={'class': ('jlpt')})
		if el:
			return el.strong.contents[0]
		else:
			return "NA"

	def get_definition(self, soup):
		el = soup.find(attrs={'class':'kanji-details__main-meanings'})
		if el:
			return el.contents[0].encode('ascii').strip()
		else:
			return "NA"

	def get_data_from_dictionary(self):
		print self.dictionary_url
		soup = BeautifulSoup(urlopen(self.dictionary_url.encode('utf-8')), 'html.parser')
		
		self.jlpt_level = self.get_jlpt_level(soup)
		self.definition = self.get_definition(soup)

		self.examples   = "c"

	def as_csv(self):
		""" 
		Convert object to csv
		"""
		return ",".join([self.character, 
						 self.grade,
						 self.dictionary_url, 
						 self.jlpt_level, 
						 '\"' + self.definition + '\"', 
						 self.examples]).encode('utf-8')

def get_kanji_from_wikipedia(): 
	"""
	Gets a list of all joyo kanji, plus their grade level from wikipedia
	For information on joyo kanji see: http://en.wikipedia.org/wiki/J%C5%8Dy%C5%8D_kanji
	"""

	joyo_kanji_url = "http://en.wikipedia.org/wiki/List_of_j%C5%8Dy%C5%8D_kanji"
	soup = BeautifulSoup(urlopen(joyo_kanji_url), 'html.parser')

	kanji = []
	# the kanji are in the 2nd column of this table
	for row in soup.findAll('table')[2].findAll('tr'):
		cells = row.findAll('td')
		if len(cells) > 0: # i.e., ignore the header
			if cells[1].a.contents:
				character = cells[1].a.contents[0]
				grade     = cells[5].contents[0]

			kanji.append(Kanji(character, grade))

	return kanji

# get all the joyo characters from wikipedia
joyo_kanji = get_kanji_from_wikipedia()

# write them as a csv file
f = open("kanji.csv", "w")
i = 0
for k in joyo_kanji:
	k.get_data_from_dictionary()
	print >> f, k.as_csv()
	i+=1
	if i > 10:
		break
