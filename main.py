import pandas as pd
import numpy as np
from KMeansIMP import KMeansIMP
from utility import findNumOfCustomerInCluster, appendWithClusterID
from plot_results import plot_results
from result_extraction import result_extraction
from normalization import  normalize
from UI import createWindow,  openFileDialogBox, showResultsOnGrid

if __name__ == '__main__':

    #SELECT CSV DATA FROM FILE DIALOG BOX
    csvPath = "resources/data.csv"

    # DATA ACQUIRE
    df = pd.read_csv(csvPath,sep =";")
    df.fillna(0)
    # CREATE USER INTERFACE
    attr_1, attr_2 = createWindow(df.columns)

    print()
    # CREATE THE DATA FOR MODEL
    X = df.iloc[:, [df.columns.get_loc(attr_1), df.columns.get_loc(attr_2)]].values
    print("Data is ready")

    # Normalization
    X = normalize(X)
    print("Normalize finished")

    # MACHINE LEARNING MODELLING
    y_kmeans, kmeans, n_cluster = KMeansIMP(X)
    print("KMeans applied")

    # RESULT EXTRACTION#
    # arr contains number of FFP per cluster
    customerWithFFP = []
    arr = findNumOfCustomerInCluster(y_kmeans)

    # Adding Cluster ID to map with FFP_ID
    a = np.array(y_kmeans)[np.newaxis]
    df = appendWithClusterID(df, a.T)
    print("Cluster ID has been added to dataFrame")

    # Result Extraction
    attributeArray = result_extraction(df, y_kmeans,n_cluster)
    print("Result Extraction finished")

    showResultsOnGrid(n_cluster, attributeArray)

    print("Plotting")
    # PLOTTING RESULTS
    plot_results(X, y_kmeans, kmeans, n_cluster)


