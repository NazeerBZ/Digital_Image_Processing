from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.layers import Dense, Flatten
from keras.models import Sequential
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
from keras import backend as K
K.set_image_dim_ordering('th')

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
        sub_dataset = np.concatenate((sub_dataset, batch))
        i += 1
        if i % 99 == 0:
            break
        
    return sub_dataset
    

for img in imgs:
    img = image.load_img(img, target_size=(150,150))
    sub_dataset = perform_augmentation(img)
    for sample in sub_dataset:
        dataset.append(sample)
       
dataset = np.array(dataset)
dataset = dataset.reshape(2,100,3,150,150)
x_train = dataset[:,:50]
x_test = dataset[:,50:]

x_train = x_train.reshape(100,3,150,150).astype('float32')
x_test = x_test.reshape(100,3,150,150).astype('float32')

x_train = x_train / 255
x_test = x_test / 255

k = np.arange(2)
y_train = np.repeat(k,50)[:,np.newaxis]
y_test = y_train.copy()

VGG16_model = VGG16(weights='imagenet', include_top=False, input_shape=(3,150,150))

model = Sequential()
for layer in VGG16_model.layers:
    model.add(layer)

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, validation_split=0.10, epochs=10, batch_size=10)

scores = model.evaluate(x_test, y_test)
print('acc: %.2.f%%' % (scores[1]*100))
