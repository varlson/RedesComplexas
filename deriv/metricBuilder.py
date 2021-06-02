from removalMethods import removalFunction, calculator, randomRemovalgenerator, np, effGlobal

#----------------- EFFICIENCY -----------------------------
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

#----------------- COMPONENTE GINGANTE -----------------------------

def giantComponent(g, metric):
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

def dinamicDriver(g, type=1):
    switcher = {
        1: giantComponent,
        2: efficiencyRemovalFuncion,
        3: totalFlowRemovalFuncion
    }

    metricList = []
    N =g.vcount()
    metricNameList = []
    dinamicFunction = lambda graph, met, typ: switcher.get(typ)(graph, met)

     # DEGREE
    degree_removal_list = dinamicFunction(g.copy(),g.degree(), type)
    metricList.append(degree_removal_list)
    metricNameList.append("Degree")

     # BETWEENNESS WITHOUT WEIGHT
    betweenness_removal_list = dinamicFunction(g.copy(),g.betweenness(), type)
    metricList.append(betweenness_removal_list)
    metricNameList.append("Betweenness")

        #BETWEENNESS WITH WEIGHT
    _weight = np.array(g.es['weight'])
    _weight = np.array([1.0/x if x != 0.0 else 0 for x in _weight])
    betweenness_removal_list = dinamicFunction(g.copy(),g.betweenness(weights = _weight),type)
    metricList.append(betweenness_removal_list)
    metricNameList.append("Betweenness with Weights")

    # STRENGTH WEIGHT
    strength_removal_list = dinamicFunction(g.copy(),g.strength(weights = g.es['weight']), type)
    metricList.append(strength_removal_list)
    metricNameList.append("Strength")

     # VULNERABILITY
    vulnerability_removal_list = dinamicFunction(g.copy(),calculator(g.copy()), type)
    metricList.append(vulnerability_removal_list)
    metricNameList.append("Vulnerability")
    
    # VULNERABILITY WITH WEIGHTS
    vulnerability_removal_list = dinamicFunction(g.copy(),calculator(g.copy(), True), type)
    metricList.append(vulnerability_removal_list)
    metricNameList.append("Vulnerability with Weights")
    
    # RANDOM REMOVAL
    random_removal_list = randomRemovalgenerator(g.copy(), 100)
    metricList.append(random_removal_list)
    metricNameList.append("Random")
    return [metricList, metricNameList]
