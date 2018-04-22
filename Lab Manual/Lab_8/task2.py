import numpy as np
from matplotlib import pyplot as plt
import cv2

data= np.loadtxt('letter-recognition.data', dtype= 'float32', delimiter = ',',
                    converters= {0: lambda ch: ord(ch)-ord('A')})

# split the data to two, 10000 each for train and test
trainSet, testSet = np.vsplit(data,2)
# split trainData and testData to features and responses
y_train, x_train = np.hsplit(trainSet,[1]) # break trainSet into 2 chunks from index 1
y_test, x_test = np.hsplit(testSet,[1]) # break testSet into 2 chunks from index 1

# Initiate the kNN, classify, measure accuracy.
knn = cv2.ml.KNearest_create()
knn.train(x_train, cv2.ml.ROW_SAMPLE, y_train)
ret, result, neighbours, dist = knn.findNearest(x_test, k=5)

correct = np.count_nonzero(result == y_test)
accuracy = correct*100.0/10000
print(accuracy)



