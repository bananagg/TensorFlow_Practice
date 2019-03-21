import numpy as np

def zero_pad(X, seq_len):
    return np.array([x[: seq_len-1] + [0] * max(seq_len - len(x), 1) for x in X])

def get_vocabulary_size(X):
    return max([max(x) for x in X]) + 1

def fit_in_vocabulary(X, voc_size):
    return [[w for w in x if w < voc_size] for x in X]

def batch_generator(X, y, batch_size):
    size = X.shape[0]
    X_copy = X.copy()
    y_copy = y.copy()
    indeces = np.arange(size)
    print(indeces)
    np.random.shuffle(indeces)
    print(indeces)
    X_copy = X_copy[indeces]
    y_copy = y_copy[indeces]
    print(X_copy)
    print(y_copy)
    i = 0
    while True:
        if i + batch_size <= size:
            yield X_copy[i: i + batch_size], y_copy[i: i + batch_size]
            i += batch_size
        else:
            i = 0
            indeces = np.arange(size)
            np.random.shuffle(indeces)
            X_copy = X_copy[indeces]
            y_copy = y_copy[indeces]
            continue


# if __name__ == '__main__':
#
#     # Test batch generator
#     gen = batch_generator(np.array(['a', 'b', 'c', 'd']), np.array([1, 2, 3, 4]), 2)
#     for _ in range(8):
#         xx, yy = next(gen)
#         print(xx, yy)
#     pass
