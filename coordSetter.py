from graphBuilder import *
import numpy as np
def coord_setter(g, attr):
    coord = np.genfromtxt('csvFiles/cities_coord.csv', delimiter=",")
    lst = coord.transpose()
    for i in range(g.vcount()):
        try:
            idx = list(lst[0]).index(g.vs[i][attr])
        except:
            print(g.vs[i]['id'])
            pass
        # idx = list(lst[0]).index(g.vs[i]['id'])
        g.vs[i]['x'] = lst[1][idx]
        g.vs[i]['y'] = lst[2][idx] *(-1)

# g = Graph.Read_GraphML('Other/fluvial.GraphML')
g = Graph.Read_GraphML('Another/terrestrial.GraphML')
# temp(g, 'fluvial')
temp(g, 'terrestrial')
