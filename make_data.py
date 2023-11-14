##################################################################
#
# Author: Eoghan O'Connor
#
# Project: 		Neural Networks applied to wireless EEG signals
# File Name: 	Make_data.py
#
# Description:  This file creates the training and validation
#				datasets for the model.py file
#					
#				Data is streamed in from the openBCI App.
#				A message is displayed to tell the user
#				which command to act. 1000 samples  of
#				the signal are taken and are stored in
#				an array. After 1000 samples the array
#				is saved under the corresponding folder.
#				This is iterated 30 times for training 
#				dataset and 6 times for validation 
#				dataset.
#
# Notes:		The following code is set for all 8
#				channels. As used for EEG signal.
#
#################################################################				


#libraries
from pylsl import StreamInlet, resolve_stream
import numpy as np
import time
import os
import random
import matplotlib.pyplot as plt
import ctypes  


print("starting")

#Max Frequency
Max_Hz = 50

#Array of possible actions by participant
Actions=['left','none','right']


#30 iterations of the actions left,right and none
for i in range(30):

	#Iterating through each actions
	for ACTION in Actions:

		#A button that needs to be pressed to start recording action
		ctypes.windll.user32.MessageBoxW(0, f" Think {ACTION} ", "Action to take", 1)

		# first resolve an EEG stream on the lab network
		print("looking for an EEG stream...")

		streams = resolve_stream('type', 'EEG') 
		# create a new inlet to read from the stream
		inlet = StreamInlet(streams[0])
		channel_datas = []
			

		print("Processing...")
		#Capture 1000 lines of the each channel
		while (len(channel_datas)<1000):
			channel_data = []

			#Iterate through all 8 channels
			for i in range(8):
				sample, cur_time = inlet.pull_sample()
				#Record up to 50 hz of data
				channel_data.append(sample[:Max_Hz])
			#Add all samples to one array
			channel_datas.append(channel_data) 
					

		channel_datas=np.array(channel_datas)
		#creating folder for data
		datadir = "./data_files/EEG_Training_data_1_50Hz_8Channels"
		if not os.path.exists(datadir):
		    os.mkdir(datadir)

		#creating folder for action
		actiondir = f"{datadir}/{ACTION}"
		if not os.path.exists(actiondir):
		    os.mkdir(actiondir)

		#Saving action
		print(f"saving {ACTION} data...")
		np.save(os.path.join(actiondir, f"{int(time.time())}.npy"), channel_datas)
		print("done recording action")

	print("Finished")
