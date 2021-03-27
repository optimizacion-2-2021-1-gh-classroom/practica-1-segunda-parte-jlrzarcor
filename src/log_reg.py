import numpy as np


class LogisticRegression:

    def __init__(self, lr=0.1, iterations=1000):
        self.lr = lr
        self.iterations = iterations


    def sigmoid(self, x):
        """

        :param x:
        :return:
        """

        sig = np.array(1 / (1 + np.exp(-x)), dtype = np.float128)
        return sig

    @staticmethod
    def loss(y, z):
        """

        :param y:
        :param z:
        :return:
        """
        def r_log(x):
            return 0 if x == 0 else np.log(x)

        tot = 0
        for j in y:
            tot += (y * r_log(z) - (1 - y) * r_log(1 - z)) * (-1 / y.shape[0])
            return tot

    # Definición de matriz simétrica


    def optimize(self, x, y):
        """
        :param x:
        :param y:
        :return:
        """
        self.weights = np.zeros(x.shape[1])
        self.bias = 0
        self.n_it = 0
        self.tol = 1

        #for j in range(self.iterations):
        while (self.n_it < self.iterations or self.tol < 10**-8):
            z = self.sigmoid(np.dot(x, self.weights) + self.bias)

            d_weights = (1 / x.shape[0]) * (2 * np.dot(x.T, (z - y)))
            d_bias = (1 / x.shape[0]) * (2 * np.sum(z - y))
            self.tol = d_weights
            self.weights -= self.lr * d_weights
            self.bias -= self.lr * d_bias
            self.n_it += 1


    def predict(self, x, threshold=0.5):
        """

        :param x: values for testing the model (e.g x.test)
        :param threshold:
        :return:
        """
        probabilities = self.sigmoid(np.dot(x, self.weights) + self.bias)
        return [1 if i > threshold else 0 for i in probabilities]

