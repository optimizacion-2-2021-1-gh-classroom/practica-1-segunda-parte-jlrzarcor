import numpy as np


class LogisticRegression:

    def __init__(self, lr=0.1, iterations=1000):
        self.lr = lr
        self.iterations = iterations

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def loss(y, z):
        def r_log(x):
            return 0 if x == 0 else np.log(x)

        tot = 0
        for j in y:
            tot += (y * r_log(z) - (1 - y) * r_log(1 - z)) + (-1 / y.shape[0])
            return tot

    def optimize(self, x, y, iterations, lr):
        """
        :param x:
        :param y:
        :param iterations:
        :param lr:
        :return:
        """
        self.weights = np.zeros(x.shape[1])
        self.bias = 0

        for j in range(iterations):
            z = self.sigmoid(np.dot(x, self.weights) + self.bias)

            d_weights = (1 / x.shape[0]) * (2 * np.dot(x.T, (z - y)))
            d_bias = (1 / x.shape[0]) * (2 * np.sum(z - y))

            self.weights -= lr * d_weights
            self.bias -= lr * d_bias

    def predict(self, x, threshold=0.5):
        """

        :param x:
        :param threshold:
        :return:
        """
        probabilities = self.sigmoid(np.dot(x, self.weights) + self.bias)
        return [1 if i > threshold else 0 for i in probabilities]
