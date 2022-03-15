import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.layers import *
from keras.models import * 
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

TRAIN_PATH = "CovidDataset/Train"
VAL_PATH = "CovidDataset/Val"

# CNN Based Model in Keras

model = Sequential()
model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(224,224,3)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(128,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(64,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss=keras.losses.binary_crossentropy,optimizer='adam',metrics=['accuracy'])

model.summary()

# Train from scratch
train_datagen = ImageDataGenerator(
    rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
)

#TRAIN_PATH = "CovidDataset/Train"
#VAL_PATH = "CovidDataset/Val"

train_generator = train_datagen.flow_from_directory(
    directory=TRAIN_PATH,
    target_size = (224,224),
    batch_size = 32,
    class_mode = 'binary')

train_generator.class_indices

validation_datagen = ImageDataGenerator(rescale=1./255)
validation_generator = validation_datagen.flow_from_directory(
    directory=VAL_PATH,
    target_size = (224,224),
    batch_size = 32,
    class_mode = 'binary')

hist = model.fit(
    train_generator,
    epochs = 10,
    validation_data = validation_generator,
    validation_steps=2
)

# Class Activation Maps
# Grad-CAM

