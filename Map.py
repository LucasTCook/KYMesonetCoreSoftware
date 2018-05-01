##      Kentucky Mesonet Core Software -- CS 496 WKU
##
##      Scope: To develop a dynamic map to visualize different weather data
##
##      Contributers: Lucas Cook, Tyler Carrico, ChunHei Yuen



from Site import *
from colorMaps import *
from Overlayer import *
from math import pi
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.mlab as mlab

class Map(object):

	def __init__(self, db):
		self.dataType = None
		self.db = db
		self.cmap = None
		self.vmin = None
		self.vmax = None
		self.baseMap = None
		print("---UPDATE: Map object created with current data---")

	def plotData(self):
		lons = self.db.get('Lon', 0)
		lats = self.db.get('Lat', 0)

		for item in self.db.psuedoPoints:
			lons.append(item['Lon'])
			lats.append(item['Lat'])

		values = self.db.get(self.dataType)
		nearest = self.db.neighborValue(self.dataType)
		for item in nearest:
			values.append(item)

		x, y = self.baseMap(lons, lats)
		x_min, x_max = min(x), max(x)
		y_min, y_max = min(y), max(y)
		xi = np.linspace(x_min, x_max, 1000) # xi
		yi = np.linspace(y_min, y_max, 1000) # yi
		xi, yi = np.meshgrid(xi, yi) # convert vectors to grids
		valsi = mlab.griddata(x, y, values, xi, yi) # zi
		norm = cm.colors.Normalize(vmax=self.vmax, vmin=self.vmin)
		self.baseMap.contour(xi, yi, valsi, 100, cmap=self.cmap, norm=norm, zorder=0)
		self.baseMap.contourf(xi, yi, valsi, 100, cmap=self.cmap, norm=norm, zorder=0)

		print(self.dataType)
		if self.dataType == 'WSPD':
			print("In barbs..")
			lons = self.db.get('Lon', 0)
			lats = self.db.get('Lat', 0)
			lons = np.array(lons, dtype=np.float32)
			lats = np.array(lats, dtype=np.float32)

			barbs_grid_size=30
			WDIR = self.db.get('WDIR', 0)
			self.db.RepairDownStations(WDIR)
			data = np.array(WDIR, dtype=np.float32)
			# Interpolate the barbs same as above
			dirs = np.multiply(data, float(pi)/180) # to radians
			# spds = np.multiply(data[wind_speed], -0.86897624) # to negative knots
			#spds = np.multiply(13, -0.86897624) # NOTE fixed length
			uvec = np.multiply(-1., np.sin(dirs))
			vvec = np.multiply(-1., np.cos(dirs))

			uvec_proj, vvec_proj, barbs_x, barbs_y = self.baseMap.rotate_vector(uvec, vvec, lons, lats, returnxy=True)
			barbs_xi = np.linspace(barbs_x.min(), barbs_x.max(), barbs_grid_size)
			barbs_yi = np.linspace(barbs_y.min(), barbs_y.max(), barbs_grid_size)
			barbs_xi, barbs_yi = np.meshgrid(barbs_xi, barbs_yi)

			uvec_proj_i = mlab.griddata(barbs_x, barbs_y, uvec_proj, barbs_xi, barbs_yi)
			vvec_proj_i = mlab.griddata(barbs_x, barbs_y, vvec_proj, barbs_xi, barbs_yi)


			self.baseMap.quiver(barbs_xi, barbs_yi, uvec_proj_i, vvec_proj_i, zorder=1, width=0.001)


		plt.savefig("images/"+str(self.dataType)+".png", bbox_inches="tight", dpi=96)

		print("---UPDATE: Mapping Finished...---{0}", self.dataType)


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

	
	def setupColorMap(self):
		if self.dataType == "PRCP":
			self.cmap, self.vmin, self.vmax = precip_colormap()
		elif self.dataType == "DWPT":
			self.cmap, self.vmin, self.vmax  = dewpoint_colormap()
		elif self.dataType == "TAIR" or self.dataType == "WCHI" or self.dataType == "TMAX" or self.dataType == "TMIN":
			self.cmap, self.vmin, self.vmax  = temperature_colormap()
		elif self.dataType == "PEAK":
			self.cmap, self.vmin, self.vmax  = wind_colormap()
		elif self.dataType == "WSMX":
			self.cmap, self.vmin, self.vmax  = wind_colormap()
		elif self.dataType == "WSPD":
			self.cmap, self.vmin, self.vmax  = wind_colormap()
		elif self.dataType == "RELH":
			self.cmap, self.vmin, self.vmax  = humidity_colormap()
		elif self.dataType == "SRAD":
			self.cmap, self.vmin, self.vmax  = solar_colormap()
		elif self.dataType == "PMAS":
			self.cmap, self.vmin, self.vmax  = precipmass_colormap()
		elif self.dataType == "TC03" or self.dataType == "TC06" or self.dataType == "TC12" or self.dataType == "TC24" or self.dataType == "TC48" or self.dataType == "DC03" or self.dataType == "DC06" or self.dataType == "DC12" or self.dataType == "DC24" or self.dataType == "DC48":
			self.cmap, self.vmin, self.vmax  = tempchange_colormap()
		elif self.dataType == "TDDP":
			self.cmap, self.vmin, self.vmax  =  dewpointdepp_colormap()
		elif self.dataType == "BATV" or self.dataType == "MNBV":
			self.cmap, self.vmin, self.vmax  =  batv_colormap()
		elif self.dataType == "TTCT":
			self.cmap, self.vmin, self.vmax  =  ttct_colormap()
		elif self.dataType == "RADAR":
			self.create_map(radar=True, embellish=False, prefix_dir=pd)
		elif self.dataType == "BLANK":
			self.create_map(output_filename=dataType, prefix_dir=pd)
		elif self.dataType == "WHITE":
			self.create_map(output_filename=dataType, prefix_dir=pd, white=True, embellish=False)
		else:
			print("In else")
		print("---UPDATE: Color map selected...---")
