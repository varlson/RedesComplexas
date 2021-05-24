import matplotlib.pyplot as plt
from removalMethods import *
# from totalFlow import removalMethods_totalFlow
# from efficiency import removalMethods_effeciency

from metricExtractor import aindaPensar
#----------------------------- GRAPH BUILDER PASSING GRAPH, METRIC(S) AND LABEL(S)---------
def graphBuilder(g, removalTypes, metrics, network, folder, option=1):
    nodes = [x/float(g.vcount()) for x in range(1, g.vcount()+1)]
    plt.xlabel("nodes")
    
    removalTypes = [removalTypes] if not isinstance(removalTypes, list) else removalTypes
    metrics = [metrics] if not isinstance(metrics, list) else metrics

    for metric, removalType in zip(metrics, removalTypes):
    	R = sum(metric[1:])/len(metric)
    	R = str(R)[:5]
    	plt.plot(nodes, metric, label = removalType+' '+R)
    
    plt.title("Rede de "+network)
    # plt.title("Rede de Passageiros de "+network[3:])
    plt.xlabel(r'$f$', fontsize=14)
    if option == 1:
        plt.ylabel(r'$P_\infty(f) / P_\infty(0)$', fontsize=14)
    elif option ==2:
        plt.ylabel(r'$ \parallel W \parallel(f) / \parallel W \parallel(0)$', fontsize=16)
    else:
        plt.ylabel(r'$ E (f) / E (0)$', fontsize=16)
    plt.legend()
    plt.margins(x = 0.02, y = 0.02)
    # plt.set_aspect('equal')
    plt.savefig("GeneratedGraphs/"+folder+'/'+network+".png")
    plt.clf()


networks = ['pas2010', 'pas2005', 'pas2000', 'pas1995', 'pas1990', 'pas1985', 'pas1980', 'pas1975', 'pas1972']
def _main():
    for net in networks[:2]:
        g = main(net)
        # lsts = removalMethods_totalFlow(g)
        # graphBuilder(g, lsts[1], lsts[0], net, 'GianComponents', 2)
        lsts = aindaPensar(g)
        graphBuilder(g, lsts[1], lsts[0], net, 'GiantComponents')
        
        lsts = aindaPensar(g, 2)
        graphBuilder(g, lsts[1], lsts[0], net, 'TotalFlow', 2)

        lsts = aindaPensar(g,3)
        graphBuilder(g, lsts[1], lsts[0], net, 'Efficiency', 3)
    
