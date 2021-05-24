from networkGenerator import *
from removalMethods import calculator, randomRemovalgenerator, effGlobal

#----------------- TOTAL FLOW -----------------------------
def efficiencyRemovalFuncion(g, metric):
    removaList = np.zeros(g.vcount())
    removaList[0] = effGlobal(g)
    count = 1
    gp = g.copy()
    for node in range(gp.vcount()):
        maxId = metric.index(max(metric))
        gp.delete_vertices(maxId)
        del metric[maxId]
        removaList[node] = effGlobal(gp)
    return removaList


def removalMethods_effeciency(g):
    metricList = []
    N =max(g.components().sizes())
    metricNameList = []
    # remList = []

     # DEGREE
    degree_removal_list = efficiencyRemovalFuncion(g.copy(),g.degree())
    metricList.append(degree_removal_list)
    metricNameList.append("Degree")

     # BETWEENNESS WITHOUT WEIGHT
    betweenness_removal_list = efficiencyRemovalFuncion(g.copy(),g.betweenness())
    metricList.append(betweenness_removal_list)
    metricNameList.append("Betweenness")

    # BETWEENNESS WITH WEIGHT
    _weight = np.array(g.es['weight'])
    try:
        _weight = 1.0/_weight
    except :
        pass
    betweenness_removal_list = efficiencyRemovalFuncion(g.copy(),g.betweenness(weights = _weight))
    metricList.append(betweenness_removal_list)
    metricNameList.append("Betweenness with Weights")

    # STRENGTH WEIGHT
    strength_removal_list = efficiencyRemovalFuncion(g.copy(),g.strength(weights = g.es['weight']))
    metricList.append(strength_removal_list)
    metricNameList.append("Strength")
    
     # VULNERABILITY
    vulnerability_removal_list = efficiencyRemovalFuncion(g.copy(),calculator(g.copy()))
    metricList.append(vulnerability_removal_list)
    metricNameList.append("Vulnerability")
    
    # VULNERABILITY WITH WEIGHTS
    vulnerability_removal_list = efficiencyRemovalFuncion(g.copy(),calculator(g.copy(), True))
    metricList.append(vulnerability_removal_list)
    metricNameList.append("Vulnerability with Weights")
    
    # RANDOM REMOVAL
    random_removal_list = randomRemovalgenerator(g.copy(), 100)
    metricList.append(random_removal_list)
    metricNameList.append("Random")
    
    return [metricList, metricNameList]