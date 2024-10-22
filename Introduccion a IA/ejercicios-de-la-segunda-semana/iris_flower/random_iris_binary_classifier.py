import random

class RandomIrisBinaryClassifier:

    def __init__(self, data):
        """Constructor of class. Argument data is a list of numeric tuples.
        The data list represents a labeled dataset for binary classification.
        Last element of each tuple is a binary value, the class (1 or 0).
        """
        self.__data = data
        self.__split_ratio = 0.7
        self.__epochs = 1 # one epoch by default
        self.__training_data = list()
        self.__testing_data = list()
        self.__confusion_matrix = { 'TP': 0, 'FP': 0, 'TN': 0, 'FN': 0}

    def set_split_ratio(self, ratio):
        self.__split_ratio = ratio

    def set_epochs(self, epochs):
        self.__epochs = epochs

    def split_dataset(self):
        """Splits dataset into training data and testing data.
        The ration __split_ratio is used for the splitting.
        Dataset must be shuffled before splitting. Resulting training data and
        testing data are stored in __training_data and __testing_data, respectively
        """
        data_clone = self.__data[::]
        random.shuffle(data_clone)
        n = len(data_clone)
        split = int(len(data_clone) * self.__split_ratio)
        self.__training_data = data_clone[:split]
        self.__testing_data = data_clone[split:]

    def fit(self):
        # does nothing. Prediction is random
        pass

    def predict(self, item):
        # does not analyze item. Just return random bit
        return random.randint(0, 1)

    def compute_confusion_matrix(self):
        """Computes number of false positives, false negatives, true positives and true negatives 
        in the testing data.
        Values are stored in self.__confusion_matrix and returned as a dictionary"""
        #TODO Implement this method
        TP = 0
        FP = 0
        TN = 0
        FN = 0
        for item in self.__testing_data:
            y = item[len(item)-1]
            y_hat = self.predict(item)
            if y == 1 and y_hat == 1:
                TP = TP + 1
            elif y == 0 and y_hat == 1:
                FP = FP + 1
            elif y == 1 and y_hat == 0:
                FN = FN + 1
            elif y == 0 and y_hat == 0:
                TN = TN + 1
        self.__confusion_matrix.update({'TP':TP})        
        self.__confusion_matrix.update({'FP':FP})        
        self.__confusion_matrix.update({'TN':TN})        
        self.__confusion_matrix.update({'FN':FN})        
        return self.__confusion_matrix

        

