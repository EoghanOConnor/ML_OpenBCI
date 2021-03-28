Author: Eoghan O'Connor
Project Title: Machine learning applied to EEG signals.



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
