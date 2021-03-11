##################################################################
#
# Author: Eoghan O'Connor
# Student I.D: 16110625
#
# Project: 		Neural Networks applied to wireless EEG signals
# File Name: 	Model.py
#
# Description: 	This file trains the model.
#					
#				The training data is loaded from the folders
#				The this data is one-hot encoded. The same
#				is then done for the validation dataset.
#				These datasets are used to train the model.
#				The model is then saved to a local directory.
#		
#				
# Notes:		The following code is set for all 8
#				channels. As used for EEG signal.
#
#################################################################				

#libaries
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv1D, BatchNormalization,Dropout
import os
import random
import time



ACTIONS = ["left","none", "right"]
reshape=(-1,8,50)

print("training...")

#Function that sorts data into 1 array
#The function also labels the different actions
def sort_data(starting_dir="test_delete"):
    
    #creating an array with 3 arrays
    training_data = {}
    for action in ACTIONS:
        if action not in training_data:
            training_data[action] = []

         #loading in data
        data_dir = os.path.join(starting_dir,action)
        for item in os.listdir(data_dir):

            data = np.load(os.path.join(data_dir, item))
            for item in data:
                training_data[action].append(item)
    lengths = [len(training_data[action]) for action in ACTIONS]

    # One-hot encoding each datapoint according to their action.
    combined_data = []
    for action in ACTIONS:
        for data in training_data[action]:

            if action == "left":
                combined_data.append([data, [1, 0, 0]])

            elif action == "right":
                combined_data.append([data, [0, 0, 1]])

            elif action == "none":
                    combined_data.append([data, [0, 1, 0]])


    print("length:",len(combined_data))
    return combined_data


#Sorting and lablling the training dataset
print("creating training data")
traindata = sort_data(starting_dir="data")
train_X = []
train_y = []
for X, y in traindata:
    train_X.append(X)
    train_y.append(y)


#Sorting and lablling the validation dataset
print("creating validation data")
testdata = sort_data(starting_dir="valid")
test_X = []
test_y = []
for X, y in testdata:
    test_X.append(X)
    test_y.append(y)


#Reshaping the data to fit model
train_y = np.array(train_y)
test_y = np.array(test_y)
train_X = np.array(train_X).reshape(reshape)
test_X = np.array(test_X).reshape(reshape)

#Creating the model using conv1D.
model = Sequential()

model.add(Conv1D(30, (8), input_shape=train_X.shape[1:]))
model.add(Activation('relu'))

model.add(Flatten())
model.add(Dense(15))

model.add(Dense(3))
model.add(Activation('softmax'))


model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

batch_size = 30
#Fitting the model to the datasets
model.fit(train_X,
            train_y,
            batch_size=batch_size,
            epochs=2,
            validation_data=(test_X, test_y))

#Saving the model to a file
MODEL_NAME = "Model_"
model.save(MODEL_NAME)
print("Model saved")
