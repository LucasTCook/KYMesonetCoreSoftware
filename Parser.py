import json
from Site import *

class Parser(object):

	def __init__(self):
		self.json,self.sites= self.load(0)

	def load(self, refresh):
		if refresh == 1: 
			with open('current.json') as json_data:
    				data = json.load(json_data)
			self.json = data
		else:
			with open('sites.json') as json_data:
				sites = json.load(json_data)
			with open('current.json') as json_data:
    				data = json.load(json_data)
			return data,sites

	def getData(self, json, searchVal):
		try:
			return json[searchVal]
		except KeyError:
			print ('Not a valid key')
			self.searchKeys(p.json)

	def getSites(self, json):
		sites = self.getData(json,'s')
		sites = [sites[i:i+4] for i in range(0, len(sites), 4)]
		return sites

	def assembleSiteObjs(self):
		count = 0
		siteObjs = []
		siteNames = self.getSites(self.json)
		for site in self.sites:
			s = Site(site['Lon'], site['Lat'])
			siteObjs.append(s)
		return siteObjs
