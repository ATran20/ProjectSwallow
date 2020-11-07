# ProjectSwallow
Code to allow for communication of multiple devices and the post processing of acquired data.

# Required libraries
## Arduino
1)MPU2950 Bolder Flight Systems https://github.com/bolderflight/MPU9250
## Python
1) SciKit Learn
2) PySerial
3) Numpy
4) Pandas

# Adruino code
Used to poll for all sensor data, depending on the sensor that is presented to the Arduino MKR Zero.

# Python code
## main.py 
Used to read from serial and log it to a csv
## plot.py
Used to live plot the inputs into the csv file
