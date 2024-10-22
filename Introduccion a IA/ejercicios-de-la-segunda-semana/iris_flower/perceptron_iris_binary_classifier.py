import random

class PerceptronIrisBinaryClassifier:

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
        self.__weights = list()
        self.__bias = 0
        self.__learning_rate = 0.01
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
        """Trains the perceptron with the training data, the number of set epochs
        """
        self.__bias = random.uniform(0, 1)
        data_item_length = len(self.__training_data[0])
        for i in range(0, data_item_length-1):
            self.__weights.append(random.uniform(0, 1))
        for i in range(0, self.__epochs):
            for item in self.__training_data:
                y_hat = self.predict(item)
                y = item[len(item) - 1]
                for j in range(0, len(self.__weights)):
                    #TODO update weights based on delta weight formula, replacing line below
                    self.__weights[j] = self.__weights[j] + 0
                self.__bias = self.__bias + self.__learning_rate * (y - y_hat)

    def predict(self, item):
        """Apply perceptron to predict class for item
        """
        #TODO Implement this method
        pass # remove when implementation ready

    def compute_confusion_matrix(self):
        """Computes number of false positives, false negatives, true positives and true negatives 
        in the testing data.
        Values are stored in self.__confusion_matrix and returned as a dictionary"""
        #TODO Implement this method
        pass # remove when implementation ready

        

