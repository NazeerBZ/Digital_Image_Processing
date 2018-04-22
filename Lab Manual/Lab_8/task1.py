import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('digits.png',0)

dataset = []
for row in np.vsplit(img, 50):
# break image into 50 chunks vartically => so we can have 20 rows x 2000 cols
    for digit in np.hsplit(row, 100): 
# break each chunk into 100 chunks horizontally => so we have 20 rows x 20 cols
        dataset.append(digit)

dataset = np.array(dataset)
#convert to 3D dataset
dataset = dataset.reshape(50,100,20,20)

x_train = dataset[:,:50] # (50,50,20,20)
x_test = dataset[:,50:] # (50,50,20,20)
#convert to 2D dataset
x_train = x_train.reshape(2500,400).astype('float32')
x_test = x_test.reshape(2500,400).astype('float32')

# Create labels for x_train and x_test dataset
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]
test_labels = train_labels.copy()

# Initiate kNN, train the data, then test it with test data for k=1
knn = cv2.ml.KNearest_create()
knn.train(x_train, cv2.ml.ROW_SAMPLE, train_labels)
ret,result,neighbours,dist = knn.findNearest(x_test,k=5)
# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result==test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print(accuracy)





