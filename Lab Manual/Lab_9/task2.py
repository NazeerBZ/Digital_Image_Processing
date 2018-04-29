import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import matplotlib.pyplot as plt
from keras import backend as K
K.set_image_dim_ordering('th') 

#Data augmentation takes the approach of generating more training data
#from existing training samples, by augmenting the samples via a number of random
#transformations. This helps model to generalize better
datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

imgs = ['cat.png', 'dog.png']
dataset = []

def perform_augmentation(img):
    sample = image.img_to_array(img)
    sub_dataset = sample.reshape((1,) + sample.shape)
    
    i = 0
    for batch in datagen.flow(sub_dataset, batch_size=1):
        plt.figure(i)    
        sub_dataset = np.concatenate((sub_dataset, batch))
        i += 1
        if i % 4 == 0:
            break
        
    return sub_dataset
    

for img in imgs:
    img = image.load_img(img, target_size=(150,150))
    sub_dataset = perform_augmentation(img)
    for sample in sub_dataset:
        dataset.append(sample)
       
dataset = np.array(dataset)

plt.imshow(image.array_to_img(dataset[7]))







