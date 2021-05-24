from graphBuilder import aindaPensar, graphBuilder
from igraph import *


g = Graph.Read_GraphML('Other/fluvial.GraphML')
lst = aindaPensar(g)
# graphBuilder(g, lst[1], lst[0], 'Fluvial', 'Terrestrial')

# lst = aindaPensar(g,3)
# graphBuilder(g, lst[1], lst[0], 'Fluvial-Total-Flow', 'Terrestrial')

# lst = aindaPensar(g,2)
# graphBuilder(g, lst[1], lst[0], 'Fluvial-Eff', 'Terrestrial')
