import json
import matplotlib.pyplot as plt

class plotSite(object):
        
        def __init__(self):
                self.json= self.load()
        def load(self):
                with open('sites.json') as json_data:
                        d = json.load(json_data)
                        return d
                                        
if __name__ == "__main__":
        try:
                ##crs_wgs = proj.Proj(init='epsg:4326')
                ##crs_bng = proj.Proj(init='epsg:27700')
                p = plotSite()
                for i in p.json:
                        ##x, y = proj.transform(crs_wgs, crs_bng,i['Lon'], i['Lat'])
                        plt.scatter(i['Lon'], i['Lat'])
                plt.show()
        except IndexError:
                fmt = 'invalid file name'
                print(fmt.format(__file__.split('/')[-1]))