# from networkGenerator import *
from igraph import *
from random import random as rand
import numpy as np

#-------------------------- VULNERABILITY LIST GENERATOR ------------------------
def effGlobal(g, weighted=False): # global efficiency calculator

    eff= 0.0
    temp = []
    N = float(g.vcount())
    if weighted:
        _weight = np.array(g.es['weight'])
        _weight = np.array([1.0/x if x != 0.0 else 0 for x in _weight])
        for l in g.shortest_paths_dijkstra(weights = _weight):
            for ll in l:
                if(ll != 0):
                    eff+= (1.0/ll)
    else:
        for l in g.shortest_paths_dijkstra():
            for ll in l:
                if(ll != 0):
                    eff+= (1.0/ll)
    E = 0
    try:
        E = eff/(N*(N-1.0))
    except:
        pass
    return E

def calculator(g, weighted = False): # vulnerability calculator
    allEff = []
    eGlobal = effGlobal(g, weighted)
    for k in range(g.vcount()):
        g_copy = g.copy()
        list_of_ids = []

        for vertex_id in range(g_copy.vcount()):
            try:
                list_of_ids.append(g_copy.get_eid(k, vertex_id))
            except:
                pass
        g_copy.delete_edges(list_of_ids)
        aux = (eGlobal - effGlobal(g_copy,weighted))/eGlobal
        allEff.append(aux)

    _max = max(allEff)
    node_size = np.array(allEff)
    _min = min(allEff)

    node_size = 7+ ((node_size - _min) * (45 - 7))/(_max - _min)
    g.vs['size'] = node_size
    index = allEff.index(_max)
    return allEff

#----------------- COMPONENTE GINGANTE -----------------------------
#----------------- REMOVAL LIST  GENERATOR BY METRICS -----------------------------

def removalFunction(g, metric):
    N = g.vcount()
    removaList = np.zeros(N)
    removaList[0] = 1.0
    count=1
    while g.vcount() > 1:
        _max = max(metric)
        index = metric.index(_max)
        g.delete_vertices(index)
        del metric[index]
        clusters = g.components()
        removaList[count] =  max(clusters.sizes())/N
        count+=1
    return removaList


#---------- RANDOM REMOVAL LIST GENERATOR-----------------------


def randomRemovalgenerator(g, simulation):

    N = g.vcount()
    removaList = np.zeros(N)

    for i in range(simulation):
        gcopy = g.copy()
        removaList[0] += 1.0
        count=1
        while gcopy.vcount() > 1:
            index = rand() * gcopy.vcount()
            index = int(index)
            gcopy.delete_vertices(index)
            clusters = gcopy.components()
            if len(clusters) > 0:
                removaList[count] += max(clusters.sizes())/float(N)
                # print(clusters.sizes())
            else:
                removaList[count] += 0.0
            count = count+1 
    removaList = removaList/simulation
    return removaList


def removal_methods_main(g):
    metricList = []
    N =g.vcount()
    metricNameList = []
    # remList = []

     # DEGREE
    degree_removal_list = removalFunction(g.copy(),g.degree())
    metricList.append(degree_removal_list)
    metricNameList.append("Degree")

     # BETWEENNESS WITHOUT WEIGHT
    betweenness_removal_list = removalFunction(g.copy(),g.betweenness())
    metricList.append(betweenness_removal_list)
    metricNameList.append("Betweenness")

        # BETWEENNESS WITH WEIGHT
    _weight = np.array(g.es['weight'])
    _weight = np.array([1.0/x if x != 0.0 else 0 for x in _weight])
    betweenness_removal_list = removalFunction(g.copy(),g.betweenness(weights = _weight))
    metricList.append(betweenness_removal_list)
    metricNameList.append("Betweenness with Weights")

    # STRENGTH WEIGHT
    strength_removal_list = removalFunction(g.copy(),g.strength(weights = g.es['weight']))
    metricList.append(strength_removal_list)
    metricNameList.append("Strength")

     # VULNERABILITY
    vulnerability_removal_list = removalFunction(g.copy(),calculator(g.copy()))
    metricList.append(vulnerability_removal_list)
    metricNameList.append("Vulnerability")
    
    # VULNERABILITY WITH WEIGHTS
    vulnerability_removal_list = removalFunction(g.copy(),calculator(g.copy(), True))
    metricList.append(vulnerability_removal_list)
    metricNameList.append("Vulnerability with Weights")
    
    # RANDOM REMOVAL
    random_removal_list = randomRemovalgenerator(g.copy(), 100)
    metricList.append(random_removal_list)
    metricNameList.append("Random")
    return [metricList, metricNameList]
