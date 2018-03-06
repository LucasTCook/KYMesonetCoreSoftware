##      Kentucky Mesonet Core Software -- CS 496 WKU
##
##      Scope: To develop a dynamic map to visualize different weather data
##
##      Contributers: Lucas Cook, Tyler Carrico, ChunHei Yuen



import json
from Parser import *
from Map import *
from sys import argv

def main():
	try:
		dataType = argv[1]
		p = Parser()
		sites = p.assembleSiteObjs()
		weather = p.getData(p.json, dataType)
		map = Map(weather,sites)
		map.setupColorMap(dataType, None)
		map.setupBasemap()
		map.plotData()
		
	except IndexError:
		fmt = 'invalid file name'
		print(fmt.format(__file__.split('/')[-1]))

if __name__ == "__main__":
	main()
	
