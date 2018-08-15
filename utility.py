def findNumOfCustomerInCluster(y_kmeans):
    arr = [0]*10
    for r in y_kmeans:
        arr[r] = arr[r] + 1
    return arr

def appendWithClusterID(df, y_kmeans):
    df['clusterID'] = y_kmeans
    return df


def getPropertyForEachCluster(df,str):
    arr = [0] * 10
    for row in df.iterrows():
        arr[int(row[1]['clusterID'])] = arr[int(row[1]['clusterID'])] + row[1][str]
    return arr

def getSumOfColumn(df,str):
    return df.sum(axis=0)[str]

def getNumberofCustomers(df):
    return len(df);


def serviceIndex(df):
    #Average Service Per Cluster / Average of Diff Services
    return getSumOfColumn(df, 'ACT_TYPE_CNT') / getNumberofCustomers(df)



