##      Kentucky Mesonet Core Software -- CS 496 WKU
##
##      Scope: To develop a dynamic map to visualize different weather data
##
##      Contributers: Lucas Cook, Tyler Carrico, ChunHei Yuen



import json
import urllib.request
from Site import *

class Parser(object):

	def __init__(self):
		self.url = "http://www.kymesonet.org/current.json"
		self.json,self.sites= self.load(0)

	def load(self, refresh):
		if refresh == 1:
			with urllib.request.urlopen(self.url) as url:
				data = json.loads(url.read().decode())
			print("---UPDATE: Current weather JSON updated...---")
			self.json = data
		else:
			with open('sites.json') as json_data:
				sites = json.load(json_data)
			print("---UPDATE: Site Location Data Loaded...---")
			with urllib.request.urlopen(self.url) as url:
				data = json.loads(url.read().decode())
			print("---UPDATE: Current weather data updated...---")
			return data,sites

	def getData(self, json, searchVal):
		try:
			print("---UPDATE: {0} Data Fetched---".format(searchVal))
			print(json[searchVal])
			return json[searchVal]
		except KeyError:
			print ('Not a valid searchVal')
			return False

	def getSiteNames(self, json):
		sites = self.getData(json,'s')
		sites = [sites[i:i+4] for i in range(0, len(sites), 4)]
		print("---UPDATE: Parsing Sites---")
		print(sites)
		return sites

	def assembleSiteObjs(self):
		count = 0
		siteObjs = []
		siteNames = self.getSiteNames(self.json)
		for site in self.sites:
			s = Site(site['Lon'], site['Lat'])
			siteObjs.append(s)
			count = count + 1
		print("---UPDATE: Site Objects Created...---")
		return siteObjs
