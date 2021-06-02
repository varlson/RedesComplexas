from graphBuilder import *
from metricBuilder import dinamicDriver


def _main(g):
    outputFolderBuilder()
    
    weight = [x for x in range(1, g.ecount())]
    g.es['weight'] = weight
    print('Antes')
    lsts = dinamicDriver(g)
    graphBuilder(g, lsts[1], lsts[0], 'Nome1', 'GiantComponents')
    
    print('depois')

    lsts = dinamicDriver(g, 2)
    graphBuilder(g, lsts[1], lsts[0], 'Nome2', 'TotalFlow', 2)

    lsts = dinamicDriver(g,3)
    graphBuilder(g, lsts[1], lsts[0], 'Nome3', 'Efficiency', 3)


g = Graph.GRG(30, 0.4)
_main(g)