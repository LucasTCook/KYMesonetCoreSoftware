import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class BaseMap(object):

	def __init__(self):
		self.base = self.setupBasemap();

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
		print("---UPDATE: Basemap Setup...---")
		return m

