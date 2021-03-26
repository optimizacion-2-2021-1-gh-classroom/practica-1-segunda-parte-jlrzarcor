import numpy as np
import os
import pandas as pd

class LogRegressionTools:

    def __init__(self, data):
        self.data = data
        pass


    def split(self, data, percent = 0.7, target = -1):
        """

        :param data:
        :param percent:
        :param target:
        :return:
        """
        cut = int(data.shape[0]*percent)
        train_set = data[0:cut,:]
        test_set = data[cut:-1,:]
        train_target = train_set[:,target]
        test_target = test_set[:,target]
        if target == -1:
            test_set = test_set[:,0:target-1]
            train_set = train_set[:,0:target-1]
        else:
            test_set = test_set[:,1:target]
            train_set = train_set[:, 1:target]
        return train_set, test_set, train_target, test_target

    def read_doc(self, data, delimiter = ','):
        """

        :param doc:
        :param delimiter:
        :return:
        """
        ext = os.path.splitext(data)[-1].lower()
        if ext == ".txt":
            dataset = np.loadtxt(data, delimiter = delimiter)
        else:
            dataset = np.genfromtxt(data, delimiter = delimiter)
        return dataset






