import os
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.neural_network import MLPClassifier


input_dir = '/home/jaime/Documentos/Python/IA_UNRC/IA_UNRC/Introduccion a IA/ejercicios-de-la-tercera-semana/sklearn_mlp/parking_lot/clf-data'
categories = ['empty', 'non_empty']

data = []
labels = []

for category in categories:
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (15, 15))
        data.append(img.flatten())
        #TODO add the corresponding label to labels
        if category=='empty':
            labels.append(0)
        else:
            labels.append(1)

data = np.asarray(data)
labels = np.asarray(labels)

#TODO split data intro training and testing sets
print(labels)
X_train, X_test, y_train, y_test = train_test_split( data, labels, test_size=0.3)


#TODO create an MLP classifier and train it on the training data
model = MLPClassifier()
model.fit(X_train, y_train)
prediction = model.predict(X_test)
#TODO measure performance, and print out confussion matrix

print ('Accuracy:', accuracy_score(y_test, prediction))
print ('\n confussion matrix:\n',confusion_matrix(y_test, prediction))