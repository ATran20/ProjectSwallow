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

        df = pd.DataFrame(matrix, columns=['X_Axis', 'Y-Axis', 'Z_Axis', 'Microphone1', 'Microphone2'])
        df.to_csv(filepath, header=None, mode="a")

        fig, ax = plt.subplots(dpi=120)
        df.plot(kind='line', y='X-Axis', ax=df, color='red')
        df.plot(kind='line', y='Y- Axis', ax=df, color='blue')
        df.plot(kind='line', y='Z- Axis', ax=df, color='black')
        df.plot(kind='line', y='Microphone', ax=df, colour='purple')
        df.plot(kind='line', y='Microphone2', ax=df, colour='green')
        ax.set_xlabel("Seconds")
        ax.set_ylabel("Values")
        plt.title('Demo graph for Line plots')
        plt.show()

        # print(df)


if __name__ == '__main__':
    # space = input("Press Spacebar to contunue...")
    # if space == True:
    main()

# Todo: save to csv file from live capture
# todo: plot from csv file to live plot using funcanimation
# todo: Create classes to call from
