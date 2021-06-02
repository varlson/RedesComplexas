import matplotlib.pyplot as plt
from removalMethods import *



#----------------------------- GRAPH BUILDER PASSING GRAPH, METRIC(S) AND LABEL(S)---------
def graphBuilder(g, removalTypes, metrics, network, folder, option=1):
    print('Chegou')
    nodes = [x/float(g.vcount()) for x in range(1, g.vcount()+1)]
    plt.xlabel("nodes")
    
    removalTypes = [removalTypes] if not isinstance(removalTypes, list) else removalTypes
    metrics = [metrics] if not isinstance(metrics, list) else metrics

    for metric, removalType in zip(metrics, removalTypes):
        R = sum(metric[1:])/len(metric)
        R = str(R)[:5]
        plt.plot(nodes, metric, label = removalType+' '+R)
    
    plt.title("Rede de "+network)
   
    plt.xlabel(r'$f$', fontsize=14)
    if option == 1:
        plt.ylabel(r'$P_\infty(f) / P_\infty(0)$', fontsize=14)
    elif option ==2:
        plt.ylabel(r'$ \parallel W \parallel(f) / \parallel W \parallel(0)$', fontsize=16)
    else:
        plt.ylabel(r'$ E (f) / E (0)$', fontsize=16)
    plt.legend()
    plt.margins(x = 0.02, y = 0.02)
   
    plt.savefig("GeneratedGraphs/"+folder+'/'+network+".png")
    plt.clf()


    

def outputFolderBuilder(fold=None):
    from os import path, mkdir
    from shutil import rmtree
    if fold==None:
        output = ['GiantComponents','TotalFlow','Efficiency']
        for folder in output:
            if path.exists('./GeneratedGraphs/'+folder):
                rmtree('./GeneratedGraphs/'+folder)
            mkdir('./GeneratedGraphs/'+folder)
    else:
        if path.exists('./GeneratedGraphs/'+fold):
            rmtree('./GeneratedGraphs/'+fold)
        mkdir('./GeneratedGraphs/'+fold)