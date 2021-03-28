##################################################################
#
# Author: Eoghan O'Connor
# Student I.D: 16110625
#
# Project: 		Neural Networks applied to wireless EEG signals
# File Name: 	GUI_test.py
#
# Description:  This file creates a sample dataset to be
#				used in replacement of a live stream in
#				the GUI.py file.
#
#				Data is streamed in from the openBCI App.
#				A message is displayed to tell the user
#				to begin. 800 samples of the signal are 
#				taken and are stored in an array.
#				This array is then stored in a local directory.
#
# Notes:		The following code is set for all 8
#				channels. As used for EEG signal.
#
#################################################################	

#libraries
from pylsl import StreamInlet, resolve_stream
import numpy as np
import os
import random
import matplotlib.pyplot as plt
import ctypes   

#Max Frequency
Max_Hz = 50
channel_datas = []

#A button that needs to be pressed to start recording action
ctypes.windll.user32.MessageBoxW(0, f" Press OK when ready", 1)

	# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
	#I think this opens the 
streams = resolve_stream('type', 'EEG') 
	# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

#Capture 800 lines of the each channel
print("Processing...")

for i in range(800):
	channel_data = []
	#Iterate through all 8 channels
	for i in range(8): 
		sample, cur_time = inlet.pull_sample()
			#Record up to 50 hz of data
		channel_data.append(sample[:Max_Hz])

	channel_datas.append(channel_data) 

print(f"the length of ch datas is : {len(channel_datas)}")
					
channel_datas=np.array(channel_datas)
datadir = "./data_files/EEG_test_sample_8Channels/"

#creating folder for data
if not os.path.exists(datadir):
	os.mkdir(datadir)

print(f" datadir is  {datadir}")

#save sample
np.save(os.path.join(datadir,"test"),channel_datas)
print(f"Finished")