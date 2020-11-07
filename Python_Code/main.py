import serial
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation
import keyboard

def main():
    port = 'COM3'#COM Port
    baudrate = 9600 # Baudrate
    s = serial.Serial(port, baudrate)
    data = []
    values = []
    filepath = (r"local pathway")
    matrix = []
    sensors = 6  # number of sensors
    while True:
        x = 0
        array = []
        matrix = []

        if keyboard.is_pressed("a"):
            for x in range(sensors):
                read = s.readline().decode()
                single = read.rstrip()
                value = float(single)
                array.append(value)
                x += 1
            if x == sensors:
                matrix.append(array)
                array= []
        df = pd.DataFrame(matrix, columns=['Microphone1', 'X_Axis', 'Y_Axis', 'Z_Axis', 'Microphone2', 'Button'])
        df.to_csv(filepath, header=True, mode="a")



if __name__ == '__main__':
    main()
