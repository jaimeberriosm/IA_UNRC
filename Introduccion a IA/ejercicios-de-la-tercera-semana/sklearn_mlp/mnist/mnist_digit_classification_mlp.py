from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.neural_network import MLPClassifier
from matplotlib import pyplot as plt
import numpy as np

mnist = fetch_openml('mnist_784')
X_train, X_test, y_train, y_test = train_test_split(mnist.data,mnist.target,test_size=0.3)

model = MLPClassifier()
model.fit(X_train, y_train)
prediction = model.predict(X_test)

#TODO Compute accuracy score on test data
print ('Accuracy:', accuracy_score(y_test, prediction))
#TODO Print out confussion matrix
print ('\n confussion matrix:\n',confusion_matrix(y_test, prediction))
