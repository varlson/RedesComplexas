from networkGenerator import *
from removalMethods import calculator, randomRemovalgenerator

#----------------- TOTAL FLOW -----------------------------
def totalFlowRemovalFuncion(g, metric):
    TOTALFLOW = float(sum(g.es['weight']))
    removaList = np.zeros(g.vcount())
    removaList[0] = 1.0
    count = 1
    while g.vcount() > 1:
        maxId = metric.index(max(metric))
        g.delete_vertices(maxId)
        del metric[maxId]
        removaList[count] = float(sum(g.es['weight'])/TOTALFLOW)
        count+=1
    return removaList


def removalMethods_totalFlow(g):
    metricList = []
    N = g.vcount()
    metricNameList = []
    # remList = []

     # DEGREE
    degree_removal_list = totalFlowRemovalFuncion(g.copy(),g.degree())
    metricList.append(degree_removal_list)
    metricNameList.append("Degree")

     # BETWEENNESS WITHOUT WEIGHT
    betweenness_removal_list = totalFlowRemovalFuncion(g.copy(),g.betweenness())
    metricList.append(betweenness_removal_list)
    metricNameList.append("Betweenness")

    # BETWEENNESS WITH WEIGHT
    _weight = np.array(g.es['weight'])
    try:
        _weight = 1.0/_weight
    except :
        pass
    betweenness_removal_list = totalFlowRemovalFuncion(g.copy(),g.betweenness(weights = _weight))
    metricList.append(betweenness_removal_list)
    metricNameList.append("Betweenness with Weights")

    # STRENGTH WEIGHT
    strength_removal_list = totalFlowRemovalFuncion(g.copy(),g.strength(weights = g.es['weight']))
    metricList.append(strength_removal_list)
    metricNameList.append("Strength")
    
     # VULNERABILITY
    vulnerability_removal_list = totalFlowRemovalFuncion(g.copy(),calculator(g.copy()))
    metricList.append(vulnerability_removal_list)
    metricNameList.append("Vulnerability")
    
    # VULNERABILITY WITH WEIGHTS
    vulnerability_removal_list = totalFlowRemovalFuncion(g.copy(),calculator(g.copy(), True))
    metricList.append(vulnerability_removal_list)
    metricNameList.append("Vulnerability with Weights")
    
    # RANDOM REMOVAL
    random_removal_list = randomRemovalgenerator(g.copy(), 100)
    metricList.append(random_removal_list)
    metricNameList.append("Random")
    
    return [metricList, metricNameList]