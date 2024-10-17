from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score
    
data, target = load_iris(return_X_y = True) # target has numeric values 0, 1, 2 for setosa, versicolor and virginica, resp.
postprocessed_target = target # TODO: Change this line to binary values versicolor vs the rest

train_data, test_data, train_target, test_target = train_test_split(data, postprocessed_target) 

model = Perceptron()
model.fit(train_data, train_target)

prediction = model.predict(test_data)

print ('Accuracy:', accuracy_score(test_target, prediction))
print ('Recall:', recall_score(test_target, prediction))
print ('Precision:', precision_score(test_target, prediction))
print ('\n clasification report:\n', classification_report(test_target, prediction))
print ('\n confussion matrix:\n',confusion_matrix(test_target, prediction))






