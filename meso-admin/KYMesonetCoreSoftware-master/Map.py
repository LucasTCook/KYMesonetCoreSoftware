##      Kentucky Mesonet Core Software -- CS 496 WKU
##
##      Scope: To develop a dynamic map to visualize different weather data
##
##      Contributers: Lucas Cook, Tyler Carrico, ChunHei Yuen



from Site import *
from colorMaps import *

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.mlab as mlab

class Map(object):
        
	def __init__(self,dataType, db):
		self.dataType = dataType
		self.db = db
		self.cmap = None
		self.vmin = None
		self.vmax = None
		self.baseMap = None
		print("---UPDATE: Map object created with current data---")

	def plotData(self):
		lons = self.db.get('Lon')
		lats = self.db.get('Lat')
		x, y = self.baseMap(lons, lats)
		x_min, x_max = min(x), max(x)
		y_min, y_max = min(y), max(y)
		xi = np.linspace(x_min, x_max, 1000) # xi
		yi = np.linspace(y_min, y_max, 1000) # yi
		xi, yi = np.meshgrid(xi, yi) # convert vectors to grids
		valsi = mlab.griddata(x, y, self.db.get(self.dataType), xi, yi, interp='linear') # zi
		norm = cm.colors.Normalize(vmax=self.vmax, vmin=self.vmin)
		self.baseMap.contour(xi, yi, valsi, 100, cmap=self.cmap, norm=norm, zorder=0)
		self.baseMap.contourf(xi, yi, valsi, 100, cmap=self.cmap, norm=norm, zorder=0)
		plt.savefig("test.png", bbox_inches="tight", dpi=96)
		print("---UPDATE: Mapping Finished...---")

	def setupBasemap(self):
		lat_min, lat_max, lon_min, lon_max = 34.47, 40.68, -89.5715, -81.7
		epsg = 3088
		plt.figure(figsize=(28., 28.), dpi=96)
		ax = plt.subplot(111)
		m = Basemap(epsg=epsg, resolution="i",llcrnrlat=lat_min, urcrnrlat=lat_max,llcrnrlon=lon_min, urcrnrlon=lon_max)
		bg = (1., 1., 1.)
		lw = 0.1
		m.drawcounties(zorder=2, linewidth=lw)
		m.drawstates(zorder=4, linewidth=lw)
		self.baseMap = m
		print("---UPDATE: Basemap Setup...---")

	
	def setupColorMap(self, dataType, pd):
		if dataType == "PRCP":
			self.cmap, self.vmin, self.vmax = precip_colormap()
		elif dataType == "DWPT":
			self.cmap, self.vmin, self.vmax  = dewpoint_colormap()
		elif dataType == "TAIR" or dataType == "WCHI" or dataType == "TMAX" or dataType == "TMIN":
			self.cmap, self.vmin, self.vmax  = temperature_colormap()
		elif dataType == "PEAK":
			self.cmap, self.vmin, self.vmax  = wind_colormap()
		elif dataType == "WSMX":
			self.cmap, self.vmin, self.vmax  = wind_colormap()
		elif dataType == "WSPD":
			self.cmap, self.vmin, self.vmax  = wind_colormap()
		elif dataType == "RELH":
			self.cmap, self.vmin, self.vmax  = humidity_colormap()
		elif dataType == "SRAD":
			self.cmap, self.vmin, self.vmax  = solar_colormap()
		elif dataType == "PMAS":
			self.cmap, self.vmin, self.vmax  = precipmass_colormap()
		elif dataType == "TC03" or dataType == "TC06" or dataType == "TC12" or dataType == "TC24" or dataType == "TC48" or dataType == "DC03" or dataType == "DC06" or dataType == "DC12" or dataType == "DC24" or dataType == "DC48":
			self.cmap, self.vmin, self.vmax  = tempchange_colormap()
		elif dataType == "TDDP":
			self.cmap, self.vmin, self.vmax  =  dewpointdepp_colormap()
		elif dataType == "BATV" or dataType == "MNBV":
			self.cmap, self.vmin, self.vmax  =  batv_colormap()
		elif dataType == "TTCT":
			self.cmap, self.vmin, self.vmax  =  ttct_colormap()
		elif dataType == "RADAR":
			self.create_map(radar=True, embellish=False, prefix_dir=pd)
		elif dataType == "BLANK":
			self.create_map(output_filename=dataType, prefix_dir=pd)
		elif dataType == "WHITE":
			self.create_map(output_filename=dataType, prefix_dir=pd, white=True, embellish=False)
		else:
			self.create_map(field=dataType, prefix_dir=pd)
		print("---UPDATE: Color map selected...---")
