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
			print(key)

	def searchKeys(self, json, searchVal):
		try:
<<<<<<< HEAD
			return json[searchVal]
		except IndexError:
			print("error")
=======
			keyword=str(raw_input('Search current values:'))
                        print keyword
			print json[keyword]
		except KeyError:
    			print "Not a valid key"
			self.searchKeys(p.json)
>>>>>>> 434136ff17a090cbcca925b43cd55eaef10bf84a

	def getStations(self, json):
		stations = self.searchKeys(json,'s')
		stations = [stations[i:i+4] for i in range(0, len(stations), 4)]
		return stations


if __name__ == "__main__":
	try:
<<<<<<< HEAD
		p = Parser()
		keyword = str(input('Search current values:'))
#		p.getKeys(p.json)
		data = p.searchKeys(p.json, keyword)
		print(data)
		stations = p.getStations(p.json)
		print(stations)
		keyword = str(input('Station Name: '))
		print(stations.index(keyword))
		print(data[stations.index(keyword)])
	except IndexError:
		fmt = 'invalid file name'
		print(fmt.format(__file__.split('/')[-1]))
=======
        	p = Parser()
		#p.getKeys(p.json)
		p.searchKeys(p.json)
    	except IndexError:
        	fmt = 'invalid file name'
        	print(fmt.format(__file__.split('/')[-1]))
>>>>>>> 434136ff17a090cbcca925b43cd55eaef10bf84a
