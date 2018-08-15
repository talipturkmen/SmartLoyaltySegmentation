import matplotlib.pyplot as plt
def plot_results(X,y_kmeans,kmeans, n_cluster):

    # Make loop
    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green')
    plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=100, c='black')
    plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=100, c='cyan')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow')
    plt.legend()
    plt.show()