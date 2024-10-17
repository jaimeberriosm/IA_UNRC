from sklearn.datasets import fetch_openml
from matplotlib import pyplot as plt
import numpy as np

mnist = fetch_openml('mnist_784')

print(mnist.data)
print(mnist.target)

rows = 3
cols = 4

images = mnist.data.to_numpy()[:rows * cols]
for i in range(rows * cols):
    plt.subplot(rows, cols, i+1)
    plt.imshow(images[i].reshape(28,28), cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()



