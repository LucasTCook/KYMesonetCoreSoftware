##      Kentucky Mesonet Core Software -- CS 496 WKU
##
##      Scope: To develop a dynamic map to visualize different weather data
##
##      Contributers: Lucas Cook, Tyler Carrico, ChunHei Yuen



import json
from Parser import *
from Map import *
from sys import argv
import time

def main():
	try:
		starttime=time.time()
		dataType = argv[1]
		p = Parser()
		sites = p.assembleSiteObjs()
		while True:
			weather = p.convert(p.getData(p.json, dataType), dataType)
			map = Map(weather,sites)
			map.setupColorMap(dataType, None)
			map.setupBasemap()
			map.plotData()
			time.sleep(60.0 - ((time.time() - starttime) % 60.0))
			
		
	except IndexError:
		fmt = 'Enter valid weather data... (ex. python main.py "TC03")'
		print(fmt.format(__file__.split('/')[-1]))

if __name__ == "__main__":
	main()
	
