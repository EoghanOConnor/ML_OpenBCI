##################################################################
#
# Author: Eoghan O'Connor
# Student I.D: 16110625
#
# Project: 		Neural Networks applied to wireless EEG signals
# File Name: 	GUI.py
#
# Description:  This file displays the GUI that will indicate
#				the directions predicted.
#
#				Data is streamed in from the openBCI App.
#				800 samples of the signal are 
#				captured in total. Each sample is passed
#				through the model predict. The prediction
#				of the model is used to move the box in the GUI
#				according to the prediction.
#
# Notes:		The following code is set for all 8
#				channels. As used for EEG signal.
#
#################################################################	

#libraries
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import cv2
import os
import time
from pylsl import StreamInlet, resolve_stream
import tensorflow as tf


#Loading model from folder
model = tf.keras.models.load_model("./Model_files/EEG_model_1_50Hz_8Channels/")


# Uncomment to load sample dataset
datadir = "./data_files/EEG_test_sample_8Channels/test.npy"
test= np.load(datadir)

reshape = (-1,8,50)

#Max Frequency
Max_Hz= 50


#Uncomment to use live stream data
# # first resolve an EEG stream on the lab network
# print("looking for an EEG stream...")
# streams = resolve_stream('type', 'EEG')
# # create a new inlet to read from the stream
# inlet = StreamInlet(streams[0])


#parameters of GUI
WIDTH = 800
HEIGHT = 800
Box_size = 50
MOVE_SPEED = 1


# Initial box position
square = {'x1': int(int(WIDTH)/2-int(Box_size/2)), 
          'x2': int(int(WIDTH)/2+int(Box_size/2)),
          'y1': int(int(HEIGHT)/2-int(Box_size/2)),
          'y2': int(int(HEIGHT)/2+int(Box_size/2))}


#Gui dimensions 
gui = np.ones((square['y2']-square['y1'], square['x2']-square['x1'], 3)) * np.random.uniform(size=(3,))
#Lines for x and y axis
horizontal_line = np.ones((HEIGHT, 10, 3)) * np.random.uniform(size=(3,))
vertical_line = np.ones((10, WIDTH, 3)) * np.random.uniform(size=(3,))

num=0

while(num<600):
	channel_data = []

	# uncomment for sampling dataset
	channel_data.append(test[num])


	# Sampling all 8 channels
	# Uncomment to use live stream
	# for i in range(8):
	# 	sample, timestamp = inlet.pull_sample()
	# 	channel_data.append(sample[:Max_Hz])

	network_input = np.array(channel_data).reshape(reshape)

	#Predicition of the model
	out = model.predict(network_input)

	#Selecting action predict	
	action_list={0:'left',1:'none',2:'right'}
	Action= action_list.get(np.argmax(out))
	choice=np.argmax(out)


	#Moving box based on prediction
	if Action=='left':
		print("left")
		if(square['x1']>0):
			square['x1'] -= MOVE_SPEED
			square['x2'] -= MOVE_SPEED

	elif Action =='none':
		print("None")
		square['x1'] += 0
		square['x2'] += 0

	elif Action =='right':
		print("right")
		if(square['x2'] < 800):
			square['x1'] += MOVE_SPEED
			square['x2'] += MOVE_SPEED

	else:
		print("No Prediction made")

	#Updating the box position
	GUI_shape = np.zeros((WIDTH, HEIGHT, 3))
	GUI_shape[:,HEIGHT//2-5:HEIGHT//2+5,:] = horizontal_line
	GUI_shape[WIDTH//2-5:WIDTH//2+5,:,:] = vertical_line
	GUI_shape[square['y1']:square['y2'], square['x1']:square['x2']] = gui

	# Displaying the new GUI
	cv2.imshow('EEG controlled GUI', GUI_shape)
	cv2.waitKey(1)
	
	# iterator
	num+=1

print("Finished")