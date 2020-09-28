import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-pastel')

filepath = (r"C:\Users\ngaij\Desktop\Project Swallow Software\Python\Accelerometer\Set1.csv")
cols_list = ['Microphone1','X_Axis', 'Y_Axis', 'Z_Axis', 'Microphone2','Button']

def animate(i):
    df = pd.read_csv(filepath, header=None).drop_duplicates()
    df.columns = df.iloc[0]
    df = df.iloc[1:]

    M1 = df["Microphone1"].astype(float)
    X = df["X_Axis"].astype(float)
    Y = df["Y_Axis"].astype(float)
    Z = df["Z_Axis"].astype(float)
    M2 = df["Microphone2"].astype(float)
    btn = df["Button"].astype(float)

    plt.cla()
    plt.plot(M1, label="X-Axis")
    plt.plot(M2, label="Y-Axis")

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1)

plt.tight_layout()
plt.show()
