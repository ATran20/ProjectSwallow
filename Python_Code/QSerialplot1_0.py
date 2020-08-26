import serial
import numpy as np
import pandas as pd


def main():
    port = 'COM3'
    baudrate = 9600
    s = serial.Serial(port, baudrate)
    data = []
    values = []
    filepath = (r"C:\Users\ngaij\Desktop\Project Swallow Software\Python\Accelerometer\Set1")
    matrix = []

    while True:
        x = 0
        array = []
        matrix = []
        run = 0

        # data.append(value)
        #
        # matrix = np.r_[data]
        # print(matrix)

        # uni = pd.read_csv(filepath, encoding='utf-8')
        for x in range(4):
            read = s.readline().decode()
            single = read.rstrip()
            value = float(single)
            array.append(value)
            x += 1
        if x == 4:
            matrix.append(array)

        df = pd.DataFrame(matrix, columns=['X_Axis', 'Y-Axis', 'Z_Axis', 'Microphone'])
        df.to_csv(filepath, header=None, mode="a")

        #print(df)

if __name__ == '__main__':
    # space = input("Press Spacebar to contunue...")
    # if space == True:
    main()
   
#Todo: save to csv file from live capture
#todo: plot from csv file to live plot using funcanimation
#todo: Creatre classes to call from
