import tensorflow as tf
import numpy as np
import keras
from keras import layers
from keras import Sequential


def compute_linear(X,Y,num_itr):
    model = Sequential([
        layers.Dense(50,activation='relu'),
        layers.Dense(25,activation='relu'),
        layers.Dense(10,activation='relu'),
        layers.Dense(1,activation='linear')
    ])


    model.compile(loss=keras.losses.mean_squared_error)
    model.fit(X,Y,epochs=num_itr)
   
    return model




