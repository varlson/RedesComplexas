from graphBuilder import aindaPensar, graphBuilder, outputFolderBuilder
from igraph import *


g = Graph.Read_GraphML('Other/terrestrial.GraphML')
lst = aindaPensar(g)

outputFolderBuilder('Terrestrial')
graphBuilder(g, lst[1], lst[0], 'GiFluvial', 'Terrestrial')

lst = aindaPensar(g,3)
graphBuilder(g, lst[1], lst[0], 'FlTotal-Flow', 'Terrestrial')

lst = aindaPensar(g,2)
graphBuilder(g, lst[1], lst[0], 'FluEff', 'Terrestrial')
