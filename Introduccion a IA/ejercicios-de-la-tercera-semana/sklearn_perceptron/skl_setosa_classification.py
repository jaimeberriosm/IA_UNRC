from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
    
data, target = load_iris(return_X_y = True) # target has numeric values 0, 1, 2 for setosa, versicolor and virginica, resp.
postprocessed_target = [0 if species == 2 else 1 for species in target] # leave zero as zero, all others to one

train_data, test_data, train_target, test_target = train_test_split(data, postprocessed_target) 

model = Perceptron()
model.fit(train_data, train_target)

score = model.score(test_data, test_target)

print(f'Accuracy: {score}')



