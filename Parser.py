import json

class Parser(object):

	def __init__(self):
		self.json= self.load()


	def load(self):
		with open('current.json') as json_data:
    			d = json.load(json_data)
    			#print(d)

		return d

	def getKeys(self, json):
		keys = json.keys()
		keys.sort()
		for key in keys:
			print key

	def searchKeys(self, json):

		try:
			keyword=str(raw_input('Search current values:'))
                        print keyword
			print json[keyword]
		except KeyError:
    			print "Not a valid key"



if __name__ == '__main__':
	try:
        	p = Parser()
		p.getKeys(p.json)
		p.searchKeys(p.json)
    	except IndexError:
        	fmt = 'invalid file name'
        	print(fmt.format(__file__.split('/')[-1]))
