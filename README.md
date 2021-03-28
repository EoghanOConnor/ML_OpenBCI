Author: Eoghan O'Connor

Project Title: Machine learning applied to EEG signals.


Video of finished project:

  https://user-images.githubusercontent.com/45408401/112758935-b104d280-8fe8-11eb-9536-1ca7491e41f2.mp4

Description of project:

  A user is able to use their thoughts to control a box inside a GUI application.
  They do this by thinking left,right and leave the mind blank to keep the box from moving.

How it works:

  A neural network is trained using the EEG signals emitted from the user brain when they think left,right and neither direction.
  The trained neural network is then applied to a live stream of incoming data.
  The signals are classified and move the box in the GUI accordingly.


Equipment used:
  Mark IV OpenBCI headset and Bluetooth dongle



The following libraries need to be installed:
  python 3
  pip install pylsl
  pip install matplotlib
  pip install numpy
  pip install scikit-learn
  pip install pickle-mixin
  pip install tensorflow
  pip install Keras


Note on Project files:
  To run the python source codes associated with
  this project. Download the datasets and model files.

To view a sample of EEG controlling the GUI:
  Once the data_files, model_files and python source codes
  have been downloaded.
  Run GUI.py. This will display a test sample of the GUI
  being controlled using a EEG model and EEG test sample.


To create a dataset:
  For this you will need the OpenBCI headset and OpenBCI app.
  Turn on the headset and connect it to the app.
  Then stream the dataset as an lsl outlet.
  Then run make_data.py.


To create a model:
  Currently the model.py is ready to make a model.
  Just run the model.py
  To make a different model, change the directly used in the sort_data
  entiries.
  Note: you may need to adjust the reshape size to fit the dataset correctly.


To create a test set:
  For this you will need the OpenBCI headset and OpenBCI app.
  Turn on the headset and connect it to the app.
  Then stream the dataset as an lsl outlet.
  Then run GUI_test.py.
