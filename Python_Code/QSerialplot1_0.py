import serial
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation
from pynput.keyboard import Key, Listener


def main():
    port = 'COM3'
    baudrate = 9600
    s = serial.Serial(port, baudrate)
    data = []
    values = []
    filepath = (r"C:\Users\ngaij\Desktop\Project Swallow Software\Python\Accelerometer\Set1.csv") #chage this filepath
    matrix = []
    sensors = 6 # number of sensors
    while True:
        x = 0
        array = []
        matrix = []


        for x in range(sensors):
            read = s.readline().decode()
            single = read.rstrip()
            value = float(single)
            array.append(value)
            x += 1
        if x == sensors:
            matrix.append(array)

        df = pd.DataFrame(matrix, columns=['Microphone1','X_Axis', 'Y_Axis', 'Z_Axis', 'Microphone2','Button'])
        df.to_csv(filepath, header=True, mode="a")



if __name__ == '__main__':
    main()
