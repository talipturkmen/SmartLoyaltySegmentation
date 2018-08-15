from scipy import stats
def normalize(X):
    X= stats.zscore(X)
    return X
