
##      Kentucky Mesonet Core Software -- CS 496 WKU
##
##      Scope: To develop a dynamic map to visualize different weather data
##
##      Contributers: Lucas Cook, Tyler Carrico, ChunHei Yuen



import json
import urllib.request
from Site import *
import numpy as np
from math import cos, asin, sqrt
from functools import reduce
import requests

class Parser(object):
	def __init__(self):
		self.url = "http://www.kymesonet.org/app.json"
		self.testPath = "/opt/lampp/htdocs/meso/python/KYMesonetCoreSoftware/app.json"
		self.json = self.load()
		self.keys = ["TAIR","RELH","PRCP","WSPD","WDIR","WSMX","SRAD","DWPT","WCHI", "Lon", "Lat"]
		self.psuedoPoints = [{'Lat': 36.217687, 'Lon': -90.065918},
                        {'Lat': 39.223742, 'Lon': -90.153809},
                        {'Lat': 39.223742, 'Lon': -90.153809},
                        {'Lat': 36.341678, 'Lon': -81.804199},
                        {'Lat': 36.004673, 'Lon': -85.297852},
                        {'Lat': 39.512517, 'Lon': -85.144043},
                        {'Lat': 39.257778, 'Lon': -81.540527}]

		self.nearest = self.getNeighbor()

	def load(self):
		return requests.get(self.url).json()

#		with open(self.testPath) as json_data:
#			d = json.load(json_data)
#		return d

	def get(self,data, convert=1):
		if data not in self.keys:
			print("NOT A VALID KEY")
		weatherData = []
		for i in range(0,len(self.json)):
			if(self.json[i][data] != None):
				weatherData.append(self.json[i][data])
		if(convert == 1):
			weatherData = self.convert(weatherData, data)
#		else:
			#print("Not Converting: " + str(data))

		return weatherData


	def RepairDownStations(self, data):

		lats= self.get('Lat',0)
		lons= self.get('Lon', 0)
		locs = []
		for i in range(0, len(data)):
			if data[i] == "NA":
				locs.append({'Lat': lats[i], 'Lon': lons[i], 'index': i})

		neighbors = self.getNeighbor(1, locs)

		for i in range(len(locs)):
			print(locs[i]['index'])
			print(neighbors[i]['index'])
			data[locs[i]['index']] = data[neighbors[i]['index']]

		return data

	def convert(self, data, dataType):
		data = self.RepairDownStations(data)

		print("in convert..{0}",dataType)
		data = np.array(data, dtype=np.float32)
 
		if dataType == 'TMAX' or dataType == 'TMIN' or dataType == 'TAIR' or dataType == 'DWPT':
			return np.add(32., np.multiply(data, 9./5.)).tolist()
		elif dataType == 'PRCP':
 			return np.multiply(data, 0.03937).tolist()
		elif dataType == 'WSPD' or dataType == 'PEAK':
			#MPH
			return np.multiply(data, 2.237).tolist()
		elif dataType == 'WCHI':
			TAIR_c = self.RepairDownStations(self.get('TAIR', 0))
			TAIR_c = np.array(TAIR_c, dtype=np.float32)
			TAIR_f = np.add(32., np.multiply(TAIR_c, 9./5.))
			WSPD_kph = self.RepairDownStations(self.get('WSPD', 0))
			WSPD_kph = np.multiply(np.array(WSPD_kph, dtype=np.float32), 3.6)
			temp_w = np.power(WSPD_kph, 0.16)
			temp_1 = np.multiply(TAIR_c, 0.6215)
			temp_2 = np.multiply(temp_w, 11.37)
			temp_3 = reduce(np.multiply, [temp_w, TAIR_c, 0.3965])
			temp = reduce(np.add, [temp_1, temp_2, temp_3, 13.12])

			# Where the tair is too high or the wspd is too low,
			# just take the tair value; else, actually use the
			# calculated values
			temp = np.where(TAIR_c > 10, TAIR_f, temp)
			WCHI_f = np.where(WSPD_kph < 5, TAIR_f, temp)
			return WCHI_f.tolist()
		return data.tolist()


	def neighborValue(self, dataType):

		values = []

		indexes = []
		for item in self.nearest:
			indexes.append(item['index'])

		data = self.get(dataType)

		for i in indexes:
			values.append(data[i])

		return values



	def getNeighbor(self, repair=0, indexes = 0):

		lons = self.get('Lon', 0)
		lats = self.get('Lat', 0)
		loc = []
		nearest = []

		for i in range(0, len(lons)):
			loc.append({'Lat': lats[i], 'Lon': lons[i], 'index': i})

		if repair == 1:
			for i in indexes:
				nearest.append(self.closest(loc, i))
				print(nearest)

			return nearest

		else:

			for i in self.psuedoPoints:
				nearest.append(self.closest(loc, i))


			return nearest

		return nearest

	def distance(self, lat1, lon1, lat2, lon2):
		p = 0.017453292519943295
		a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
		d = 12742 * asin(sqrt(a))
		if d == 0:
			return 1000
		else:
			return d

	def closest(self, data, v):
		return min(data, key=lambda p: self.distance(v['Lat'],v['Lon'],p['Lat'],p['Lon']))


##
##class Parser(object):
##
##	def __init__(self):
##		self.url = "http://www.kymesonet.org/current.json"
##		self.json,self.sites= self.load(0)
##
##	def load(self, refresh):
##		if refresh == 1:
##			with urllib.request.urlopen(self.url) as url:
##				data = json.loads(url.read().decode())
##			print("---UPDATE: Current weather JSON updated...---")
##			self.json = data
##		else:
##			with open('sites.json') as json_data:
##				sites = json.load(json_data)
##			print("---UPDATE: Site Location Data Loaded...---")
##			with urllib.request.urlopen(self.url) as url:
##				data = json.loads(url.read().decode())
##			print("---UPDATE: Current weather data updated...---")
##			return data,sites
##
##	def convert(self, data, dataType):
##		convertedData = []
##		if dataType == 'TMAX' or dataType == 'TMIN' or dataType == 'WCHI':
##			for i in data:
##				convertedData.append(np.add(32., np.multiply(i, 9./5.)))
##			print("---CONVERTED: Celcius -> Fahrenheit---"),
##			print(convertedData)
##			return convertedData
##		return data
##				
##
##	def getData(self, json, searchVal):
##		try:
##			print("---UPDATE: {0} Data Fetched---".format(searchVal))
##			print(json[searchVal])
##			return json[searchVal]
##		except KeyError:
##			print ('Not a valid searchVal')
##			return False
##
##	def getSiteNames(self, json):
##		sites = self.getData(json,'s')
##		sites = [sites[i:i+4] for i in range(0, len(sites), 4)]
##		print("---UPDATE: Parsing Sites---")
##		print(sites)
##		return sites
##
##	def assembleSiteObjs(self):
##		count = 0
##		siteObjs = []
##		siteNames = self.getSiteNames(self.json)
##		for site in self.sites:
##			s = Site(site['Lon'], site['Lat'])
##			siteObjs.append(s)
##			count = count + 1
##		print("---UPDATE: Site Objects Created...---")
##		return siteObjs
