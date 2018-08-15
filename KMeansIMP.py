import matplotlib.pyplot as plt

def KMeansIMP(X):
    from sklearn.cluster import KMeans
    from elbow import find_num_of_cluster

    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i,init ='k-means++', max_iter = 300, n_init=10, random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 11), wcss)
    plt.show()

    #FIND ELBOWW HERE
    n_cluster = find_num_of_cluster(wcss)


    kmeans = KMeans(n_clusters=n_cluster, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)
    return y_kmeans, kmeans, n_cluster