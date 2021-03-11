##################################################################
#
# Author: Eoghan O'Connor
# Student I.D: 16110625
#
# Project: 		Neural Networks applied to wireless EEG signals
# File Name: 	SVM.py
#
# Description: 	This file trains the model.
#					
#				The SVM dataset is loaded from the folders
#				The this data is labelled. The same
#				is then done for the validation dataset.
#				These datasets are used to train the model.
#				The model is then saved to a local directory.
#		
#				
# Notes:		The following code is set for all 8
#				channels. As used for EEG signal.
#
#################################################################

from sklearn import svm
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
import os
import random
import time
import pickle

ACTIONS = ["left","none", "right"]

#8 channels of 50 Hz are flatten to on 1D.
reshape=(-1,400)
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
traindata = sort_data(starting_dir="svm_data")
train_X = []
train_y = []
for X, y in traindata:
    train_X.append(X)
    train_y.append(y)


#Sorting and lablling the validation dataset
print("creating validation data")
testdata = sort_data(starting_dir="svm_valid")
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


correct=0
#The SVM is default set to a hard margin C=1
clf=svm.SVC( kernel='linear')
clf.fit(train_X,train_y)
print("Trained")
z=clf.predict(test_X)

#Calculating the Accuracy of the SVM.
for i in range (len(test_X)):
	if z[i]==test_y[i]:
		correct+=1
accuracy=int((correct/len(test_X))*100)
print(f"Accuracy = {accuracy}% ")



#Saving the model to a file
filename='model_svm'
pickle.dump(clf,open(filename,'wb'))

