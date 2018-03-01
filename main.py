import json
from Parser import *
from Map import *

if __name__ == "__main__":
        try:
                p = Parser()
                weather = p.getData(p.json, 'TC03')
                print(weather)
                sites = p.assembleSiteObjs()
        except IndexError:
                fmt = 'invalid file name'
                print(fmt.format(__file__.split('/')[-1]))
