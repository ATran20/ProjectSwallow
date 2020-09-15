import serial
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    port = 'COM3'
    baudrate = 9600
    s = serial.Serial(port, baudrate)
    data = []
    values = []
    filepath = (r"C:\Users\TechFast Australia\Documents\Project\Accelerometer\Set 1")
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

        df = pd.DataFrame(matrix, columns=['Microphone1', 'X-Axis', 'Y_Axis', 'Z_Axis', 'Microphone2', 'Button'])
        df.to_csv(filepath, header=None, mode="a")

        fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(8,5))
        df['Microphone1'].plot(kind='line', ax=df[0,0], color='red')
        df['Microphone2'].plot(kind='line', ax=df[0,0], color='blue')
        axes[0,0].set_title('Mic')
        df['x_Axis'].plot(kind='line', ax=df[0,1], color='red')
        df['Y_Axis'].plot(kind='line', ax=df[0,1], color='blue')
        df['Z_axis'].plot(kind='line', ax=df[0,1], color='black')
        axes[0, 1].set_title('Aceel')
        df['Button'].plot(kind='line', ax=df[0,2], color='blue')
        axes[0, 2].set_title('Button')
        ax.set_xlabel("Seconds")
        ax.set_ylabel("Values")
        plt.show()

        # print(df)


if __name__ == '__main__':
    # space = input("Press Spacebar to contunue...")
    # if space == True:
    main()

# Todo: save to csv file from live capture
# todo: plot from csv file to live plot using funcanimation
# todo: Create classes to call from
