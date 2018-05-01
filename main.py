##      Kentucky Mesonet Core Software -- CS 496 WKU
##
##      Scope: To develop a dynamic map to visualize different weather data
##
##      Contributers: Lucas Cook, Tyler Carrico, ChunHei Yuen
import json
from Parser import *
from Map import *
from BaseMap import *
from sys import argv
import time
from copy import deepcopy

def main():
    #try:
	starttime=time.time()
	#dataType = argv[1]
	basemap = BaseMap()


	#Start Time loop here
	p = Parser()
	#map = Map(p)
	for i in p.keys:
		if i == 'Lon' or i == 'Lat' or i == 'WDIR':
			continue
		else:
			map = Map(p)
			map.baseMap = basemap.base
			map.dataType = i
			map.setupColorMap()
			map.plotData()

			overlayer = Overlayer("images/mask.png")
			overlayer.save("images/"+str(i)+".png","images/"+str(i)+".png")
			if i == 'WSPD' or i =='WSMX':
				basemap = BaseMap()


##    except:
##        print("Unknown Error")

if __name__ == "__main__":
	main()


