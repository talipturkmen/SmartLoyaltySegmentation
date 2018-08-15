import matplotlib.pyplot as plt2

def find_num_of_cluster(wcss):
    rangeNumber = 10
    variance = 0
    clusterNum = 0
    normValue = wcss[0] / rangeNumber
    for i in range(0, rangeNumber-1):
        variance = (wcss[i] - wcss[i + 1]) / normValue

        if variance < 1 :
            clusterNum = i + 1
            break
    return clusterNum