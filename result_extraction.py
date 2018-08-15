from utility import findNumOfCustomerInCluster , getSumOfColumn ,getNumberofCustomers ,getPropertyForEachCluster
def result_extraction(df,y_kmeans,n_cluster):

    customersInCluster = findNumOfCustomerInCluster(y_kmeans)
    totalMiles = getSumOfColumn(df,'SUM_OF_POINTS_LT')
    numberOfCustomer  = getNumberofCustomers(df);
    sumofActTypeForEachCluster =  getPropertyForEachCluster(df,'ACT_TYPE_CNT')
    sumofMilesForEachCluster =  getPropertyForEachCluster(df,'SUM_OF_POINTS_LT')
    sumofActType = getSumOfColumn(df ,'ACT_TYPE_CNT')
    averageServicePerCluster = [0] * n_cluster
    averageServiceOverall = sumofActType/numberOfCustomer
    milesPercentages = [0] * n_cluster
    customerPercentages =  [0] * n_cluster
    weights = [0] * n_cluster
    serviceIndexes = [0] * n_cluster
    averageServices = [0] * n_cluster
    for idx,row in enumerate(customersInCluster):
        # Miles percentage for each cluster
        try:
         print(repr(idx) + "Miles percentage "+ repr(sumofMilesForEachCluster[idx]*100/totalMiles))
         milesPercentages[idx] = sumofMilesForEachCluster[idx]*100/totalMiles
         # Customer Percentage
         print(repr(idx) + "Customer Percentage "+ repr(row*100 / numberOfCustomer))
         customerPercentages[idx] = row*100 / numberOfCustomer
         # Find Weiht mileagePerc/ customerPerc
         print(repr(idx) + "Weiht "+ repr((row *100/totalMiles)/(row*100 / numberOfCustomer)))
         weights[idx] = 10000*(row *100/totalMiles)/(row*100 / numberOfCustomer)
        except:
         continue;
    i = 0
    # Avg. Services per Cluster
    while i < n_cluster:
         averageServicePerCluster[i] = sumofActTypeForEachCluster[i]/customersInCluster[i]
         print("Services per Cluster" +repr(averageServicePerCluster[i]))
         averageServices[i] = averageServicePerCluster[i]
         i = i+1

    # Find Service Index
    for idx,row in enumerate(averageServicePerCluster):
        serviceIndexes[idx] = +row/averageServiceOverall
        print(repr(idx) + "Service Index "+repr(row/averageServiceOverall))
    return [milesPercentages,
            customerPercentages,
            weights,
            serviceIndexes,
            averageServices
            ]